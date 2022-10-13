FROM nvidia/cuda:11.3.1-devel-ubuntu20.04

#Ubuntu update & upgrade 
#install git 
RUN apt-get update \
    && apt-get upgrade -y \
    && apt-get autoremove -y \
    && apt-get install -y git 

#install python3 pip3 
RUN apt-get install -y python3-pip
RUN python3 -m pip install --upgrade pip

#install pytorch
RUN pip3 install torch torchvision torchaudio --extra-index-url https://download.pytorch.org/whl/cu113

