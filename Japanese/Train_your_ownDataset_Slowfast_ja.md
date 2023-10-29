<h1 align="center">Slowfast训练你自己的数据集</h1>
<p align="center">
  <strong>如何在Slowfast上训练自己的数据集</strong>
</p>

## 📝 为什么写这个总结？

> 最近有用到Slowfast来训练自己的数据，所以做一个总结。

---
- github上有大佬已经写出了如何训练自己的数据集的具体流程，[Github的回答](https://github.com/facebookresearch/SlowFast/issues/149#issuecomment-7232654619)

- 整体的流程入下图所示。主要需要改的部分就是下面的5个红色的圈圈。
![custom_total](./picture/custom_dataset_slowfast/custom_total.png)

## 1️⃣ data1 and data2的部分
- 首先，你需要创建一个配置文件（```.yaml```），三个用于数据集拆分的文件（```.csv```），一个用于引用类的文件（```.json```），以及一个用于解析数据集的文件（```mydata.py```）。
- 然后，你要确认你的数据是不是mp4的类型，如果不是需要把视频先转换成mp4，请交给chatGPT或者自己写。

## 2️⃣ 创建mydata.py
- 创建```mydata.py```：复制与```mydata.py```同一文件夹下的```kinetics.py```文件，重命名为mydata.py，并将其中所有的Kinetics替换为```Mydata```（注意大小写）。
- 导入mydata.py：在同一个文件夹的```__init__.py```文件中，添加
```from .mydata import Mydata。```

## 3️⃣ 创建classids.json
- 该文件包含类名和id的映射，如：
```
{"ClassA": 0, "ClassB": 1, "ClassC": 2}
```
## 4️⃣  .csv文件
- 定义哪些视频将被用于训练、验证和推理测试，以及它们引用的类。例如：
```bash
/SlowFast/data/MyData/ClassA/ins.mp4 0
/SlowFast/data/MyData/ClassC/tak.mp4 2
```
对于大型数据集，建议使用自动脚本来根据classids.json和文件夹结构创建此类文件。
- 注意：所有三个文件不应有相同的行（使用相同的视频），并注意您的实际路径（可以使用绝对或相对路径）。

## 5️⃣ 创建配置文件
- 复制```SlowFast/configs/Kinetics```文件夹中的现有文件，如```I3D_8x8_R50.yaml```，并替换其中的所有```kinetics```为```mydata```（注意大小写）。

## 6️⃣ 运行SlowFast
- 使用新配置运行以下命令：
```python /SlowFast/tools/run_net.py --cfg /SlowFast/configs/MyData/I3D_8x8_R50.yaml```
注意，可能需要根据你的实际工作目录调整路径。

### 快速 Access
- [🐧 Ubuntu 的 NVIDIA 安装](https://github.com/Leozyc-waseda/TechMemoirsOfLeo/blob/main/Ubuntu_NVIDIA_CUDA_INSTALL.md)
- [🚀 Slowfast 的环境安装](https://github.com/Leozyc-waseda/TechMemoirsOfLeo/blob/main/slowfast_install_2023_leo.md)
- [🎥 Slowfast 的 Kinetics-400 数据集训练调试成功](./Slowfast_kinetics-400.md)
- [📊 Slowfast 训练自己的数据集](./Train_your_ownDataset_Slowfast.md) 
- [💼 Ubuntu 的常用工作软件](./Ubuntu_Remote_Software.md) 
