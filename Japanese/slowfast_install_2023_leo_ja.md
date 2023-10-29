# Meta (Facebook AI) Slowfast の環境構築のまとめ
## 🚀 背景
- このreadmeを書く理由は、Slowfastを構築する際に、多くの変更が必要だったためです。[公式インストールガイド](https://github.com/facebookresearch/SlowFast/blob/main/INSTALL.md)のreadmeは2年前のものですので、この記事が他の方々の参考になればと思います。

- また、Slowfastを使用して独自のモデルをトレーニングする方法についても書きました。[Slowfastのカスタマイズ](./Train_your_ownDataset_Slowfast.md)。

- インストール前にNVIDIA Driver、CUDA、CUDNNが正しくインストールされていることを確認してください。インストールしていない場合は、[UbuntuのNVIDIAのインストールガイド](https://github.com/Leozyc-waseda/TechMemoirsOfLeo/blob/main/Ubuntu_NVIDIA_CUDA_INSTALL.md)を参照してください。最後に`python nvidia-smi`や`python nvcc -V`の結果が表示されれば、通常は問題ありません。

## 🛠 インストール手順
### 1. 新しいPython環境を作成
```bash
# Anacondaを使用しているユーザー
$ conda create -n slowfast python=3.8

# 企業のポリシーでAnacondaが使用できないユーザー
$ mkdir my_venv
$ cd my_venv
$ python3 -m venv
$ python3 -m venv my_venv
$ source my_venv/bin/activate


### 2. Pytorchのインストール。[Pytorch​](https://pytorch.org/get-started/previous-versions/), から、自分のcuda versionに応じてインストールしてください。最新版は、多くのオープンソースソフトウェアで未対応の可能性があります。
```bash 
# 私のPCの場合
$ pip install torch==1.13.1+cu117 torchvision==0.14.1+cu117 torchaudio==0.13.1 --extra-index-url https://download.pytorch.org/whl/cu117
```
### [公式インストールガイド](https://github.com/facebookresearch/SlowFast/blob/main/INSTALL.md)を参考にして、以下のパッケージをインストール:
```bash
# fvcore
$ pip install 'git+https://github.com/facebookresearch/fvcore'
or
$ git clone https://github.com/facebookresearch/fvcore
$ cd fvcore
$ python setup.py install

# simplejson
$ pip install simplejson

# PyAV
$ conda install av -c conda-forge
or
$ pip install av

# iopath
$ pip install -U iopath 
or 
$ conda install -c iopath iopath

# psutil
$ pip install psutil

# OpenCV
$ pip install opencv-python

# tensorboard
$ pip install tensorboard

# moviepy
$ conda install -c conda-forge moviepy 
or 
$ pip install moviepy

# PyTorchVideo
$ pip install pytorchvideo
or
$ pip install "git+https://github.com/facebookresearch/pytorchvideo.git"

# FairScale
$ pip install 'git+https://github.com/facebookresearch/fairscale'

# cython
$ pip install -U torch torchvision cython

# Detectron2
$ git clone https://github.com/facebookresearch/detectron2 detectron2_repo
$ pip install -e detectron2_repo

# scipy
$ pip install scipy

# pandas    
$ pip install pandas

# scikit-learn   
$ pip install scikit-learn
```


### 3.環境変数の設定
```bash
$ sudo nano ~/.bashrc
$ export PYTHONPATH=/path/to/your/SlowFast/slowfast:$PYTHONPATH
$ source  ~/.bashrc
$ cd ./slowfast
$ python setup.py build develop

```

### 4. テストプログラムを実行。もし、運が良ければ、以下の画像が表示されるはずです。
```bash
$ python tools/run_net.py --cfg configs/Kinetics/C2D_8x8_R50.yaml NUM_GPUS 1 TRAIN.BATCH_SIZE 8 SOLVER.BASE_LR 0.0125 DATA.PATH_TO_DATA_DIR path_to_your_data_folder
```
![install_OK_picture](./picture/picture_for_install/install_OK_picture.png)


### 🚧 トラブルシューティング

- いくつかの理由、例えば我々が一つのGPUしか持っていないのに対して、Facebookの人々が8つのGPUを使用している、また彼らのOSSバージョンが古いため一部のOSSが使用できなくなっているなどの理由で、トラブルシューティングが必要です。以下は私のPCの状況ですが、他の方は参考として、具体的には各自のPCのエラーをもとにデバッグしてください。

- ```SLOWFAST_8x8_R50.yaml```(必要なモデル構造を使用してください)内のBATCH_SIZE: 12, NUM_GPUS: 1, NUM_WORKDERS

- ```probe_video_from_memory```または```-Failed to decode by pyav with exception: unsupported operand type(s) for -: 'list' and 'int'```のエラー
[参考](https://github.com/facebookresearch/SlowFast/issues/181#issuecomment-1179203872)。この[Pull request](https://github.com/facebookresearch/SlowFast/pull/541/files)に従ってコードを変更してください。
![install_OK_picture](./picture/picture_for_install/probe_video_from_memory.png)

- ```defaults.py```
```bash
# torchvision 改成pyav
_C.DATA.DECODING_BACKEND = "pyav"
```
![pyav](./picture/picture_for_install/pyav.png)

### すべてが順調であれば、Slowfastを実行できるようになります~(参考4.)
- inetics-400を使用してモデルの性能をテストする必要がある場合、参考[这篇笔记​](https://github.com/facebookresearch/SlowFast/pull/541/files)。を参照してください。Kinetics-400には多くの失効したコードがあり、完全なファイルをダウンロードするのが困難で、Kinetics-400のデータセットを使用したトレーニングテストをスムーズに行うことができません。

- Slowfastを使用して独自のモデルをトレーニングする方法が必要な場合[Slowfast的Kinetics-400数据集训练调试成功​](..).

### 🔗 参考链接


１．[阮喵喵のrmmv開発ノート​](https://www.ruan-cat.com/ruan-cat-own-notes/python/SlowFast/SlowFast.html).​

２．[公式インストールガイド.](https://github.com/facebookresearch/SlowFast/blob/main/INSTALL.md).​

### 快速 Access
- [🐧 UbuntuのNVIDIAインストール](https://github.com/Leozyc-waseda/TechMemoirsOfLeo/blob/main/Ubuntu_NVIDIA_CUDA_INSTALL.md)
- [🚀 Slowfastの環境セットアップ](https://github.com/Leozyc-waseda/TechMemoirsOfLeo/blob/main/slowfast_install_2023_leo.md)
- [🎥 SlowfastのKinetics-400データセットトレーニングデバッグ成功](./Slowfast_kinetics-400.md)
- [📊  Slowfastでの独自データセットのトレーニング](./Train_your_ownDataset_Slowfast.md) 
- [💼 Ubuntuの主要な業務ソフトウェア](./Ubuntu_Remote_Software.md) 

# not finish yet.