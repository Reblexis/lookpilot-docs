This guide explains how to set up and use the virtual camera feature in LookPilot on Linux.

## What is Virtual Camera

The virtual camera feature creates a virtual camera device that mirrors the input from your selected physical camera. This allows you to use your camera in multiple applications simultaneously - for example, you can use LookPilot for head tracking while also using the same camera feed in OBS for streaming or in video conferencing applications.

## Where to Enable

The virtual camera can be enabled in **Settings > Camera**.

1. Open LookPilot
2. Go to **Settings** (top menu)
3. Select the **Camera** tab
4. Find the **Virtual camera** section
5. Check **Enable virtual camera**

## Prerequisites

Before enabling the virtual camera, you need to install the `v4l2loopback` kernel module and run the setup script.

### 1. Install v4l2loopback

Install the v4l2loopback kernel module for your distribution:

**Ubuntu/Debian**:
```bash
sudo apt-get install v4l2loopback-dkms
```

**Fedora**:
```bash
sudo dnf install v4l2loopback
```

**Arch Linux**:
```bash
sudo pacman -S v4l2loopback-dkms
```

### 2. Run the Setup Script

After installing v4l2loopback, run the LookPilot virtual camera setup script:

```bash
sudo /path/to/LookPilot/data/static/scripts/virtualcam_linux.sh
```

**Note**: Replace `/path/to/LookPilot/` with the actual path to your LookPilot installation. If you're unsure of the path, LookPilot will show it in the error message if you try to enable the virtual camera without running the setup first.

This script will:
- Load the v4l2loopback module with the correct parameters
- Create the virtual camera device at `/dev/video12`
- Configure the system to load the module automatically at boot

## Setup Process

Once the prerequisites are installed:

1. Check the **Enable virtual camera** checkbox in Settings > Camera
2. The virtual camera device will be created at `/dev/video12`
3. LookPilot will start sending camera frames to the virtual camera

The virtual camera will appear as **"VirtualCam"** in other applications.

### Using the Virtual Camera

Once enabled, the virtual camera device is available system-wide:

1. Keep LookPilot running with the virtual camera enabled
2. Open any application that uses a camera (OBS, Zoom, Discord, etc.)
3. Select **"/dev/video12"** or **"VirtualCam"** from the camera/video device list
4. The application will now receive the camera feed from LookPilot

## Use Cases

**Streaming and Recording**:
- Use in OBS Studio to stream or record your camera feed while using head tracking in games
- Apply filters or overlays in OBS while maintaining head tracking functionality

**Video Conferencing**:
- Use the same camera for head tracking and video calls (Zoom, Discord, Microsoft Teams)
- Share your camera in meetings while gaming or using head tracking applications

**Multi-Application Camera Sharing**:
- Use your camera in multiple applications simultaneously without conflicts

## Troubleshooting

### Virtual Camera Fails to Start

If you see an error when trying to enable the virtual camera:

**Check if v4l2loopback is installed**:
```bash
modinfo v4l2loopback
```

If this command fails, install v4l2loopback using the commands in the Prerequisites section above.

**Run the setup script**:
```bash
sudo /path/to/LookPilot/data/static/scripts/virtualcam_linux.sh
```

### Device Already in Use

If you get an error that `/dev/video12` is already in use:

**Check which processes are using the device**:
```bash
sudo lsof /dev/video12
```

Close any applications shown in the output, then try enabling the virtual camera again.

### Permission Denied

If you get permission errors:

1. Make sure you ran the setup script with `sudo`
2. Check that your user is in the `video` group:
   ```bash
   groups $USER
   ```
3. If not in the video group, add yourself:
   ```bash
   sudo usermod -a -G video $USER
   ```
4. Log out and log back in for the group change to take effect

### Virtual Camera Not Loading at Boot

If the virtual camera device doesn't exist after rebooting:

**Check if the module is configured to load**:
```bash
cat /etc/modules-load.d/v4l2loopback.conf
```

This should contain `v4l2loopback`. If the file doesn't exist or is empty, run the setup script again:
```bash
sudo /path/to/LookPilot/data/static/scripts/virtualcam_linux.sh
```

**Manually load the module** (temporary until next reboot):
```bash
sudo modprobe v4l2loopback devices=1 video_nr=12 card_label='VirtualCam' exclusive_caps=1
```

### Virtual Camera Stops Working

If the virtual camera stops functioning:

1. Uncheck **Enable virtual camera** in Settings > Camera
2. Wait a few seconds
3. Check **Enable virtual camera** again

If the issue persists:
1. Close all applications using the virtual camera
2. Restart LookPilot
3. Re-enable the virtual camera

### Camera Feed is Frozen or Delayed

1. Check that your physical camera is working properly in LookPilot's camera preview
2. Close unnecessary applications that might be using the camera
3. Try disabling and re-enabling the virtual camera
4. If the issue persists, restart LookPilot



