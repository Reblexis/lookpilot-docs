This guide explains the three main ways to connect LookPilot to any game on Windows. This is the recommended approach for any game which isn't described in detail in the [game setup guides](https://lookpilot.app/game-guides). Choose the method that works best for your game.

## Where to Find Protocol Settings

All protocol settings described below can be found at the bottom of the **General** tab in **Tracking settings**. Click the **Settings** button in the output pose visualization to open the Tracking settings window.

## 1. FreeTrack (emulating TrackIR)

This is the recommended method for most games.

### Setup
1. Set protocol to `freetrack`
2. Click **Start tracking**
3. Launch your game
4. Some games require enabling head tracking in their settings - look for keywords like "TrackIR", "head tracking", or "eye tracking"

### Status Indicator
The status indicator shows the connection state:
- **Grey**: Tracking stopped
- **Yellow**: Searching for connection
- **Green**: Connected to game

Hover over the indicator to see which game is connected and additional details.

## 2. Virtual Joystick

Use this method for games that don't support FreeTrack/TrackIR but support joystick input. Virtual joystick can also be used for controlling the game in other ways than just head tracking, such as steering with your head.

### Setup
1. Set protocol to `virtual joystick`
2. Click **Start tracking**
3. When starting tracking with virtual joystick for the first time, a driver installation window will appear
4. Complete the driver installation as prompted
5. If needed, restart the app after completing the installation if it still doesn't work
6. To configure axis mapping, go to **Tracking settings** and open each axis tab (Yaw, Pitch, Roll, X, Y, Z) - use the **Mapping** dropdown to select which joystick axis each head/eye tracking axis should control

### Status Indicator
The status indicator will be green if the virtual joystick is initialized and running.

## 3. Mouse Emulation

Use this method for games that only support mouse input for camera control. This requires routing through opentrack.

### Setup
1. Follow the [opentrack setup guide](../opentrack-setup/guide.md) to connect LookPilot to opentrack
2. In opentrack, set the output to mouse emulation
3. Configure mouse sensitivity in opentrack as needed

### Status Indicator
The status indicator will be green if data is being sent to opentrack (note: this doesn't confirm opentrack is receiving the data).

