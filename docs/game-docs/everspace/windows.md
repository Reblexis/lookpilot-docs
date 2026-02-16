## Prerequisites

Before setting up head tracking for EVERSPACE, you need to copy the NPClient64.dll file:

1. Open your Steam Library in the Steam client
2. Right-click **LookPilot** → **Manage** → **Browse local files**
3. Navigate to `main.dist/data/static/protocols`
4. Copy the **NPClient64.dll** file
5. Right-click **EVERSPACE** in your Steam Library → **Manage** → **Browse local files**
6. Navigate to `RSG/Plugins/TrackIR/ThirdParty/TrackIR/Win64`
7. Paste the **NPClient64.dll** file that you copied from LookPilot's folder (replace the existing one if needed)
8. Restart EVERSPACE

## LookPilot Configuration
1. Set protocol to `freetrack`
2. Click **Start** to begin tracking

## EVERSPACE Setup
1. In the game options, ensure head tracking is enabled
2. Switch to **Cockpit View** in-game (head tracking only works in cockpit view)