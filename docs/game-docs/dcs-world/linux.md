## LookPilot Configuration
1. Set protocol to `auto`
2. Launch the game
3. Select the DCS World Wine prefix in the `Game's Wine prefix` dropdown
4. Click **Start tracking** to begin tracking

### Fallback Option
If the above method doesn't work, try using the freetrack (Wine) protocol:

1. Set protocol to `freetrack (Wine)`
2. Select your Steam installation from the dropdown
3. Set Game to `DCS World Steam Edition` in the game dropdown
4. Launch the game from Steam
5. Click **Start tracking** to begin tracking

## DCS World Setup
1. If launching the game from Steam, make sure to force the use of specific compatibility tool (Proton)
2. Launch DCS World
3. Go to `OPTIONS` → `CONTROLS`
4. Head tracking should be automatically detected

## Launch options (Steam)
If the game connects but behaves oddly (or head tracking axes never appear), these launch options have helped users (community-confirmed):

```
WINEDLLOVERRIDES='wbemprox=n' %command% --no-launcher
```

Then in DCS go to `OPTIONS` -> `CONTROLS` and click **Rescan devices**. If Proton Experimental or a distro-specific Proton fails to connect, force an official Proton version (Proton 9/10) or Proton-GE on the game.

## DCS Standalone via Heroic Games Launcher
A user-confirmed recipe (reproduced by the developer with the AppImage build of Heroic):

1. Use the Heroic **AppImage**, not the Flatpak.
2. Set the game's compatibility tool to **Proton-GE (latest)**.
3. In the game's Heroic settings (Advanced), **disable UMU** and the BattlEye/EAC runtimes.
4. Add the environment variable `WINEDLLOVERRIDES=wbemprox=n`.
5. Launch the game without logs.
6. In LookPilot use the `auto` protocol and pick the **second** detected prefix.
7. Fallback `freetrack (Wine)`: in DCS controls the head tracking axis bindings appear only after clicking **Add Axis**.

## Known issues
- **Connected/Connecting loop with standalone DCS under Lutris (LookPilot 1.9.x)**: the status flips between Connected and Connecting every 1-2 seconds. Until this is fixed, downgrade LookPilot to 1.8.x (Steam -> Properties -> Betas, or the standalone releases page) - developer-confirmed workaround. One user also resolved it by switching Lutris to system Wine 11.0 Staging (community-reported).
- **DCS hangs on exit while tracking is running**: stop tracking in LookPilot before quitting DCS (developer-confirmed; no in-app fix yet).
