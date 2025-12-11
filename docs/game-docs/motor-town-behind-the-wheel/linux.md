## Prerequisites

Before setting up head tracking for Motor Town: Behind the Wheel, you need to copy the NPClient64.dll file:

1. Open your Steam Library in the Steam client
2. Right-click **LookPilot** → **Manage** → **Browse local files**
3. Navigate to `main.dist/data/static/protocols`
4. Copy the **NPClient64.dll** file
5. Right-click **Motor Town: Behind the Wheel** in your Steam Library → **Manage** → **Browse local files**
6. Navigate to `MotorTown/Binaries/Win64`
7. Paste the **NPClient64.dll** file that you copied from LookPilot's folder (replace the existing one if needed)
8. Restart Motor Town: Behind the Wheel

## LookPilot Configuration

1. Set protocol to `auto`
2. Launch the game
3. Select the Motor Town: Behind the Wheel prefix in `Game's wine prefix` dropdown
4. Click **Start tracking** to begin tracking and wait for about 10 seconds
5. Click **Stop tracking**
6. Restart the game
7. Click **Start tracking**

### Fallback Option

If the above method doesn't work, try using the freetrack (Wine) protocol:

1. Set protocol to `freetrack (wine)`
2. Select your Steam installation from the dropdown
3. Set Game to `Motor Town: Behind the Wheel` in the game dropdown
4. Launch the game from Steam
5. Click **Start tracking** to begin tracking and wait for about 10 seconds
6. Click **Stop tracking**
7. Restart the game
8. Click **Start tracking**

## Motor Town: Behind the Wheel Setup

1. If launching the game from Steam, make sure to force the use of specific compatibility tool (Proton)
2. Should work out of the box after completing the prerequisites
