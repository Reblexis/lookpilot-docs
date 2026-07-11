## LookPilot Configuration
1. Set protocol to `freetrack`
2. Click **Start** to begin tracking

## Euro Truck Simulator 2 Setup
Head tracking should work automatically. If it doesn't respond, check the game's settings for a TrackIR or head tracking option that may need to be enabled. 

## Common issues
### Game not reacting to tracking input even though the tracking is running
1. Make sure to have the line "uset g_trackir" set to "1" (including the quotes) in *../Documents/Euro Truck Simulator 2/config.cfg*.
2. Bind a key in Keys and Buttons for "Enable Head Tracking" and try pressing the key in-game.

### Mouse-look stops working after closing LookPilot
A known issue in SCS titles: if the in-game camera stops following your mouse after you exit LookPilot, restart the game - mouse-look returns. Keeping LookPilot running for the whole session avoids it entirely.

## Reducing jitter and shake
Shaky or twitchy tracking is the most-reported issue across all games, and it almost always traces to the camera picture, not the game:

1. **Light your face from the front.** Backlighting (a window or lamp behind you) starves the tracker of facial detail and produces micro-jumps.
2. **Check your camera's real frame rate.** Many webcams silently drop to 10-15 fps in low light even when set to 30. In LookPilot, watch the *Tracker fps* readout while tracking - if it is far below your camera's rating, more light usually fixes it.
3. **Raise smoothing.** In *Settings -> Tracking*, increase smoothing/filtering until stillness feels stable, then walk it back until the response feels quick enough.
4. **Flatten the curve center.** Give the response curves a gentle plateau around the center so breathing and small posture shifts do not move the camera.

## Recentering
Press **Alt+C** (default) to recenter tracking on your current head position at any time - do it once seated in your normal driving position, looking at the center of your screen. If you find yourself recentering constantly, move the webcam so it faces you head-on (an off-axis camera makes turned positions read as drift) and recenter while looking at the horizon in-game, not at the camera.

## Using a wheel or HOTAS alongside LookPilot
If your wheel or stick misbehaves while LookPilot runs (stiff force feedback, lost input), make sure the output protocol is `freetrack` rather than *virtual joystick* - the virtual joystick device can conflict with some wheel drivers. ETS2 reads the FreeTrack protocol directly, so the virtual joystick is not needed.

## FAQ
**Does ETS2 need TrackIR hardware for this?** No - ETS2 listens for the FreeTrack/TrackIR protocol, and LookPilot speaks it with just your webcam. ETS2 is the single most-played game among LookPilot users.

**Tracking worked yesterday but not after a game update?** SCS updates sometimes reset `g_trackir` in config.cfg - re-check step 1 under Common issues.

**Where do I make looking-behind faster for reversing?** *Settings -> Tracking* - steepen the yaw curve's outer section so a small extra head turn sweeps the camera further at docks.
