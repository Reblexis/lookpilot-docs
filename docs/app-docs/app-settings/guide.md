This guide covers application settings in LookPilot. These settings affect how the application behaves and are separate from your tracking presets.

## Interface

Found in **Settings > Interface**.

### Language
- Choose your preferred interface language
- Restart required for changes to take effect

## Camera

Found in **Settings > Camera**.

### Camera Selection
- **Select camera**: Choose from available webcams
- **Reload button (⟲)**: Refresh the camera list
- **Resolution**: Choose camera resolution
  - 1280x720 recommended for most setups
  - 640x480 for lower-end systems
  - 1920x1080 for high-end systems (may reduce camera FPS)
  - Each resolution entry lists its maximum framerate, and LookPilot always runs the highest framerate the camera offers at the selected resolution. High-fps modes (90-120 fps) are usually only available at lower resolutions - pick 720p or lower to unlock them.
- **Mirror camera**: Flip the camera preview horizontally (doesn't affect tracking)
- **Auto exposure**: Lets the camera manage exposure automatically. In dim rooms auto exposure can silently halve your camera's framerate; disabling it (and lighting your face from the front) restores full fps.
- **Use GStreamer**: Capture backend with the lowest latency. Try disabling it if your camera fails to load.
- **Use MJPEG**: Compressed capture that reduces USB bandwidth on high-resolution cameras. Disable it if the camera fails to load or shows "format not supported" errors.
- **Use DirectShow** (Windows): Legacy capture API. Enable it for older cameras that do not work with the default backend - e.g. the PS3 Eye (see Troubleshooting).

**Tips**:
- Position camera at eye level for best tracking
- Ensure good lighting on your face
- USB 3.0 cameras generally perform better than USB 2.0
- Plug the camera in directly - USB hubs can limit bandwidth and framerate

### Choosing a Webcam
- **Framerate beats resolution**: 30 fps is the workable minimum, 60 fps is the sweet spot, above 60 the gains are minimal. 720p at 60 fps is the recommended target.
- **Field of view does not affect tracking quality** as long as the image is undistorted - a wider FOV just allows bigger physical movements.
- **Community-verified models**: Logitech C920 / C922 / C925e / C270 / Brio / StreamCam, EMEET C950 (1080p60), OBSBOT Meet SE (100 fps), Ugreen 1080p60, PS3 Eye (~60 fps, very cheap; on Windows it needs a DirectShow driver - see Troubleshooting).
- **Phones work well as cameras**: on Windows use DroidCam or iVCam as the bridge app and connect over **USB, not Wi-Fi** (Wi-Fi latency makes tracking floaty); the phone then appears in the camera dropdown. Keep the phone near eye level.
- Cameras with built-in IR illumination (e.g. ELP KL36IR) are a community-recommended option for playing in the dark.

## Tracking

Found in **Settings > Tracking**.

### Performance

**Tracking FPS limit**:
- Range: 5-240 FPS
- Default: 60 FPS
- Lower values reduce CPU usage but may impact smoothness
- Actual FPS also limited by your camera's capabilities

**Head tracking mode**:
- **Static**: Single-frame prediction
- **Temporal (experimental)**: Uses LSTM for smoother tracking

## Keybinds

Found in **Settings > Keybinds**. Here you can bind your mouse buttons / keyboard keys / joystick buttons to different actions.

### System Keybinds

**Center Tracking**:
- Default: Ctrl+Space
- Resets your current head position as the neutral center

**Toggle Tracking**:
- Default: Not assigned
- Starts or stops head tracking

**Pause Tracking**:
- Default: Not assigned
- Freezes tracking at your current pose (unlike Toggle, which recenters when tracking restarts) - useful for holding a view while clicking small cockpit switches

### Setting Keybinds

1. Click in the keybind field
2. Press the desired key combination
3. Automatically saved

**Good choices**: Combinations with Ctrl, Alt, or Shift (e.g., Ctrl+Space, Alt+F1)

**Avoid**: Single letters/numbers that games use, common shortcuts (Ctrl+C, Alt+Tab)

**Note**: Preset keybinds are configured in the preset management window, not here. See the Presets guide for details.

## Posture

Found in **Settings > Posture** (if posture monitoring is enabled).

### Posture Monitoring

**Enable posture monitoring**:
- Monitor your head position and show warnings when your posture needs adjustment

**Warning threshold**:
- Distance below center position that triggers a warning (in cm)
- Higher values are more sensitive

**Warning delay**:
- How long to wait before showing a warning after bad posture is detected (in seconds)

### Current Status

Displays your current head position and warning status.

### Set Center Position

Use the "Set as center" button to set your current position as the reference for posture monitoring.

## Privacy

Found in **Settings > Privacy**.

**Send usage statistics**:
- Default: Enabled
- Helps improve the app by sending anonymous usage data

**Send gaze data**:
- Default: Disabled
- Helps improve eye tracking models by sending anonymized gaze data
