This guide explains how to set up and use the virtual camera feature in LookPilot on Windows.

## What is Virtual Camera

The virtual camera feature creates a virtual camera device that mirrors the input from your selected physical camera. This allows you to use your camera in multiple applications simultaneously - for example, you can use LookPilot for head tracking while also using the same camera feed in OBS for streaming or in video conferencing applications.

## Where to Enable

The virtual camera can be enabled in **Settings > Camera**.

1. Open LookPilot
2. Go to **Settings** (top menu)
3. Select the **Camera** tab
4. Find the **Virtual camera** section
5. Check **Enable virtual camera**

## Setup Process

### First-Time Setup

When you enable the virtual camera for the first time, LookPilot will automatically install the required driver:

1. Check the **Enable virtual camera** checkbox
2. **Administrator privileges may be required** - if prompted, allow the installation
3. The driver installation happens automatically in the background
4. Once complete, the virtual camera device will be available

The virtual camera will appear as **"Cight Virtual Camera"** in other applications.

### Using the Virtual Camera

Once enabled, the virtual camera device is available system-wide:

1. Keep LookPilot running with the virtual camera enabled
2. Open any application that uses a camera (OBS, Zoom, Discord, etc.)
3. Select **"Cight Virtual Camera"** from the camera/video device list
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

### Virtual Camera Not Appearing in Applications

**Solution**: Restart the application or LookPilot
1. Disable the virtual camera in LookPilot settings
2. Close and reopen the application that should see the virtual camera
3. Re-enable the virtual camera in LookPilot
4. The camera should now appear in the application's device list

### Driver Installation Failed

If the automatic driver installation doesn't work:

1. Navigate to the LookPilot installation folder
2. Find the `libs/installers/` directory
3. Run `softcam_installer.exe` manually with administrator privileges
4. Restart LookPilot and try enabling the virtual camera again

### Virtual Camera Stops Working

**Known Issue**: The virtual camera may occasionally stop functioning and require a reset.

**Solution**: Restart the virtual camera
1. Uncheck **Enable virtual camera** in Settings > Camera
2. Wait a few seconds
3. Check **Enable virtual camera** again
4. The virtual camera should now be working

If the issue persists:
1. Close all applications using the virtual camera
2. Restart LookPilot
3. Re-enable the virtual camera

### Camera Feed is Frozen or Delayed

1. Check that your physical camera is working properly in LookPilot's camera preview
2. Close unnecessary applications that might be using the camera
3. Try disabling and re-enabling the virtual camera
4. If the issue persists, restart LookPilot



