# Using the LookPilot App

LookPilot is a head and eye tracking application that allows you to control your view in games and simulators using natural head movements and eye gaze.

## Main Interface

The LookPilot app is organized into several tabs:

### Gaming Tab
The primary interface for tracking control:
- **Start/Stop Tracking**: Large button to begin or end head tracking
- **Preset Selection**: Switch between saved configurations
- **Protocol Settings**: Choose how to communicate with games (FreeTrack, UDP, etc.)
- **Quick Settings**: Eye tracking influence and TrueView toggle
- **Advanced Settings**: Access detailed head and eye tracking configuration

### Settings Tab
Application configuration organized into subtabs:
- **Interface**: Language selection
- **Camera**: Select and configure your camera
- **Performance**: Adjust tracking FPS and GPU acceleration
- **Keybinds**: Set up keyboard shortcuts for centering and toggling tracking
- **Privacy**: Control data collection preferences

## Key Concepts

### Head Tracking
Monitors head rotation (yaw, pitch, roll) and translation (X, Y, Z movement) to control your in-game view. Works with most games that support head tracking.

### Eye Tracking
Tracks your eye rotation to add subtle view adjustments on top of head tracking. Works automatically without calibration.

### Presets
Saved configurations that store all your tracking and communication settings. Switch between presets for different games or use cases.

### Protocols
Different methods to send tracking data to games:
- **FreeTrack**: Most common, works with many games
- **SimConnect**: Specifically for Microsoft Flight Simulator
- **UDP**: For custom applications or OpenTrack
- **OpenTrack**: Integration with the OpenTrack ecosystem

## Getting Started Workflow

1. **Camera Setup**: Select your camera in Settings > Camera
2. **Protocol Selection**: Choose the appropriate protocol for your game
3. **Basic Configuration**: Adjust tracking settings as needed
4. **Start Tracking**: Click the tracking button and test in your game
5. **Fine-tune**: Create presets and adjust settings for optimal experience

## Quick Tips

- Start with the Default preset and modify as needed
- Use FreeTrack protocol for most games (SimConnect only if FreeTrack doesn't work)
- Test tracking with the 3D visualization before launching games
- Create game-specific presets once you find settings that work well
- Use keybinds for quick centering and tracking control while gaming

For detailed setup instructions, see the [Getting Started](../getting-started/guide.md) guide.
