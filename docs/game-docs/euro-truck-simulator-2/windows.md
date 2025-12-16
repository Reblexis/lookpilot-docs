## LookPilot Configuration
1. Set protocol to `freetrack`
2. Click **Start** to begin tracking

## Euro Truck Simulator 2 Setup
Head tracking should work automatically. If it doesn't respond, check the game's settings for a TrackIR or head tracking option that may need to be enabled. 

## Common issues
### Game not reacting to tracking input even though the tracking is running
1. Make sure to have the line "uset g_trackir" set to "1" (including the quotes) in *../Documents/Euro Truck Simulator 2/config.cfg*.
2. Bind a key in Keys and Buttons for "Enable Head Tracking" and try pressing the key in-game.
