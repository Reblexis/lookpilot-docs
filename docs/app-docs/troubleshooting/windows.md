This guide covers common issues you might encounter with LookPilot and how to resolve them.

## Find your issue

| Symptom | Where to look |
|---|---|
| App won't start / exits immediately | [App Startup Issues](#app-startup-issues) |
| Camera missing from the dropdown | [Camera Not Detected](#camera-not-detected) |
| Camera FPS lower than expected | [Camera FPS Lower Than Expected](#camera-fps-lower-than-expected) |
| Tracking shaky or drifting | [Tracking is Jittery](#tracking-is-jittery) |
| Status stays yellow / game ignores tracking | [Game Not Responding to Head Tracking](#game-not-responding-to-head-tracking) |
| Mouse camera stuck in ETS2/ATS | the game's setup guide, "Mouse-look stops working" section |
| No internet / offline play | [Offline Use](#offline-use) |
| Something broke after an update | [Switching to an Older Version](#switching-to-an-older-version) |
| Tracking keeps running after closing the app | [Tracking Continues After Closing](#tracking-continues-after-closing-the-app) |


## Camera Issues

### Camera Not Detected

**Symptoms**: Camera doesn't appear in the dropdown list or shows "No camera"

**Solutions**:
1. **Refresh camera list**: Click the reload button (⟲) next to the camera dropdown
2. **Check camera connection**: Ensure your camera is properly connected via USB
3. **Close other applications**: Make sure no other software is using the camera (browsers, video chat apps, etc.)
4. **Try different USB ports**: Switch to a different USB port, preferably USB 3.0
5. **Restart LookPilot**: Close and reopen the application
6. **PS3 Eye**: LookPilot sees any camera exposed as a Media Foundation (MSMF) or DirectShow device. The PS3 Eye needs a DirectShow driver first - install the PS3EyeDirectShow driver (the .msi from github.com/jkevin/PS3EyeDirectShow/releases); the stock/CL-Eye/libusbK drivers are not visible to LookPilot. If the feed is black after installing, enable **Use DirectShow** in Settings > Camera.

### Camera FPS Lower Than Expected

**Symptoms**: A 60-120 fps camera runs at 30 fps or less in LookPilot

**Solutions**:
1. **Pick a lower resolution**: Each resolution entry lists its maximum framerate and LookPilot always uses the highest framerate available for the selected resolution - high-fps modes usually exist only at 720p and below
2. **Toggle capture backends**: Flip **Use MJPEG** off/on, and try **Use DirectShow** (Settings > Camera) - missing fps modes often appear after switching backends
3. **Add light**: In dim rooms cameras silently raise exposure and halve their framerate; light your face from the front or disable **Auto exposure**
4. **Plug in directly**: Avoid USB hubs; close other apps using the camera
5. **Guidance**: 30 fps is the workable minimum, 60 fps the sweet spot; above 60 the gains are minimal

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
1. **Increase smoothness**: Raise smoothness values in tracking settings
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
7. **Run as administrator**: Try running both LookPilot and the game as administrator
8. **Check Windows firewall**: Ensure firewall isn't blocking communication
9. **Uninstall or reconfigure competing tracking software**: TrackIR software, Beam Eye Tracker, Tobii, or AITrack can hold or redirect the TrackIR interface even when not running. In Beam Eye Tracker specifically, set Immersive Camera to the "using OpenTrack application" mode (its "Direct Game Camera Control" mode blocks LookPilot's connection)

### UDP Protocol Issues

**Symptoms**: UDP communication fails to connect

**Solutions**:
1. **Verify IP and port**: Double-check the IP address and port number configuration
2. **Check target application**: Ensure the receiving application is running and listening
3. **Test with localhost**: Try using 127.0.0.1 for local testing
4. **Check firewall**: Verify firewall isn't blocking UDP traffic on the specified port
5. **Try different port**: Test with a different port number if the current one is in use

## Performance Issues

### High CPU Usage

**Symptoms**: LookPilot uses excessive CPU resources

**Solutions**:
1. **Lower FPS limit**: Reduce tracking FPS in Settings > Performance
2. **Reduce camera resolution**: Use lower resolution in Settings > Camera
3. **Close other applications**: Free up CPU resources
4. **Check camera drivers**: Update to latest camera drivers

## App Startup Issues

### App won't start / flashes in Task Manager and exits

**Solutions**:
1. **Steam must be running**: The Steam build requires the Steam client running and logged in - restart Steam and try again
2. **JSONDecodeError after a crash or power loss**: A settings file got corrupted. Delete `%LOCALAPPDATA%\Lookpilot\settings.json` (settings reset; presets are separate files in the presets folder). Reinstalling alone does not fix this, because that folder is preserved across reinstalls

### App freezes when selecting a camera / after an update

**Solutions**:
1. Switch to another camera and toggle **Use MJPEG** / **Use GStreamer** / **Use DirectShow** in Settings > Camera
2. If the UI is unreachable, set `"camera_use_dshow": true` directly in `%LOCALAPPDATA%\Lookpilot\settings.json`
3. If problems started after an update, do a clean reinstall: uninstall, delete `%LOCALAPPDATA%\Lookpilot`, reinstall
4. Send an in-app bug report from the Feedback tab so logs reach the developer; logs live in `%LOCALAPPDATA%\Lookpilot\logs`

## Offline Use

LookPilot currently needs an internet connection at startup (known issue). Workarounds:
1. **Start online, then disconnect**: Start LookPilot while online and load your preset - tracking keeps working after you go offline
2. **ISP blocking**: If community presets or bug reports never load even though your connection works, your ISP may be blocking our servers - testing over a VPN confirms this

## Switching to an Older Version

If something broke right after an update, rolling back is a quick way to confirm it and keep playing:
- **Steam**: right-click LookPilot > Properties > Betas, and pick an older version from the dropdown
- **Standalone**: all releases are available at github.com/Reblexis/lookpilot-downloads/releases

If an older version fixes your problem, please report the bug (in-app Feedback tab) so it gets fixed in the current version.

## Tracking Continues After Closing the App

1. LookPilot minimizes to the system tray - quit it from the tray icon
2. To stop it launching with Windows, disable auto startup in Settings > Interface
3. If you uninstalled but tracking persists, check that both the **Demo** and the full version are uninstalled

## Known Issues

- **Game stays "running" in Steam after you exit it**: press **Stop tracking** in LookPilot and the game process will finish closing. You do not need to quit LookPilot
- **Can't find LookPilot in your Steam library?** Steam's library filter shows Games only by default - open the filter (funnel icon) and tick "Software"

---

If your issue isn't listed here, please contact support@lookpilot.app

