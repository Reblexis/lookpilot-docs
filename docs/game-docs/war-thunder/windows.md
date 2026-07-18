## LookPilot Configuration
1. Set protocol to `freetrack`
2. Click **Start** to begin tracking

## War Thunder Setup
Head tracking should work automatically. If it doesn't respond, open War Thunder's Controls settings and look for the TrackIR / head tracking option - it may need to be enabled there.

## Common issues
### Anti-cheat reports blocking NPClient64.dll / status stays yellow
This is almost always a War Thunder anti-cheat (BattlEye) regression on the game's side, not a LookPilot problem. It has happened before and was resolved with the War Thunder developers, historically within hours to a day or two. What to do:
1. Update War Thunder (and let BattlEye update itself), then retry.
2. If it persists, reinstalling the game has fixed recurrences for some users.
3. As an interim route, head tracking can be sent through opentrack instead - see the Opentrack Setup guide.
