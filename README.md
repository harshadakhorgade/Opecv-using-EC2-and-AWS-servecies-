# Opecv-using-EC2-and-AWS-servecies-
This is a Python project that performs face and eye detection using AWS Rekognition and Haarcascades. 

First need create instance
#here i am using amzon linux os

IAM role is required and that attach to ec2-instance

IAM users required for acess key

#connect to ssh

follow thse cammond
sudo yum install python3

sudo yum install python3-pip

pip3 install opencv-python numpy boto3 termcolor matplotlib

mkdir myproject

xml file for detect face and eye
wget https://github.com/opencv/opencv/raw/master/data/haarcascades/haarcascade_frontalface_default.xml wget https://github.com/opencv/opencv/raw/master/data/haarcascades/haarcascade_eye.xml

mkdir opencv

pip install awscli

aws configure Acess_key Sceret key

thse is soln for error occur when file not run

sudo apt-get install xvfb

sudo yum install xorg-x11-server-Xvfb

Change ownership to ec2-user for the 'photo' directory and its contents
sudo chown -R ec2-user:ec2-user /home/ec2-user/opencv/photo/

local to ec2
scp -i MUMBAI_KEY.pem srk.png ec2-user@35.154.28.254:/home/ec2-user/opencv/photo/

#ec2 to local

scp -i MUMBAI_KEY.pem ec2-user@3.109.133.244:/path/to/source/on/ec2/girl.png C:\Users\Admin\PycharmProjects\OPENCV

RUN FILE
python detection.py -t photo/group.webp

Ec2 instance don't have direct permission for acess image so for that first we save image in form of.png file for image and .avi for vedio and then thse file transfer on local terminal i am using pycham and we easily see image

OUPUT
