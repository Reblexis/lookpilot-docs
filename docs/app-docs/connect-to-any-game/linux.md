This guide explains the three main ways to connect LookPilot to any game on Linux. This is the recommended approach for any game which isn't described in detail in the [game setup guides](https://lookpilot.app/game-guides). Choose the method that works best for your game.

## Where to Find Protocol Settings

All protocol settings described below can be found at the bottom of the **General** tab in **Tracking settings**. Click the **Settings** button in the output pose visualization to open the Tracking settings window.

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

The stop-tracking/restart-game cycle is normally needed only the **first time per game** - afterwards tracking connects directly. Note the indicator can already show green before the restart even though the game has not yet loaded the tracker.

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
3. Select the game's Wine prefix path:
   - **Default Wine**: `~/.wine`
   - **Lutris**: Right-click the game → Configure → Runner options → Wine prefix field, or typically `~/.local/share/lutris/runners/wine/<game-name>`
   - **Heroic Games Launcher**: Check game settings → Wine/Proton prefix, typically `~/Games/Heroic/Prefixes/<game-name>`
     
     > **Important for Heroic Launcher users:** UMU (Unified Launcher for Windows Games on Linux) is a compatibility tool that can interfere with LookPilot's connection. Before launching your game, open the game's settings in Heroic, go to the **Advanced** tab, and **disable UMU**. If you've previously launched the game with UMU enabled, you'll need to delete the game's prefix folder (either manually from the file system or by resetting it through Heroic's interface) and let it recreate on the next launch.
     
   - **Bottles**: Bottles Manager → Select bottle → Bottle path shown in details
   - **Custom installations**: Look for a directory containing `drive_c` folder
4. Select the game's Wine executable path:
   - **System Wine**: `/usr/bin/wine`
   - **Steam (Proton)**: `~/.steam/steam/steamapps/common/Proton <version>/files/bin/wine`
   - **Lutris**: `~/.local/share/lutris/runners/wine/<version>/bin/wine`
   - **Heroic Launcher**: 
     - Wine: `~/.config/heroic/tools/wine/<version>/bin/wine`
     - Proton: `~/.config/heroic/tools/proton/<version>/bin/wine`
   - **Bottles**: `~/.local/share/bottles/runners/<version>/bin/wine`
   - **Custom (Proton-GE)**: `~/.steam/root/compatibilitytools.d/<version>/files/bin/wine`

   > **Tip:** If you're unsure which version you're using, check the "Runner" or "Compatibility" settings in your launcher. The path usually ends with `/bin/wine`.
5. Launch the game
6. Click **Start tracking** and wait for about 10 seconds
7. Click **Stop tracking**
8. Restart the game
9. Click **Start tracking**
10. Some games require enabling head tracking in their settings - look for keywords like "TrackIR", "head tracking", or "eye tracking"

### Fallback Option: Steam Games in Nonstandard Locations
If your Steam game doesn't appear in the game dropdown (e.g., installed in a custom Steam library folder), you can use the `Other` launcher with manual paths:

1. Set protocol to `freetrack (Wine)`
2. Set launcher to `Other`
3. Select the game's Wine prefix path — for Steam/Proton games this is the `compatdata` prefix:
   - **Default Steam**: `~/.steam/steam/steamapps/compatdata/<appid>/pfx`
   - **Custom library folder**: `<library_path>/steamapps/compatdata/<appid>/pfx`
   
   > **Tip:** To find your game's app ID, open its Steam store page — the ID is in the URL: `store.steampowered.com/app/<appid>/...`

4. Select the game's Wine executable path (the Proton binary):
   - **Default Steam**: `~/.steam/steam/steamapps/common/Proton <version>/files/bin/wine`
   - **Custom library folder**: `<library_path>/steamapps/common/Proton <version>/files/bin/wine`
   - **Proton-GE**: `~/.steam/root/compatibilitytools.d/GE-Proton<version>/files/bin/wine`

   > **Tip:** Check which Proton version your game uses in Steam → Right-click game → Properties → Compatibility.

5. Launch the game from Steam
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

### First-time permissions (/dev/uinput)
Creating a virtual joystick needs write access to `/dev/uinput`. On first use LookPilot shows an error with a `setup_joystick_permissions.sh` command to run:

- For AppImage installs, the `/tmp/.mount_...` path in that command changes on every launch - copy the command fresh from the current error message **while LookPilot is still open**, or extract the AppImage with `--appimage-extract` and run the script from `squashfs-root`.
- If the script route keeps failing, add yourself to the input group manually: `sudo usermod -aG input $USER`, then **reboot** (logging out is not always enough).

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

## Troubleshooting

### Heroic Games Launcher: UMU Compatibility Issues

If you're using Heroic Games Launcher and LookPilot isn't connecting to your game, UMU (Unified Launcher for Windows Games on Linux) may be interfering with the connection.

**Solution:**
1. Open your game's settings in Heroic Games Launcher
2. Navigate to the **Advanced** tab
3. **Disable UMU**
4. If you've previously launched the game with UMU enabled, delete the game's prefix folder:
   - **Manual deletion**: Remove the prefix folder from `~/Games/Heroic/Prefixes/<game-name>`
   - **Reset through Heroic**: Use Heroic's interface to reset/delete the prefix
5. Launch the game again - the prefix will be recreated without UMU interference

### Use Native (Non-Containerized) LaunchersContainerized versions of game launchers (Flatpak, Snap, etc.) can cause issues with LookPilot's connection due to sandboxing. This applies to Steam, Heroic Games Launcher, Bottles, and other launchers. If you're experiencing problems, make sure you're using the native versions installed via `.deb` packages or your distribution's package manager. For Steam specifically, download the native version from [https://store.steampowered.com/about/](https://store.steampowered.com/about/).

### CachyOS Proton builds fail to connect
CachyOS-specific Proton builds currently have connection issues (status stuck on "Connecting", or the game missing from the freetrack (Wine) game dropdown). Force an official Proton version or Proton-GE on the game (Steam -> Properties -> Compatibility) until this is fixed.
