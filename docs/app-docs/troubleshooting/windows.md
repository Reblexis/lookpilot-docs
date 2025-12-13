# Troubleshooting

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
1. **Increase smoothness**: Raise smoothness values in head/eye tracking settings
2. **Improve lighting**: Add stable, consistent lighting to your face
3. **Reduce background movement**: Minimize movement behind you in the camera view
4. **Lower FPS**: Reduce tracking FPS in Settings > Performance if your system can't keep up
5. **Check camera mounting**: Ensure camera is mounted stably and not vibrating
6. **Close other applications**: Free up system resources by closing unnecessary programs

### Eye Tracking Not Working

**Symptoms**: Eye tracking settings don't affect camera movement

**Solutions**:
1. **Check eye tracking influence**: Ensure "Eye tracking influence" is greater than 0.0
2. **Verify eye tracking is enabled**: Check that Yaw and/or Pitch are enabled in eye tracking settings
3. **Improve eye visibility**: Ensure your eyes are clearly visible to the camera
4. **Adjust lighting**: Eye tracking requires good lighting on your face, especially around the eyes
5. **Check camera quality**: Eye tracking works better with higher quality cameras
6. **Remove obstructions**: Take off glasses if they're causing tracking issues

## Game Communication Issues

### Game Not Responding to Head Tracking

**Symptoms**: Tracking works in LookPilot but doesn't affect the game camera

**Solutions**:
1. **Verify game support**: Check that your game supports head tracking (FreeTrack, etc.)
2. **Check protocol selection**: Ensure the correct protocol is selected for your game
3. **Enable in game**: Look for head tracking options in the game's settings menu
4. **Restart game**: Close and reopen the game after starting LookPilot tracking
5. **Try different protocol**: If available, test with a different communication protocol
6. **Run as administrator**: Try running both LookPilot and the game as administrator
7. **Check Windows firewall**: Ensure firewall isn't blocking communication

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
4. **Disable GPU acceleration**: Try disabling GPU acceleration if it's causing issues
5. **Check camera drivers**: Update to latest camera drivers

---

If your issue isn't listed here, please contact support@lookpilot.app

