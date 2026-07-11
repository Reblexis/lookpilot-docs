## LookPilot Configuration
1. Set protocol to `freetrack`
2. Click **Start** to begin tracking

## DCS World Setup
1. Launch DCS World
2. Go to `OPTIONS` → `CONTROLS`
3. In the control settings, TrackIR/head tracking should be automatically detected
4. Head tracking works natively with the freetrack protocol

DCS has extensive head tracking support and should detect your setup automatically once LookPilot is running.

## Common issues
### Game FPS drops when DCS has focus
A few users report DCS frame drops while LookPilot runs in the background. If you see this: close other camera apps, try a lower camera resolution in *Settings -> Camera* (tracking quality is driven by frame rate more than resolution), and make sure Windows' *Game Mode* is not throttling background apps aggressively.

### Head position sits wrong relative to the gunsight (IL-2 style offsets)
DCS reads 6DoF but the neutral position is yours to define: sit in your normal flying posture, look at the center of the screen, and press **Alt+C** to make that the zero point. Repeat any time the seat position feels off.

## Reducing jitter and shake
Shaky or twitchy tracking is the most-reported issue across all games, and it almost always traces to the camera picture, not the game:

1. **Light your face from the front.** Backlighting (a window or lamp behind you) starves the tracker of facial detail and produces micro-jumps.
2. **Check your camera's real frame rate.** Many webcams silently drop to 10-15 fps in low light even when set to 30. In LookPilot, watch the *Tracker fps* readout while tracking - if it is far below your camera's rating, more light usually fixes it.
3. **Raise smoothing.** In *Settings -> Tracking*, increase smoothing/filtering until stillness feels stable, then walk it back until the response feels quick enough.
4. **Flatten the curve center.** Give the response curves a gentle plateau around the center so breathing and small posture shifts do not move the camera.

## Recentering
Press **Alt+C** (default) to recenter tracking on your current head position at any time - do it once seated in your normal driving position, looking at the center of your screen. If you find yourself recentering constantly, move the webcam so it faces you head-on (an off-axis camera makes turned positions read as drift) and recenter while looking at the horizon in-game, not at the camera.

## Using a wheel or HOTAS alongside LookPilot
If your wheel or stick misbehaves while LookPilot runs (stiff force feedback, lost input), make sure the output protocol is `freetrack` rather than *virtual joystick* - the virtual joystick device can conflict with some wheel drivers. DCS reads the FreeTrack protocol directly, so the virtual joystick is not needed.

## FAQ
**Do I need to configure anything in the DCS axis tuning?** Usually not - DCS maps TrackIR input automatically once detected (check the TrackIR column under Axis Controls if you want to verify). If the column shows nothing, restart DCS with tracking already running.
