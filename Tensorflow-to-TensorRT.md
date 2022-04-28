# Install Docker
Follow the instructions given [here](https://docs.docker.com/engine/install/).

# Hardware Acceleration
NVIDIA Container Toolkit may be installed to take advantage of hardware acceleration during the process. Note NVIDIA Container Toolkit which is only supported on specific linux distributions (mostly Ubuntu LTS)! Details about this can be found [here](https://docs.nvidia.com/datacenter/cloud-native/container-toolkit/install-guide.html#linux-distributions). If supported install the NVIDIA Container Toolkit by following the instructions given on the same page.

Note: If you are running a non-LTS version of Ubuntu (18.04+), manually setting the value of environmental variable ```distribution``` to the previous LTS version of Ubuntu may work. [[Source]](https://github.com/NVIDIA/nvidia-docker/issues/1574#issuecomment-986632998)

# Install NVIDIA Container Toolkit (Optional)
Follow the instructions given [here](https://docs.nvidia.com/datacenter/cloud-native/container-toolkit/install-guide.html#setting-up-nvidia-container-toolkit)

# Pull TensorFlow NGC Container
Pull the latest TensorFlow NGC Container from [here](https://catalog.ngc.nvidia.com/orgs/nvidia/containers/tensorflow).

Note: Choose the image corresponding to the Tensorflow version the model was trained on (TF2 if model was trained using this repo).

# Optimize Model
Optimize the model using TF-TRT optimizer using this command:
```
python3 Tensorflow-to-TensorRT.py <paths to unoptimized models>
```
The optimized model will be saved to the same directory as the unoptimized model with '-RT' suffix.

The script is designed refering to [this](https://docs.nvidia.com/deeplearning/frameworks/tf-trt-user-guide/index.html?ncid=so-yout-578539#usingtftrt).