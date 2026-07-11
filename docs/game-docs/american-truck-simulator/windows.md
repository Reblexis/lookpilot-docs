## LookPilot Configuration
1. Set protocol to `freetrack`
2. Click **Start** to begin tracking

## American Truck Simulator Setup
Head tracking should work automatically. If it doesn't respond, check the game's settings for a TrackIR or head tracking option that may need to be enabled. 

## Common issues
### Game not reacting to tracking input even though the tracking is running
1. Make sure to have the line "uset g_trackir" set to "1" (including the quotes) in *../Documents/American Truck Simulator/config.cfg*.

### Mouse-look stops working after closing LookPilot
A known issue in SCS titles: if the in-game camera stops following your mouse after you exit LookPilot, restart the game - mouse-look returns. Keeping LookPilot running for the whole session avoids it entirely.

### Having to re-center constantly while driving
The most common ATS complaint. Three things fix nearly all of it: put the webcam dead-center under or above your monitor (not off to the side), recenter with **Alt+C** while sitting in your natural driving posture, and add a small center plateau to the yaw curve in *Settings -> Tracking* so highway posture drift does not accumulate into the camera.

## Reducing jitter and shake
Shaky or twitchy tracking is the most-reported issue across all games, and it almost always traces to the camera picture, not the game:

1. **Light your face from the front.** Backlighting (a window or lamp behind you) starves the tracker of facial detail and produces micro-jumps.
2. **Check your camera's real frame rate.** Many webcams silently drop to 10-15 fps in low light even when set to 30. In LookPilot, watch the *Tracker fps* readout while tracking - if it is far below your camera's rating, more light usually fixes it.
3. **Raise smoothing.** In *Settings -> Tracking*, increase smoothing/filtering until stillness feels stable, then walk it back until the response feels quick enough.
4. **Flatten the curve center.** Give the response curves a gentle plateau around the center so breathing and small posture shifts do not move the camera.

## Using a wheel or HOTAS alongside LookPilot
If your wheel or stick misbehaves while LookPilot runs (stiff force feedback, lost input), make sure the output protocol is `freetrack` rather than *virtual joystick* - the virtual joystick device can conflict with some wheel drivers. ATS reads the FreeTrack protocol directly, so the virtual joystick is not needed.

## FAQ
**Do I need TrackIR hardware?** No - ATS reads the FreeTrack protocol, which LookPilot provides from a normal webcam. Together with ETS2, ATS makes up roughly two thirds of all LookPilot tracking hours, so the truck-sim path is the most battle-tested in the app.
