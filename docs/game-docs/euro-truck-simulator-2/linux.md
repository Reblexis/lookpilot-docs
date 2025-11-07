## LookPilot Configuration
1. Set protocol to `auto`
2. Launch the game
3. Select the `Euro Truck Simulator 2`'s Wine prefix in `Game's Wine prefix` dropdown
4. Click **Start tracking** to begin tracking and wait for about 10 seconds
5. Click **Stop tracking**
6. Restart the game
7. Click **Start tracking**

### Fallback Option
If the above method doesn't work, try using the freetrack (Proton) protocol:

1. Set protocol to `freetrack (Proton)`
2. Select your Steam installation from the dropdown
3. Set Game to `Euro Truck Simulator 2` in the game dropdown
4. Launch the game from Steam
5. Click **Start tracking** to begin tracking and wait for about 10 seconds
6. Click **Stop tracking**
7. Restart the game
8. Click **Start tracking**

## Euro Truck Simulator 2 Setup
1. If launching the game from Steam, make sure to force the use of specific compatibility tool (Proton)

## Common issues
### Game not reacting to tracking input even though the tracking is running
1. Make sure to have the line "uset g_trackir" set to "1" (including the quotes) in *<STEAM_LIBRARY>/steamapps/compatdata/<APPID>/pfx/drive_c/users/steamuser/Documents/Euro Truck Simulator 2/config.cfg*.
2. Bind a key in Keys and Buttons for "Enable Head Tracking" and try pressing the key in-game.
