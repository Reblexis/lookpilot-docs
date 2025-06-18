## Opentrack
TODO.

## How to set it up
1. Set protocol to `opentrack`.
2. In opentrack set Tracker to `UDP over network`
3. Press `Start tracking` in LookPilot 

## Recommendations
- As opentrack has its own mapping system, it's recommended to modify mapping in only one of the apps and keep it to identity in the other.
- If you'd like to use native LookPilot filtering (smoothing or deadzone) then set opentrack `Filter` to none. If you want to take advantage of filters provided by opentrack, then set both `deadzone` and `smoothness` to 0 in LookPilot.
