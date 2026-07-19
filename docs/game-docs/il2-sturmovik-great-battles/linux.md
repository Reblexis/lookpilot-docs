## LookPilot Configuration
1. Set protocol to `auto`
2. Launch the game
3. Select the IL-2 Sturmovik Wine prefix in the `Game's Wine prefix` dropdown
4. Click **Start tracking** to begin tracking

### Fallback Option
If the above method doesn't work, try using the freetrack (Wine) protocol:

1. Set protocol to `freetrack (Wine)`
2. Select your Steam installation from the dropdown
3. Set Game to `IL-2 Sturmovik: Battle of Stalingrad` in the game dropdown
4. Launch the game from Steam
5. Click **Start tracking** to begin tracking

## IL-2 Sturmovik: Great Battles Setup
1. If launching the game from Steam, make sure to force the use of specific compatibility tool (Proton)
2. Head tracking should work once LookPilot is running

## Second fallback: virtual joystick
If neither `auto` nor `freetrack (Wine)` ever connects (status stays yellow), users have had good results with the `virtual joystick` protocol instead (community-confirmed):

1. Set protocol to `virtual joystick` and start tracking.
2. In IL-2's controls, bind **Bow head vertically** and **Bow head horizontally** to the virtual right stick axes.
