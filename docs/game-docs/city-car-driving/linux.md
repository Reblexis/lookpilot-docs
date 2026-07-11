## LookPilot Configuration
1. Set protocol to `auto`
2. Launch the game
3. Select the City Car Driving Wine prefix in the `Game's Wine prefix` dropdown
4. Click **Start tracking** to begin tracking and wait for about 10 seconds
5. Click **Stop tracking**
6. Restart the game
7. Click **Start tracking**

### Fallback Option
If the above method doesn't work, try using the freetrack (Wine) protocol:

1. Set protocol to `freetrack (Wine)`
2. Select your Steam installation from the dropdown
3. Set Game to `City Car Driving` in the game dropdown
4. Launch the game from Steam
5. Click **Start tracking** to begin tracking and wait for about 10 seconds
6. Click **Stop tracking**
7. Restart the game
8. Click **Start tracking**

## City Car Driving Setup
Once LookPilot is running and configured, head tracking support may vary by version - check the game's Settings → Controls for TrackIR options, or you may need to edit the `game.ini` file and set `EnableTrackIr=true`.

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
