# Face Recognition using Tensorflow and Facenet
---------------------------------------------------------------------------------------------------------
## Pre-trained models
| Model name      | LFW accuracy | Training dataset | Architecture |
|-----------------|--------------|------------------|-------------|
| [20180408-102900](https://drive.google.com/open?id=1R77HmFADxe87GmoLwzfgMu_HY0IhcyBz) | 0.9905        | CASIA-WebFace    | [Inception ResNet v1](https://github.com/davidsandberg/facenet/blob/master/src/models/inception_resnet_v1.py) |
| [20180402-114759](https://drive.google.com/open?id=1EXPBSXwTaqrSC0OhUdXNmKSh9qJUQ55-) | 0.9965        | VGGFace2      | [Inception ResNet v1](https://github.com/davidsandberg/facenet/blob/master/src/models/inception_resnet_v1.py) |

## Requirements
pip3 install -r requirements.txt

## Structure:
- ``pretrain_models``:
    Contains training model, support for verification.
- ``src``:
    Contains the source code of the program.
- ``align``:
        Detect and align face size. Default: 160x160

## Run code
- ``python3 src/extract_frame_from_cam.py``:
        Extract frame image from camera
- ``python3 src/align/align_dataset_mtcnn.py``:
        Cut face from image (shape: 160x160)
- ``python3 src/classifier.py``:
        training classifier SVM
- ``python3 src/_face_rec_cam.py``:
        face recognition from camera
        