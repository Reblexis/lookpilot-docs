## LookPilot Configuration
1. Set protocol to `opentrack`
2. Click **Start** to begin tracking

## Cyberpunk 2077 Setup
Cyberpunk 2077 has no built-in head tracking. The free [Cyberpunk 2077 head tracking mod](https://github.com/itsloopyo/cyberpunk-2077-headtracking) by itsloopyo adds it: it reads opentrack data, which LookPilot sends with the `opentrack` protocol, and moves the view while your mouse or controller keeps aiming.

### Install the Mod
1. Download the installer ZIP from the mod's [Releases page](https://github.com/itsloopyo/cyberpunk-2077-headtracking/releases)
2. Right-click the ZIP, open **Properties**, tick **Unblock** and click **OK**, so Windows does not block the files inside
3. Extract it anywhere and double-click `install.cmd`. It finds Steam, GOG and Epic installs and also sets up the mod loaders it needs (Cyber Engine Tweaks, RED4ext and TweakXL, bundled in the ZIP)

If you install the mods by hand from Nexus Mods, install them in this order into the game folder: RED4ext, TweakXL, Cyber Engine Tweaks, then the head tracking mod. On Steam, also add the free **REDmod** DLC and turn on **Enable mods** in the game launcher.

### First Launch
1. Start the game once. Cyber Engine Tweaks asks you to bind a key for its overlay: pick any key you do not use
2. Load a save, then quit the game, so the mod loaders finish setting up
3. Start LookPilot with the `opentrack` protocol, then start the game again. Your head now moves the view

### Tips
- If your shots land off the crosshair while you look around, turn off the movement axes (X, Y and Z) in LookPilot's tracking settings and keep only the rotation axes. Your aim then stays aligned
- Lower **Movement sensitivity** instead if you want to keep a little leaning
