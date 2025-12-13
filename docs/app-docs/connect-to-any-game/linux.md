This guide explains the three main ways to connect LookPilot to any game on Linux. This is the recommended approach for any game which isn't described in detail in the [game setup guides](https://lookpilot.app/game-guides). Choose the method that works best for your game.

## Where to Find Protocol Settings

All protocol settings described below can be found at the top of the **General** tab in **Tracking settings**. Click the **Settings** button in the output pose visualization to open the Tracking settings window.

## 1. FreeTrack (emulating TrackIR)

This is the recommended method for most games.

### Setup with Auto Protocol (Recommended)
1. Set protocol to `auto`
2. Launch the game
3. Select the game's Wine prefix in `Game's Wine prefix` dropdown
4. Click **Start tracking** and wait for about 10 seconds
5. Click **Stop tracking**
6. Restart the game
7. Click **Start tracking**
8. Some games require enabling head tracking in their settings - look for keywords like "TrackIR", "head tracking", or "eye tracking"

### Fallback Option: Steam Games
If the auto method doesn't work and you're playing a Steam game:

1. Set protocol to `freetrack (Wine)`
2. Select your Steam installation from the dropdown
3. Set the game in the game dropdown
4. Launch the game from Steam
5. Click **Start tracking** and wait for about 10 seconds
6. Click **Stop tracking**
7. Restart the game
8. Click **Start tracking**
9. Some games require enabling head tracking in their settings - look for keywords like "TrackIR", "head tracking", or "eye tracking"

### Fallback Option: Non-Steam Games
If the auto method doesn't work and you're playing a non-Steam game:

1. Set protocol to `freetrack (Wine)`
2. Set launcher to `Other`
3. Select the game's Wine prefix path
4. Select the game's Wine executable path
5. Launch the game
6. Click **Start tracking** and wait for about 10 seconds
7. Click **Stop tracking**
8. Restart the game
9. Click **Start tracking**
10. Some games require enabling head tracking in their settings - look for keywords like "TrackIR", "head tracking", or "eye tracking"

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
3. To configure axis mapping, go to **Tracking settings** and open each axis tab (Yaw, Pitch, Roll, X, Y, Z) - use the **Mapping** dropdown to select which joystick axis each head/eye tracking axis should control

### Status Indicator
The status indicator will be green if the virtual joystick is initialized and running.

## 3. Mouse Emulation

Use this method for games that only support mouse input for camera control. This requires routing through OpenTrack.

### Setup
1. Follow the [OpenTrack setup guide](../opentrack-setup/guide.md) to connect LookPilot to OpenTrack
2. In OpenTrack, set the output to mouse emulation
3. Configure mouse sensitivity in OpenTrack as needed

### Status Indicator
The status indicator will be green if data is being sent to OpenTrack (note: this doesn't confirm OpenTrack is receiving the data).

