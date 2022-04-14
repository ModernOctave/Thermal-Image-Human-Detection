# System Requirements
Note this process requires NVIDIA Container Toolkit which is only supported on specific linux distributions (mostly Ubuntu LTS)! Details about this can be found [here](https://docs.nvidia.com/datacenter/cloud-native/container-toolkit/install-guide.html#linux-distributions).

# Install Docker
Follow the instructions given [here](https://docs.docker.com/engine/install/ubuntu/).

# Install NVIDIA Container Toolkit
Follow the instructions given [here](https://docs.nvidia.com/datacenter/cloud-native/container-toolkit/install-guide.html#setting-up-nvidia-container-toolkit)

# Pull TensorFlow NGC Container
Pull the latest TensorFlow NGC Container from [here](https://catalog.ngc.nvidia.com/orgs/nvidia/containers/tensorflow).

Note: Choose the image corresponding to the Tensorflow version the model was trained on.

# Optimize Model
Optimize the model using TF-TRT using the instructions given [here](https://docs.nvidia.com/deeplearning/frameworks/tf-trt-user-guide/index.html?ncid=so-yout-578539#usingtftrt).