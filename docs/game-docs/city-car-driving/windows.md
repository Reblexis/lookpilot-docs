## LookPilot Configuration
1. Set protocol to `freetrack`
2. Click **Start** to begin tracking

## City Car Driving Setup
Once LookPilot is running, launch the game. Head tracking support may vary by version - check the game's Settings → Controls for TrackIR options, or you may need to edit the `game.ini` file in `Documents\Forward Development\City Car Driving\config` and set `EnableTrackIr=true`.

## Reducing jitter and shake
Shaky or twitchy tracking is the most-reported issue across all games, and it almost always traces to the camera picture, not the game:

1. **Light your face from the front.** Backlighting (a window or lamp behind you) starves the tracker of facial detail and produces micro-jumps.
2. **Check your camera's real frame rate.** Many webcams silently drop to 10-15 fps in low light even when set to 30. In LookPilot, watch the *Tracker fps* readout while tracking - if it is far below your camera's rating, more light usually fixes it.
3. **Raise smoothing.** In *Settings -> Tracking*, increase smoothing/filtering until stillness feels stable, then walk it back until the response feels quick enough.
4. **Flatten the curve center.** Give the response curves a gentle plateau around the center so breathing and small posture shifts do not move the camera.

## Recentering
Press **Alt+C** (default) to recenter tracking on your current head position at any time - do it once seated in your normal driving position, looking at the center of your screen. If you find yourself recentering constantly, move the webcam so it faces you head-on (an off-axis camera makes turned positions read as drift) and recenter while looking at the horizon in-game, not at the camera.

## FAQ
**Which City Car Driving versions support head tracking?** Support varies by version. Newer versions expose TrackIR options under *Settings -> Controls*; older ones need the `EnableTrackIr=true` line in *game.ini* (path above). If neither exists in your version, head tracking is not available in that build.

**Why use head tracking in a driving school simulator?** Mirror checks and junction scanning - the exact habits the simulator teaches - become natural head movements instead of button presses, which is closer to real driving practice.

**Do I need any hardware besides a webcam?** No. City Car Driving listens for the TrackIR protocol and LookPilot provides it from a standard webcam - no clips or IR devices.
