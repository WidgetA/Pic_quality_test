# PNG_test
 
## 用途
本项目用于测试不同的图片生成方式是否有损。

## 用法
### 环境准备
1. python 3.6/3.7
2. opencv 4.1/3.2
3. ffmpeg

### 运行脚本
1. 运行`read_save.py`脚本，将`test_video`中的视频所有帧按照既定方式（npy/bmp/png/ffmpeg-png）解码并存储。
2. 运行`load_compare.py`脚本，读入并对比RGB矩阵。