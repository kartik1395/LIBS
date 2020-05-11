# VISION BASED MISPLACED BOOK DETECTION SYSTEM USING DEEP CONVOLUTIONAL NEURAL NETWORKS

## To obtain project files
- Open the link https://drive.google.com/drive/folders/1Xb967iqmi_-V1z3RyVsWHxjPfQwEvjf4?usp=sharing
- Download the zip called IRS_Project.zip

## Requirements

- Windows PC 

- **CMake >= 3.8** for modern CUDA support: https://cmake.org/download/

- **CUDA 10.0**: https://developer.nvidia.com/cuda-toolkit-archive (on Linux do [Post-installation Actions](https://docs.nvidia.com/cuda/cuda-installation-guide-linux/index.html#post-installation-actions))

- **OpenCV >= 2.4**: use your preferred package manager (brew, apt), build from source using [vcpkg](https://github.com/Microsoft/vcpkg) or download from [OpenCV official site](https://opencv.org/releases.html) (on Windows set system variable `OpenCV_DIR` = `C:\opencv\build` - where are the `include` and `x64` folders [image](https://user-images.githubusercontent.com/4096485/53249516-5130f480-36c9-11e9-8238-a6e82e48c6f2.png))

- **cuDNN >= 7.0 for CUDA 10.0** https://developer.nvidia.com/rdp/cudnn-archive (on **Linux** copy `cudnn.h`,`libcudnn.so`... as desribed here https://docs.nvidia.com/deeplearning/sdk/cudnn-install/index.html#installlinux-tar , on **Windows** copy `cudnn.h`,`cudnn64_7.dll`, `cudnn64_7.lib` as desribed here https://docs.nvidia.com/deeplearning/sdk/cudnn-install/index.html#installwindows )

- **GPU with CC >= 3.0**: https://en.wikipedia.org/wiki/CUDA#GPUs_supported

-  **Python** >=3.5

- **Pytesseract**

  

## Installation

- Navigate to darknet/builld/darknet/x64 & Install darknet using steps : https://github.com/AlexeyAB/darknet#how-to-compile-on-windows-using-cmake-gui

## Training (Optional)

- Run : darknet.exe detector train cfgk/obj.data cfgk/yolov3.cfg darknet19_448.conv.23
- **For object detection using pretrained weights** : darknet.exe detector test cfgk/obj.data cfgk/yolov3.cfg backup/yolov3_6000.weights file_name.jpg

## Inference

- Navigate to darknet/builld/darknet/x64 
- For full project execution python3 libs.py

