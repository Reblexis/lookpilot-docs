## LookPilot Configuration
1. Set protocol to `opentrack`
2. Click **Start** to begin tracking

## Dying Light 2 Setup
Dying Light 2 Stay Human has no built-in head tracking. The free [Dying Light 2 head tracking mod](https://github.com/itsloopyo/dying-light-2-headtracking) by itsloopyo adds it: it reads opentrack data, which LookPilot sends with the `opentrack` protocol, and lets you look around while your mouse or controller keeps aiming.

### Install the Mod
1. Download the installer ZIP from the mod's [Releases page](https://github.com/itsloopyo/dying-light-2-headtracking/releases)
2. Right-click the ZIP, open **Properties**, tick **Unblock** and click **OK**, so Windows does not block the files inside
3. Extract it anywhere and double-click `install.cmd`

The mod needs Dying Light 2 v1.16 or later.

### In-Game
1. Keep LookPilot running with the `opentrack` protocol
2. Launch Dying Light 2. Your head now moves the view, so you can look around while you run

### Tips
- If your shots land off the crosshair, turn off the movement axes (X, Y and Z) in LookPilot's tracking settings and keep only the rotation axes
