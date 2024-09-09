# VNC Camera Preview on Raspberry Pi 4

This guide explains how to set up a Raspberry Pi 4 with a Camera Module 3 to display a camera preview on a VNC session using OpenCV.

## Dependencies

First, install the required software packages:

```bash
sudo apt-get install realvnc-vnc-server
sudo apt install -y python3-picamera2 python3-opencv
sudo apt-get install v4l-utils
```

## Setup

### VNC

After installation, check if the host is accessible via VNC using a viewer compatible with the installed VNC Server.

### Systemd Service

Create a systemd service (`camera-preview.service`) to automatically start the camera preview after the graphical interface is ready. This service will restart automatically if it crashes.

```bash
# Enable, start then stop the service to test.
sudo systemctl enable camera-preview.service
sudo systemctl start camera-preview.service
# If there are issues check the status of the service
sudo systemctl status camera-preview.service
# Wait for a few seconds for the preview window to pop up
sudo systemctl stop camera-preview.service
```
