## LookPilot Configuration
1. Select your webcam in LookPilot and confirm the preview follows your face
2. Set protocol to `freetrack`
3. Click **Start** to begin tracking, sit in your normal flying position and recenter
4. Launch Microsoft Flight Simulator 2024 after tracking has started

## Microsoft Flight Simulator 2024 Setup
Head tracking should work automatically: the simulator detects TrackIR/FreeTrack-compatible devices, and LookPilot speaks that protocol with just your webcam, no IR clip or dedicated tracking camera needed. If the cockpit view does not respond, check the simulator's camera settings for a TrackIR or head tracking option that may need to be enabled (community reports on the official forums point at this switch when detection fails).

## What head tracking changes in the cockpit
The view follows your head instead of a hat switch: rotate to scan the runway and traffic, lean toward the instruments, shift sideways around the cockpit frame, and look into a turn while your hands stay on the yoke and throttle.

- **Yaw and pitch**: look left/right and up/down
- **Roll**: tilt naturally with the aircraft
- **X, Y and Z translation**: lean sideways, move up/down, or move closer to a panel

## Recommended baseline for flight simulation
From the [tracking settings guide](../../app-docs/tracking-settings/guide.md):

- Enable all six head axes (Yaw, Pitch, Roll, X, Y, Z)
- Global deadzone 0.05-0.1
- Global smoothness 0.2-0.4

Then tune for your webcam, monitor, seating position and aircraft: raise smoothing if the picture jitters, lower it if movement feels delayed, and set rotation sensitivity so you can check the side windows without losing sight of the monitor. Keep translation gentler than rotation if leaning feels exaggerated.

## Common issues
### Simulator does not respond to tracking
1. Start LookPilot and tracking before the simulator, and confirm the protocol is `freetrack`.
2. Check the simulator's camera settings for a TrackIR or head tracking option.
3. If tracking moves in LookPilot's preview but not in-game, stop and restart tracking, then restart the simulator.

### View drifts or no longer faces forward
Return to a neutral posture and recenter. If you recenter constantly, move the webcam so it faces you head-on (an off-axis camera makes turned positions read as drift) and recenter while looking at the horizon, not at the camera.

### Jittery cockpit view
Light your face from the front, keep your whole face in the picture, raise the webcam image quality, or add a little smoothing. Many webcams silently drop to 10-15 fps in low light; watch the *Tracker fps* readout while tracking.

### Movement feels delayed
Lower smoothing gradually and check that the webcam is running at a suitable frame rate.

### View moves too far
Reduce rotation or translation sensitivity, or soften the affected axis curve in *Settings -> Tracking*.

## FAQ
**Does MSFS 2024 support webcam head tracking?** It receives TrackIR/FreeTrack-compatible head-tracking data; LookPilot converts webcam movement into that data.

**Do I need TrackIR hardware?** No. LookPilot uses a standard built-in or USB webcam.

**Is the tracking 6DoF?** Yes: yaw, pitch, roll, left/right, up/down and forward/back.

**What settings should I start with?** All six axes, deadzone 0.05-0.1, smoothness 0.2-0.4, then adjust to taste.

**Should LookPilot start before MSFS 2024?** Yes. Starting tracking first gives the simulator the best chance to detect the output when it launches.

**Can I try it before buying?** Yes. LookPilot has a 14-day free trial; the lifetime license is $14.99.
