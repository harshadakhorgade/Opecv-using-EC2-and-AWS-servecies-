# Opecv-using-EC2-and-AWS-servecies-
# This is a Python project that performs face and eye detection using AWS Rekognition and Haarcascades. 

# First need create instance
#here i am using ubuntu os

IAM role is required and that attach to ec2-instance

IAM users required for acess key

#connect to ssh

# follow thse cammond
sudo su
sudo apt update
sudo apt upgrade

sudo apt install python3
python3 --version

sudo apt install python3-venv
python3 -m venv env
. env/bin/activate

sudo apt install python3-pip
pip3 install opencv-python numpy boto3 termcolor matplotlib


mkdir opencv 
cd opencv
# xml file for detect face and eye
wget https://github.com/opencv/opencv/raw/master/data/haarcascades/haarcascade_frontalface_default.xml


wget https://github.com/opencv/opencv/raw/master/data/haarcascades/haarcascade_eye.xml


pip install awscli 
aws configure Acess_key Sceret key

sudo apt-get install xvfb
sudo apt install xorg-x11-server-Xvfb

vi detection.py 


# Change ownership to ec2-user for the 'photo' directory and its contents
sudo chown -R ec2-user:ec2-user /home/ec2-user/opencv/photo/

# local to ec2
run on cmd
scp -i "C:\Users\Harsahada Khorgade\Downloads\yeskey.pem" "C:\Users\Harsahada Khorgade\Downloads\opencv\elon.jpg" ubuntu@16.171.174.63:/home/ubuntu/opencv

//use public ip address here


sudo apt install mesa-libGL
sudo apt install mesa-libGLU
pip install pyvirtualdisplay

# RUN FILE
python detection.py elon.jpg


# ec2 to local

scp -i "C:\Users\Harsahada Khorgade\Downloads\yeskey.pem" ubuntu@3.109.133.244:\home\ubuntu\opencv\result_with_eyes.jpg "C:\Users\Harsahada Khorgade\Downloads"
 //use public ip adress here




# OUPUT
result_with_eyes.jpg

![Example Image](result_with_eyes.jpg)