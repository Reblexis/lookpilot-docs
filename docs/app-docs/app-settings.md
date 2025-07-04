# App Settings

This guide covers all the application settings in LookPilot, organized by category. These settings affect how the application behaves and are separate from your tracking presets.

## Camera Settings

Camera settings configure your webcam and are found in **Settings > Camera**.

### Camera Selection
- **Select camera**: Choose from available webcams
- **Reload button (⟲)**: Refresh the list of available cameras
- **None selected**: Shows "No camera" until you select one

### Camera Configuration
- **Resolution**: Choose camera resolution (e.g., 1280x720, 1920x1080)
  - Higher resolutions provide better tracking quality but use more system resources and may run at lower FPS
  - 1280x720 is recommended for most setups
  - 640x480 for lower-end systems
  - 1920x1080 for high-end systems with powerful computers (may reduce camera FPS)

- **Mirror camera**: Flip the camera preview horizontally
  - Enable if you prefer the preview to match a mirror view
  - Does not affect tracking quality, only preview appearance

### Camera Tips
- Position the camera at eye level for best tracking
- Ensure good lighting on your face
- Minimize background movement and reflections
- USB 3.0 cameras generally provide better performance than USB 2.0

## Interface Settings

Interface settings control the application's appearance and behavior, found in **Settings > Interface**.

### Language
- **Application language**: Choose your preferred interface language
- **Available languages**: Depends on community translations
- **Restart required**: Language changes take effect after restarting LookPilot

## Keybinds Settings

Keybind settings configure global hotkeys, found in **Settings > Keybinds**.

### System Keybinds

#### Center Tracking
- **Default**: Ctrl+Space
- **Function**: Resets your current head position as the neutral center
- **Usage**: Press when you're in your normal sitting position to recalibrate

#### Toggle Tracking  
- **Default**: Not assigned
- **Function**: Starts or stops head tracking
- **Usage**: Quick way to enable/disable tracking without opening the interface



### Setting Keybinds

1. Click in the keybind field next to the action
2. Press the desired key combination
3. The keybind is automatically saved
4. To clear a keybind, press the clear button (if available) or delete key

### Keybind Guidelines

**Good keybind choices**:
- Combinations with Ctrl, Alt, or Shift (e.g., Ctrl+Space, Alt+F1)
- Function keys (F1-F12) if not used by games
- Numeric keypad keys (if available)

**Avoid**:
- Single letters or numbers that games might use
- Common shortcuts (Ctrl+C, Ctrl+V, Alt+Tab)
- Keys that games commonly bind to important functions

### Preset Keybinds

Individual preset keybinds are configured in the preset management window, not in the keybinds settings. See the [Presets](presets.md) guide for details.

## Performance Settings

Performance settings optimize LookPilot for your system, found in **Settings > Performance**.

### Tracking FPS Limit
- **Range**: 5-240 FPS
- **Default**: 20 FPS
- **Lower values**: Reduce CPU usage but may impact smoothness
- **Higher values**: Smoother tracking but use more system resources
- **Function**: Limits the processing frequency of the tracking pipeline
- **Note**: Actual tracking FPS is also limited by your camera's FPS capabilities

### GPU Acceleration
- **Use GPU acceleration**: Enable hardware acceleration for processing
- **Default**: Disabled (uses CPU processing)
- **Function**: Offloads parts of the tracking pipeline to the GPU
- **Benefits**: Can significantly improve performance on most systems
- **Note**: GPU acceleration requirements and performance vary by system

### Performance Tips
- Close unnecessary applications while using LookPilot
- Ensure adequate lighting to reduce processing requirements
- Use appropriate camera resolution for your system capabilities
- Monitor system temperature and performance during extended use

## Privacy Settings

Privacy settings control data collection, found in **Settings > Privacy**.

### Send Usage Statistics
- **Default**: Enabled
- **Function**: Helps improve the app by sending anonymous usage data

### Send Gaze Data  
- **Default**: Disabled
- **Function**: Helps improve eye tracking models by sending anonymized gaze data

For additional troubleshooting, see the [Troubleshooting](troubleshooting.md) guide. 