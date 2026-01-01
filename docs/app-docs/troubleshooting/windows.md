This guide covers common issues you might encounter with LookPilot and how to resolve them.

## Camera Issues

### Camera Not Detected

**Symptoms**: Camera doesn't appear in the dropdown list or shows "No camera"

**Solutions**:
1. **Refresh camera list**: Click the reload button (⟲) next to the camera dropdown
2. **Check camera connection**: Ensure your camera is properly connected via USB
3. **Close other applications**: Make sure no other software is using the camera (browsers, video chat apps, etc.)
4. **Try different USB ports**: Switch to a different USB port, preferably USB 3.0
5. **Restart LookPilot**: Close and reopen the application

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

---

If your issue isn't listed here, please contact support@lookpilot.app

