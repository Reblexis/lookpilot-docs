## LookPilot Configuration
1. Set protocol to `freetrack`
2. Click **Start** to begin tracking

## Nuclear Option Setup
1. In the game, go to **Controls** and enable **Use TrackIR inputs for cockpit camera**
2. Enter the cockpit view before restarting the game, and again after restarting, for tracking to connect

## Common issues
### Status stays "unconnected"
Nuclear Option only picks up the tracker from the cockpit view - enter the cockpit, and if you started the game before tracking, restart the game with tracking already running (the two-step in the setup above exists because of this).

### Camera moves when I blink
That is the eye-tracking influence reacting to blinks. If it bothers you, lower or disable the eye-tracking influence (or just eye pitch) in *Settings -> Tracking -> Eye tracking* - head tracking is unaffected.

## Reducing jitter and shake
Shaky or twitchy tracking is the most-reported issue across all games, and it almost always traces to the camera picture, not the game:

1. **Light your face from the front.** Backlighting (a window or lamp behind you) starves the tracker of facial detail and produces micro-jumps.
2. **Check your camera's real frame rate.** Many webcams silently drop to 10-15 fps in low light even when set to 30. In LookPilot, watch the *Tracker fps* readout while tracking - if it is far below your camera's rating, more light usually fixes it.
3. **Raise smoothing.** In *Settings -> Tracking*, increase smoothing/filtering until stillness feels stable, then walk it back until the response feels quick enough.
4. **Flatten the curve center.** Give the response curves a gentle plateau around the center so breathing and small posture shifts do not move the camera.

## Recentering
Press **Alt+C** (default) to recenter tracking on your current head position at any time - do it once seated in your normal driving position, looking at the center of your screen. If you find yourself recentering constantly, move the webcam so it faces you head-on (an off-axis camera makes turned positions read as drift) and recenter while looking at the horizon in-game, not at the camera.
