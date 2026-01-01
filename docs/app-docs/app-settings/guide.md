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
- **Mirror camera**: Flip the camera preview horizontally (doesn't affect tracking)

**Tips**:
- Position camera at eye level for best tracking
- Ensure good lighting on your face
- USB 3.0 cameras generally perform better than USB 2.0

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
