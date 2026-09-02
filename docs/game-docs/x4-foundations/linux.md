## Linux Native (UDP Protocol)

Use this method if you're running the native Linux version of X4: Foundations
(the build Steam installs on Linux by default).

LookPilot's `auto` protocol only finds games running under Wine or Proton, so a
native Linux game never shows up there. The native X4 build reads the OpenTrack
UDP protocol directly since game version 7.50; older versions have no head
tracking on Linux at all (use the Windows version via Proton below).

### LookPilot Configuration
1. Set protocol to `udp`
2. Set IP address to `127.0.0.1`
3. Set port to `4242`
4. Click **Start** to begin tracking

### X4: Foundations Setup
1. Make sure the game is version 7.50 or newer
2. Open **Settings** > **Controls** and enable the **OpenTrack** head tracking option
3. Head tracking should respond as soon as LookPilot is tracking. If it does not, restart the game with LookPilot already running.

## Windows version via Proton

Use this method if you're running the Windows version of X4: Foundations via
Proton or Wine.

### LookPilot Configuration
1. Set protocol to `auto`
2. Launch X4: Foundations
3. Select the game's Wine prefix in the `Game's Wine prefix` dropdown
4. Click **Start tracking** and wait about 10 seconds
5. If the game does not react, click **Stop tracking**, restart the game, and click **Start tracking** again

### X4: Foundations Setup
Head tracking should work automatically. If it doesn't respond, check the game's settings for a TrackIR or head tracking option that may need to be enabled.
