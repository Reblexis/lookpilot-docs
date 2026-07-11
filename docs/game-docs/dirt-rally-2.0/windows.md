## LookPilot Configuration
1. Set protocol to `freetrack`
2. Click **Start** to begin tracking

## DiRT Rally 2.0 Setup
Head tracking should work automatically. If it doesn't respond, check the game's settings for a TrackIR or head tracking option that may need to be enabled.

## Credits
Thanks to malinkb for helping with this guide.

## Common issues
### Game connects only sometimes
Reported by DiRT Rally 2.0 players: start tracking first, then launch the game - Codemasters titles check for the tracker at startup. If the status stays yellow, restart the game with tracking already running rather than restarting LookPilot.

## Reducing jitter and shake
Shaky or twitchy tracking is the most-reported issue across all games, and it almost always traces to the camera picture, not the game:

1. **Light your face from the front.** Backlighting (a window or lamp behind you) starves the tracker of facial detail and produces micro-jumps.
2. **Check your camera's real frame rate.** Many webcams silently drop to 10-15 fps in low light even when set to 30. In LookPilot, watch the *Tracker fps* readout while tracking - if it is far below your camera's rating, more light usually fixes it.
3. **Raise smoothing.** In *Settings -> Tracking*, increase smoothing/filtering until stillness feels stable, then walk it back until the response feels quick enough.
4. **Flatten the curve center.** Give the response curves a gentle plateau around the center so breathing and small posture shifts do not move the camera.

## Recentering
Press **Alt+C** (default) to recenter tracking on your current head position at any time - do it once seated in your normal driving position, looking at the center of your screen. If you find yourself recentering constantly, move the webcam so it faces you head-on (an off-axis camera makes turned positions read as drift) and recenter while looking at the horizon in-game, not at the camera.
