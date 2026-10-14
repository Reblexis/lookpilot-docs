## LookPilot Configuration
1. Set protocol to `opentrack`
2. Click **Start** to begin tracking

## Assetto Corsa Rally Setup
Assetto Corsa Rally has no built-in head tracking. The free [Assetto Corsa Rally head tracking mod](https://github.com/itsloopyo/assetto-corsa-rally-headtracking) by itsloopyo adds it: it reads opentrack data, which LookPilot sends with the `opentrack` protocol.

### Install the Mod
1. Download the installer ZIP from the mod's [Releases page](https://github.com/itsloopyo/assetto-corsa-rally-headtracking/releases)
2. Right-click the ZIP, open **Properties**, tick **Unblock** and click **OK**, so Windows does not block the files inside
3. Extract it anywhere and double-click `install.cmd`. It finds the game and puts the files next to `acr.exe`

To install by hand instead, copy two files from the ZIP into `<game folder>\acr\Binaries\Win64\` (the folder that holds `acr.exe`, open it from Steam with **Manage** > **Browse local files**):
- `vendor\ultimate-asi-loader\dinput8.dll`
- `plugins\AssettoCorsaRallyHeadTracking.asi`

### In-Game
1. Keep LookPilot running with the `opentrack` protocol
2. Launch Assetto Corsa Rally and take a car out. Your head now moves the cockpit view
3. Adjust the seat position and field of view so the view feels natural

### Tips
- Raise **Rotation sensitivity** if you want to look further into corners with less head movement
- Add a little **Smoothness** if the view shakes in low light
