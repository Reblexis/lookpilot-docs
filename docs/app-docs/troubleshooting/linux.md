This guide covers common issues you might encounter with LookPilot and how to resolve them.

## Find your issue

| Symptom | Where to look |
|---|---|
| App won't launch at all | [App Startup Issues](#app-startup-issues) |
| Camera missing from the dropdown | [Camera Not Detected](#camera-not-detected) |
| Tracking shaky or drifting | [Tracking is Jittery](#tracking-is-jittery) |
| Status stays yellow / game ignores tracking | [Game Not Responding to Head Tracking](#game-not-responding-to-head-tracking) |
| Game never connects under Proton | [Proton Issues](#proton-issues) |
| Keybinds do nothing (Wayland) | [Keybind Issues](#keybind-issues) |
| No internet / offline play | [Offline Use](#offline-use) |
| Something broke after an update | [Switching to an Older Version](#switching-to-an-older-version) |


## Camera Issues

### Camera Not Detected

**Symptoms**: Camera doesn't appear in the dropdown list or shows "No camera"

**Solutions**:
1. **Refresh camera list**: Click the reload button (⟲) next to the camera dropdown
2. **Check camera connection**: Ensure your camera is properly connected via USB
3. **Close other applications**: Make sure no other software is using the camera (browsers, video chat apps, etc.)
4. **Try different USB ports**: Switch to a different USB port, preferably USB 3.0
5. **Restart LookPilot**: Close and reopen the application
6. **Check camera permissions**: Ensure your user has access to `/dev/video*` devices
7. **Install v4l-utils**: `sudo apt install v4l-utils` then check cameras with `v4l2-ctl --list-devices`
8. **Use .deb Steam version**: Make sure to use .deb version of Steam (Flatpak, Snap or any other containerized installations aren't supported) - https://store.steampowered.com/about/

## Tracking Issues

### Head Tracking Not Responsive

**Symptoms**: Moving your head doesn't affect the 3D visualization or game camera

**Solutions**:
1. **Check tracking status**: Ensure "Start tracking" button shows "Stop tracking" (tracking is active)
2. **Verify camera selection**: Make sure a camera is selected in Settings > Camera
3. **Check lighting**: Ensure your face is well-lit with even lighting
4. **Verify head position**: Sit in the camera's field of view with your face clearly visible
5. **Adjust deadzone**: Lower the deadzone value in head tracking settings
6. **Reset tracking**: Press the "Center" button to reset the neutral position
7. **Check enabled axes**: Verify the desired axes (Yaw, Pitch, etc.) are enabled

### Tracking is Jittery

**Symptoms**: Camera movement is shaky or jumps around erratically

**Solutions**:
1. **Increase smoothness**: Raise smoothness values in head/eye tracking settings
2. **Increase deadzone**: Deadzone prevents tiny movements (sometimes noise) from affecting the tracking.
3. **Increase confidence threshold**: Can be also found in tracking settings. Increasing will cause less certain tracking predictions to be ignored.
4. **Improve lighting**: Add stable, consistent lighting to your face
5. **Reduce background movement**: Minimize movement behind you in the camera view
6. **Lower FPS**: Reduce tracking FPS in Settings > Performance if your system can't keep up
7. **Check camera mounting**: Ensure camera is mounted stably and not vibrating
8. **Close other applications**: Free up system resources by closing unnecessary programs


## Game Communication Issues

### Game Not Responding to Head Tracking

**Symptoms**: Tracking works in LookPilot but doesn't affect the game camera

**Solutions**:
1. **Look for a game guide**: Most popular games have a corresponding guide here: [game setup guides](https://lookpilot.app/game-guides). 
2. **Verify TrackIR support** If trying the *freetrack* protocol, verify that given game support *TrackIR* tracking online or in the game documentation.
3. **Check protocol selection**: Ensure the correct protocol is selected for your game
4. **Enable in game**: Look for head tracking options in the game's settings menu
5. **Restart game**: Close and reopen the game after starting LookPilot tracking
6. **Try different protocol**: If available, test with a different communication protocol
7. **Check Proton setup**: For Proton games, verify Steam installation and game selection are correct
8. **Verify game launched**: Ensure the target game has been launched at least once through Steam
9. **Check Steam running**: Make sure Steam is running and logged in

### UDP Protocol Issues

**Symptoms**: UDP communication fails to connect

**Solutions**:
1. **Verify IP and port**: Double-check the IP address and port number configuration
2. **Check target application**: Ensure the receiving application is running and listening
3. **Test with localhost**: Try using 127.0.0.1 for local testing
4. **Check firewall**: Verify firewall isn't blocking UDP traffic on the specified port
5. **Try different port**: Test with a different port number if the current one is in use

### Proton Issues

**Symptoms**: Proton protocols fail to start or games don't detect tracking

**Solutions**:
1. **Launch game first**: Start the target game through Steam at least once to create Proton prefix
2. **Check Steam path**: Verify LookPilot has detected the correct Steam installation path
3. **Select correct game**: Ensure you've selected the right game from the dropdown
4. **Steam running**: Make sure Steam is running and you're logged in
5. **Verify game in library**: Confirm the game is actually in your Steam library
6. **Browse for Steam**: Manually browse to your Steam installation if auto-detection fails
7. **Force a mainline Proton version**: If `auto` / `freetrack (Wine)` never connect, force a specific official Proton version on the game (Steam -> Properties -> Compatibility). Proton 10 is the most commonly confirmed by users; Proton-GE has also fixed connection failures where Proton Experimental or distro-specific builds (e.g. CachyOS Proton) failed
8. **Native Linux game builds**: most native builds have no head-tracking interface at all (X4: Foundations is a notable exception, via UDP). If a game ships both native and Windows builds, force Proton on the game and follow the Wine/Proton setup

## Keybind Issues

### Keybinds Not Working

**Symptoms**: Preset keybinds or system keybinds don't respond when pressed

**Solutions**:
1. **Wayland**: Update LookPilot first - recent versions support global hotkeys on Wayland. The robust route on any Wayland compositor is the local control API: bind your compositor's own shortcuts to `lookpilotctl center` / `toggle` / `pause` (see the Control API guide)
2. **Check other applications**: Verify another application isn't capturing the key combination
3. **Try different keys**: Use a different key combination
4. **Restart LookPilot**: Close and reopen the application to re-register keybinds
5. **Verify keybind is set**: Check that the keybind is actually configured in the preset options

## Performance Issues

### High CPU Usage

**Symptoms**: LookPilot uses excessive CPU resources

**Solutions**:
1. **Lower FPS limit**: Reduce tracking FPS in Settings > Performance
2. **Reduce camera resolution**: Use lower resolution in Settings > Camera
3. **Close other applications**: Free up CPU resources
4. **Check camera drivers**: Update to latest camera drivers

## App Startup Issues

### LookPilot won't launch

**Solutions**:
1. **Run it natively**: Never force Proton/Wine on LookPilot itself - it is a native Linux app
2. **Force the sniper runtime**: If the default launch fails, set the Steam compatibility tool for LookPilot to "Steam Linux Runtime 3.0 (sniper)" and let it update
3. **Check the logs**: They live in `~/.local/share/LookPilot/logs` - zip and send them to support@lookpilot.app
4. **Clean reset (last resort)**: Delete the installed files (Steam -> Browse local files) plus `~/.local/share/LookPilot`, then reinstall. This resets local presets and settings
5. **Standalone fallback**: The standalone build from lookpilot.app/downloads works without the Steam runtime
6. **AppImage needs FUSE2**: The standalone AppImage currently requires FUSE2, which some distros (Fedora Atomic, CachyOS) no longer ship - install libfuse2 manually or use the Steam build

## Offline Use

LookPilot currently needs an internet connection at startup (known issue). Workarounds:
1. **Start online, then disconnect**: Start LookPilot while online and load your preset - tracking keeps working after you go offline
2. **Launch the binary directly**: `.../steamapps/common/LookPilot/main.dist/LookPilot` starts without Steam and offers a guest login (presets cannot be loaded that way)
3. **ISP blocking**: If community presets or bug reports never load even though your connection works, your ISP may be blocking our servers - testing over a VPN confirms this

## Switching to an Older Version

If something broke right after an update, rolling back is a quick way to confirm it and keep playing:
- **Steam**: right-click LookPilot > Properties > Betas, and pick an older version from the dropdown
- **Standalone**: all releases are available at github.com/Reblexis/lookpilot-downloads/releases

If an older version fixes your problem, please report the bug (in-app Feedback tab) so it gets fixed in the current version.

## Known Issues

- **Game stays "running" in Steam after you exit it**: press **Stop tracking** in LookPilot and the game process will finish closing. You do not need to quit LookPilot
- **DCS hangs on exit while tracking runs**: stop tracking before quitting DCS (see the DCS World guide)

---

If your issue isn't listed here, please contact support@lookpilot.app

