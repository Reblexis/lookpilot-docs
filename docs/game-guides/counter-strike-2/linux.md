# Setting up LookPilot with Counter-Strike 2 (Linux)

> **🐧 Linux Note:** This guide is specifically for Linux systems. CS2 runs through Steam with Proton compatibility layer.

## LookPilot Configuration

1. Launch LookPilot from terminal:
   ```bash
   lookpilot
   ```
2. Ensure your head tracking device is connected and detected
3. In the **Output** tab, select `Mouse emulation` protocol
4. Configure mouse settings:
   - **Mouse sensitivity:** Start with 50-100
   - **Update rate:** 60-120 Hz
5. Click **Start** to begin tracking
6. Go to the **Mapping** tab to adjust curves for competitive gaming

## Counter-Strike 2 Setup

1. Launch LookPilot before starting CS2
2. Start Counter-Strike 2 through Steam:
   ```bash
   steam steam://rungameid/730
   ```
3. In CS2, go to **Settings** → **Mouse/Keyboard**
4. Enable **Raw Input** for mouse
5. Adjust mouse sensitivity to work with head tracking
6. Test head tracking in a practice match

> **🎯 Gaming Tip:** Use subtle head tracking for competitive advantage without affecting aim precision.

## Troubleshooting

### No tracking detected
- Ensure LookPilot is started before CS2
- Check that mouse emulation protocol is selected
- Verify mouse emulation is working:
  ```bash
  xinput list
  ```
- Test mouse movement outside the game first

### Laggy input
- Increase update rate in LookPilot Output settings
- Close unnecessary applications
- Check system performance:
  ```bash
  htop
  ```
- Lower graphics settings in CS2 if needed

### Permission errors
- Add your user to the input group:
  ```bash
  sudo usermod -a -G input $USER
  ```
- Log out and back in for changes to take effect
- Check device permissions:
  ```bash
  ls -la /dev/input/
  ```

### Tracking affects aim too much
- Reduce sensitivity in LookPilot mapping
- Use smaller curves for subtle movement
- Increase deadzone for precise aiming
- Consider disabling certain axes (like roll)

---

*Part of the [LookPilot Guides](https://github.com/Reblexis/lookpilot-guides) community project.* 