## LookPilot Configuration
1. Set protocol to `freetrack`
2. Click **Start** to begin tracking

## iRacing Setup
iRacing supports head tracking natively through the Freetrack protocol. The game will automatically detect the head tracking input once LookPilot is running.

### Tips for iRacing
- For iRacing, **very subtle head tracking** works best
- Too much movement makes the experience abrupt and disorienting
- Focus primarily on **Yaw** (left/right look) movements
- Keep pitch and translation movements minimal
- Head tracking helps with mirror checks and looking into corners

## Common issues
### Tracking feels jumpy even with my head still
Reported by several iRacing users, and iRacing's fast cameras amplify it. Work through the jitter checklist below, then keep overall sensitivity low - iRacing rewards the subtle setup described above more than any other sim.

## Reducing jitter and shake
Shaky or twitchy tracking is the most-reported issue across all games, and it almost always traces to the camera picture, not the game:

1. **Light your face from the front.** Backlighting (a window or lamp behind you) starves the tracker of facial detail and produces micro-jumps.
2. **Check your camera's real frame rate.** Many webcams silently drop to 10-15 fps in low light even when set to 30. In LookPilot, watch the *Tracker fps* readout while tracking - if it is far below your camera's rating, more light usually fixes it.
3. **Raise smoothing.** In *Settings -> Tracking*, increase smoothing/filtering until stillness feels stable, then walk it back until the response feels quick enough.
4. **Flatten the curve center.** Give the response curves a gentle plateau around the center so breathing and small posture shifts do not move the camera.

## Recentering
Press **Alt+C** (default) to recenter tracking on your current head position at any time - do it once seated in your normal driving position, looking at the center of your screen. If you find yourself recentering constantly, move the webcam so it faces you head-on (an off-axis camera makes turned positions read as drift) and recenter while looking at the horizon in-game, not at the camera.

## Using a wheel or HOTAS alongside LookPilot
If your wheel or stick misbehaves while LookPilot runs (stiff force feedback, lost input), make sure the output protocol is `freetrack` rather than *virtual joystick* - the virtual joystick device can conflict with some wheel drivers. iRacing reads the FreeTrack protocol directly, so the virtual joystick is not needed.

## FAQ
**Is head tracking allowed in iRacing?** Yes - iRacing supports TrackIR-protocol head tracking natively; it is a normal, widely-used accessibility and awareness aid in official racing.
