#!/bin/bash

# 1. Run a Python Program in a Docker Container
echo -e "Creating Dockerfile for Python Program..."
echo -e "FROM python:3.8-slim\nWORKDIR /app\nCOPY . /app\nRUN pip install -r requirements.txt\nCMD ['python', 'your_script.py']" > Dockerfile

echo -e "Building Python Program Docker Image..."
docker build -t python-program .

echo -e "Running Python Program in Docker Container..."
docker run -d --name python-container python-program

# 2. Run a GUI Program in a Docker Container
echo -e "Allowing Docker containers to access X server..."
xhost +local:docker

echo -e "Running GUI Program in Docker Container (gedit)..."
docker run -it --rm --env DISPLAY=$DISPLAY --volume /tmp/.X11-unix:/tmp/.X11-unix your-docker-image-name gedit

# 3. Run a Machine Learning Model in a Docker Container
echo -e "Creating Dockerfile for ML Model..."
echo -e "FROM python:3.8-slim\nWORKDIR /app\nCOPY . /app\nRUN pip install -r requirements.txt\nCMD ['python', 'train_model.py']" > Dockerfile

echo -e "Building ML Model Docker Image..."
docker build -t ml-model .

echo -e "Running ML Model in Docker Container..."
docker run -d --name ml-container ml-model

# 4. Run Docker Inside Docker (DinD) with CentOS Image
echo -e "Running Docker Inside Docker (DinD) with CentOS..."
docker run --privileged -d --name dind-centos centos:latest /bin/bash -c "yum install -y docker && dockerd"

# 5. Launch VLC Player Inside a Docker Container
echo -e "Allowing Docker containers to access X server for VLC..."
xhost +local:docker

echo -e "Running VLC Player Inside Docker Container..."
docker run -it --rm --env DISPLAY=$DISPLAY --volume /tmp/.X11-unix:/tmp/.X11-unix jess/vlc

# 6. Launch a Web Server in Docker Container
echo -e "Launching Web Server (Nginx) in Docker Container..."
docker run -d --name web-server -p 8080:80 nginx

# 7. SSH into the Docker Running Container
echo -e "SSH into the running Docker container..."
docker exec -it python-container /bin/bash

# 8. Launch a Web Server in Docker Container and Connect to It from a Windows Host
echo -e "Running Web Server in Docker Container and Exposing Port 8080..."
docker run -d --name web-server -p 8080:80 nginx

echo -e "Access the web server from Windows using http://<Linux_VM_IP>:8080"

echo -e "All tasks have been completed successfully!"
