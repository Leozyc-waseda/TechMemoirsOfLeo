<h1 align="left">Slowfast kinetics400的数据集使用总结</h1>
<p align="left">
  <strong>在用kinetics400重新训练slowfast模型的时候踩的坑的记录。</strong>
</p>

## 📝 为什么写这个总结？

> 写这个readme是因为，我想要测试一下slowfast中的模型在kinetics400表现是否与github的精度一样的过程中，遇到了好多坑，记录一下。

---


- kinetics-400由于全是视频，全部下载大概需要450Gb的空间，请提前清理出来。
- [参考github的下载](https://github.com/cvdfoundation/kinetics-dataset)
## 1️. 下载文件
- 有人可能疑惑，为什么就下载一个东西有什么难的。这是因为kinetics400大多数是从Youtube上爬虫的，YouTube上这些视频有一些已经失效了。用slowfast官方的代码下载的话，会导致失败。
- [参考github的下载](https://github.com/cvdfoundation/kinetics-dataset)去这里下载，这个github都有500多星，看来有不少人被下载这个数据集折磨。
```bash
$ git clone https://github.com/cvdfoundation/kinetics-dataset.git 
$ cd kinetics-dataset

#如果你不想下载train和validation，记得把代码里面的train和validation注释掉
$ bash ./k400_downloader.sh
$ bash ./k400_extractor.sh
```

## 2准备Slowfast用的数据格式
- 如果觉得分步骤看代码太麻烦的话看这个[总结的代码就好](./source_code/Slowfast_kinetics-400/kinetics_data_processing.py)
### 2.1 csv的格式变换
- 成功的下载好了数据后，按照官方的指示，```train.csv, val.csv, test.csv```的准备是必要的。如下图所示。

[data_format](./picture/Slowfast_kinetics-400/data_format.png)


- 在我们下载的数据集中其实有```train.csv, val.csv, test.csv```,打开看了一下格式如下图所示。和官方要求的不一样，所以得修改。
[previsou_data](./picture/Slowfast_kinetics-400/previsou_data.png)


- 代码在这 [csv_transfer.py](./source_code/Slowfast_kinetics-400/csv_transfer.py)用这个代码去转换csv文件。

- 记得改路径，然后得到如下图after的文件格式，这个是slowfast官方要求的。
[before_after](./picture/Slowfast_kinetics-400/before_after.png)


### 2.2 用classids.json改变class id

- 官方没有提供classid的文件，可以从[这里下载](https://github.com/facebookresearch/video-nonlocal-net/blob/main/process_data/kinetics/classids.json)。可以看到是He kaiming大神初步initial commit的。
[class_id_init](./picture/Slowfast_kinetics-400/class_id_init.png)

### 2.3 检查csv文件的视频是否还存在
- [检查的代码](./source_code/Slowfast_kinetics-400/check_is_exist.py)

### 测试之前
- 按照[Slowfast 的环境构建总结](https://github.com/Leozyc-waseda/TechMemoirsOfLeo/blob/main/slowfast_install_2023_leo.md)，确保都做好了之后,按照下面的代码运行。[参考官方的开始建议手册](https://github.com/facebookresearch/SlowFast/blob/main/GETTING_STARTED.md)

```bash
python tools/run_net.py --cfg ~/SlowFast/configs/Kinetics/SLOWFAST_8x8_R50.yaml --opts DATA.PATH_TO_DATA_DIR ~/kinetics-dataset/k400/test/ TEST.CHECKPOINT_FILE_PATH ~/PySlowFast_Model_Zoo/SLOWFAST_8x8_R50.pkl TRAIN.ENABLE False TEST.ENABLE True TEST.CHECKPOINT_TYPE caffe2  DATA_LOADER.NUM_WORKERS 2

```