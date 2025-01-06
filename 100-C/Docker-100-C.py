// Docker Automation Tasks

const { exec } = require('child_process');

// 1. Run a Python Program in a Docker Container
function runPythonInDocker() {
    exec('docker run --rm -v $(pwd):/app -w /app python:3.9 python script.py', (err, stdout, stderr) => {
        if (err) {
            console.error(`Error: ${stderr}`);
        } else {
            console.log(`Output: ${stdout}`);
        }
    });
}

// 2. Run a GUI Program in a Docker Container
function runGUIProgramInDocker() {
    exec('docker run --rm -e DISPLAY=$DISPLAY -v /tmp/.X11-unix:/tmp/.X11-unix gui-app-image', (err, stdout, stderr) => {
        if (err) {
            console.error(`Error: ${stderr}`);
        } else {
            console.log(`GUI Program launched.`);
        }
    });
}

// 3. Run a Machine Learning Model in a Docker Container
function runMLModelInDocker() {
    exec('docker run --rm -v $(pwd):/app -w /app tensorflow/tensorflow:latest python ml_model.py', (err, stdout, stderr) => {
        if (err) {
            console.error(`Error: ${stderr}`);
        } else {
            console.log(`ML Model Output: ${stdout}`);
        }
    });
}

// 4. Run Docker Inside Docker (DinD) with CentOS Image
function runDinD() {
    exec('docker run --privileged --rm -it docker:stable-dind', (err, stdout, stderr) => {
        if (err) {
            console.error(`Error: ${stderr}`);
        } else {
            console.log(`DinD Environment Launched.`);
        }
    });
}

// 5. Launch VLC Player Inside a Docker Container
function launchVLCInDocker() {
    exec('docker run --rm -e DISPLAY=$DISPLAY -v /tmp/.X11-unix:/tmp/.X11-unix jess/vlc', (err, stdout, stderr) => {
        if (err) {
            console.error(`Error: ${stderr}`);
        } else {
            console.log(`VLC Player Launched.`);
        }
    });
}

// 6. Launch Webserver in Docker Container
function launchWebserverInDocker() {
    exec('docker run --rm -d -p 8080:80 httpd', (err, stdout, stderr) => {
        if (err) {
            console.error(`Error: ${stderr}`);
        } else {
            console.log(`Webserver running on http://localhost:8080`);
        }
    });
}

// 7. SSH in the Docker Running Container
function sshIntoDockerContainer() {
    exec('docker exec -it container_id /bin/bash', (err, stdout, stderr) => {
        if (err) {
            console.error(`Error: ${stderr}`);
        } else {
            console.log(`Connected to Docker Container.`);
        }
    });
}

// 8. Launch Webserver and Connect from Host System
function launchWebserverAndConnect() {
    exec('docker run --rm -d -p 8080:80 nginx', (err, stdout, stderr) => {
        if (err) {
            console.error(`Error: ${stderr}`);
        } else {
            console.log(`Webserver running. Access it at http://<host-ip>:8080`);
        }
    });
}

module.exports = {
    runPythonInDocker,
    runGUIProgramInDocker,
    runMLModelInDocker,
    runDinD,
    launchVLCInDocker,
    launchWebserverInDocker,
    sshIntoDockerContainer,
    launchWebserverAndConnect
};
