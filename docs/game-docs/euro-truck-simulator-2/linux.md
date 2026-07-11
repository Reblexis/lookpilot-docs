## LookPilot Configuration
1. Set protocol to `auto`
2. Launch the game
3. Select the `Euro Truck Simulator 2`'s Wine prefix in `Game's Wine prefix` dropdown
4. Click **Start tracking** to begin tracking and wait for about 10 seconds
5. Click **Stop tracking**
6. Restart the game
7. Click **Start tracking**

### Fallback Option
If the above method doesn't work, try using the freetrack (Wine) protocol:

1. Set protocol to `freetrack (Wine)`
2. Select your Steam installation from the dropdown
3. Set Game to `Euro Truck Simulator 2` in the game dropdown
4. Launch the game from Steam
5. Click **Start tracking** to begin tracking and wait for about 10 seconds
6. Click **Stop tracking**
7. Restart the game
8. Click **Start tracking**

## Euro Truck Simulator 2 Setup
1. If launching the game from Steam, make sure to force the use of specific compatibility tool (Proton)

## Common issues
### Game not reacting to tracking input even though the tracking is running
1. Make sure to have the line "uset g_trackir" set to "1" (including the quotes) in *~/.steam/debian-installation/steamapps/compatdata/227300/pfx/drive_c/users/steamuser/Documents/Euro Truck Simulator 2/config.cfg*.
2. Bind a key in Keys and Buttons for "Enable Head Tracking" and try pressing the key in-game.

### Game not found in the Wine prefix list
- If you run the **native Linux** build of ETS2, protocol detection differs from Proton: force the Proton version of ETS2 in Steam (Properties -> Compatibility) - several users only got tracking working through Proton.
- After launching the game, click the refresh next to the prefix dropdown; prefixes appear only once the game process is running.

### Mouse-look stops working after closing LookPilot
A known issue in SCS titles: if the in-game camera stops following your mouse after you exit LookPilot, restart the game - mouse-look returns. Keeping LookPilot running for the whole session avoids it entirely.
### Game shows a yellow status / never connects
1. Start LookPilot and tracking **before** launching the game, or restart the game after tracking is running - SCS titles only look for the tracker at startup.
2. Verify `uset g_trackir "1"` (with quotes) in the game's *config.cfg* (see path above) - game updates occasionally reset it.
3. In-game, bind a key to **Enable Head Tracking** (Keys & Buttons) and press it once while driving.

### Hotkeys do nothing on Wayland (Hyprland, KDE Wayland, GNOME)
Wayland compositors do not deliver global hotkeys to apps. Use LookPilot's local control API instead: bind your compositor's own shortcuts to call `lookpilotctl center` / `toggle` / `pause` (the helper script ships with the app; the API listens on 127.0.0.1 while LookPilot runs). This gives you recenter/pause from any keybind or Stream Deck.

## Reducing jitter and shake
Shaky or twitchy tracking is the most-reported issue across all games, and it almost always traces to the camera picture, not the game:

1. **Light your face from the front.** Backlighting (a window or lamp behind you) starves the tracker of facial detail and produces micro-jumps.
2. **Check your camera's real frame rate.** Many webcams silently drop to 10-15 fps in low light even when set to 30. In LookPilot, watch the *Tracker fps* readout while tracking - if it is far below your camera's rating, more light usually fixes it.
3. **Raise smoothing.** In *Settings -> Tracking*, increase smoothing/filtering until stillness feels stable, then walk it back until the response feels quick enough.
4. **Flatten the curve center.** Give the response curves a gentle plateau around the center so breathing and small posture shifts do not move the camera.

## Recentering
Press **Alt+C** (default) to recenter tracking on your current head position at any time - do it once seated in your normal driving position, looking at the center of your screen. If you find yourself recentering constantly, move the webcam so it faces you head-on (an off-axis camera makes turned positions read as drift) and recenter while looking at the horizon in-game, not at the camera.
