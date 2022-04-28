# About
This project is a proof of concept for a human detection system which utilizes thermal images. This branch is designed to use a Raspberry Pi along with a Adafruit MX90640 IR Thermal camera. The camera provides a resolution of 24x32 pixels.

## Pretrained Models
A few pretrained models have been included in this repo. They can be extracted from the [zip](models/MLX90640-models.zip). Models have aslo been provided in TRT optimized form, these are suffixed with '-TRT'. The description of the models are as follows:

| Model Code      | Layers |         |         |         |        |         |         |          |          |         |        | Testing Accuracy | FPS  | FPS (TRT) |
|-----------------|--------|---------|---------|---------|--------|---------|---------|----------|----------|---------|--------|------------------|------|-----------|
| Human-Detection | conv16 | maxpool | conv32  | maxpool | conv64 | maxpool | flatten | dense64  | dense1   |         |        |            0.933 |  914 |       969 |
|               0 | conv16 | conv16  | maxpool | conv32  | conv32 | conv64  | conv64  | flatten  | dense128 | dense64 | dense1 |            0.967 |  707 |       717 |
|               1 | conv16 | maxpool | conv32  | maxpool | conv64 | maxpool | flatte  | dense128 | dense128 | dense64 | dense1 |            0.967 | 1038 |      1143 |
|               2 | conv16 | conv32  | conv32  | maxpool | conv64 | conv64  | maxpool | flatten  | dense128 | dense64 | dense1 |                1 |  872 |       855 |

Note: FPS values are recorded on a system with Intel 11th Gen i5 processor with 16 GB of RAM.

# Setup Instructions (Incomplete!)
Clone the repo:
```
git clone --branch MLX90640 https://github.com/ModernOctave/Thermal-Image-Human-Detection.git
```
Extract the models:
```
unzip models/MLX90640-models.zip -d models/
```
Create a virtual environment and install the required packages:
```
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```
Now run the human detection script:
```
python3 live-human-detection.py <path to model>
```

# Build Instructions
To design and build a custom model refer to the [Jupyter Notebook](make-model.ipynb) in the project root. It contains a series of steps to build a custom model with descriptions of each step.

## Optimizing the Model for NVIDIA GPUs
The model trained above can be optimized for NVIDIA GPUs by using the TensorRT optimizer. To do this refer to [these instructions](Tensorflow-to-TensorRT.md).