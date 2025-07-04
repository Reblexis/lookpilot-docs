# Getting Started

Welcome to LookPilot! This guide will help you get head tracking working with your first game in just a few minutes.

## What is LookPilot?

LookPilot is a head and eye tracking application that uses your webcam to track your head movement and translate it into camera control for games. This creates a more immersive gaming experience where looking around naturally moves your in-game camera view.

## Quick Setup

### Step 1: First Launch

When you first start LookPilot, you'll see the main interface with several tabs:
- **Gaming**: Configure tracking and communication with games
- **Settings**: Camera, performance, privacy, and interface options  
- **Feedback**: Send feedback to the developers
- **About**: Application information

On first launch, you may be prompted to allow anonymous usage data collection to help improve the app. This is optional and can be changed later in Settings > Privacy.

### Step 2: Camera Setup

1. Go to the **Settings** tab, then **Camera**
2. Click the dropdown next to "Select camera" and choose your webcam
3. If you don't see your camera, click the reload button (⟲) next to the dropdown
4. Position your camera so you can see yourself clearly in the preview
5. Adjust the **Resolution** if needed (1280x720 is recommended for most setups)
6. Optionally enable **Mirror camera** if you prefer the preview flipped

> **Note**: On Linux, some cameras may not appear due to format compatibility. Try different cameras or check that your camera supports standard formats.

### Step 3: Protocol Selection

Go back to the **Gaming** tab and configure communication with your game:

#### Windows Users
1. In the **Protocol** dropdown, select:
   - **FreeTrack**: For most games (recommended)
   - **SimConnect**: For Microsoft Flight Simulator (only if FreeTrack doesn't work)
   - **UDP**: For custom applications
   - **OpenTrack**: For OpenTrack compatibility

#### Linux Users
1. In the **Protocol** dropdown, select:
   - **FreeTrack (Proton)**: For Windows games running through Steam Proton (recommended)
   - **SimConnect (Proton)**: For Microsoft Flight Simulator through Proton (only if FreeTrack doesn't work)
   - **UDP**: For native Linux applications
   - **OpenTrack**: For OpenTrack compatibility

For Proton protocols, you'll need to configure your Steam installation and select the game you want to play.

### Step 4: Basic Tracking Configuration

1. Click **Head tracking settings** to open the head tracking window
2. Make sure the axes you want to use are enabled:
   - **Yaw**: Left/right head movement (usually enabled)
   - **Pitch**: Up/down head movement (usually enabled)  
   - **Roll**: Head tilting (optional)
   - **X, Y, Z**: Physical head movement (optional)
3. Adjust **Smoothness** (0.3 is a good starting point)
4. Adjust **Deadzone** (0.1 is a good starting point)
5. Click **OK** to close the window

### Step 5: Start Tracking

1. In the Gaming tab, click **Start tracking**
2. The button will change to **Stop tracking** when active
3. You should see the 3D head visualization moving as you move your head
4. If no camera is selected, you'll be prompted to select one

### Step 6: Configure in Game

1. Launch your game
2. Check our [game guides](https://lookpilot.app/game-guides) to find your specific game setup guide
3. If no guide exists for your game, look in the game's settings for:
   - **FreeTrack** support
   - **TrackIR** support 
   - **Head tracking** options
4. Configure the game to accept head tracking input:
   - For **FreeTrack**: Enable FreeTrack or head tracking in game settings
   - For **SimConnect**: No additional setup needed in Microsoft Flight Simulator
   - For **OpenTrack**: Configure OpenTrack to receive UDP input on port 4242
5. Test the head tracking by moving your head - you should see the camera move in game

### Step 7: Center Your View

- Press **Center** in the Gaming tab (or use the keybind Ctrl+Space) to set your current head position as the neutral/center position
- Do this while sitting in your normal gaming position

## Next Steps

Once basic tracking is working:

1. **Fine-tune tracking settings**: Adjust smoothness, deadzone, and axis sensitivity in the head tracking settings
2. **Configure mapping curves**: Click "Mapping" in head tracking settings to customize response curves
3. **Set up eye tracking**: Configure eye tracking influence if you want combined head+eye tracking
4. **Create custom presets**: Save different configurations for different games
5. **Check game-specific guides**: Visit the game setup guides for detailed game-specific instructions

## Troubleshooting

**Camera not detected?**
- Try clicking the reload button (⟲) next to the camera dropdown
- Check that your camera isn't being used by another application
- On Linux, ensure your camera supports standard video formats

**Tracking not working in game?**
- Make sure you clicked "Start tracking" in the Gaming tab
- Verify the correct protocol is selected for your game
- Check that the game supports head tracking and has it enabled
- For Proton users, ensure Steam and the target game are properly configured

**Tracking is jittery?**
- Increase the Smoothness value in head tracking settings
- Ensure good lighting on your face
- Try adjusting camera resolution or position

**Tracking drifts over time?**
- Increase the Deadzone value in head tracking settings
- Press Center to reset the neutral position
- Ensure stable lighting conditions

For more detailed troubleshooting, see the [Troubleshooting](https://lookpilot.app/guides/app-troubleshooting.html) guide. 