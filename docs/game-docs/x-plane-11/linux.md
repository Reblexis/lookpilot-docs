## Linux Native (UDP Protocol)

Use this method if you're running the native Linux version of X-Plane 11.

### Prerequisites
1. Install the headtrack plugin for X-Plane 11:
   - Download the headtrack plugin from GitHub: [amyinorbit/headtrack](https://github.com/amyinorbit/headtrack)
   - Get the latest release: [2209.1r2](https://github.com/amyinorbit/headtrack/releases/tag/2209.1r2) (as of the original writing)
   - Download the release zip file: [htrack-1010-2209.1r2.zip](https://github.com/amyinorbit/headtrack/releases/download/2209.1r2/htrack-1010-2209.1r2.zip)
   - Extract the zip file and navigate to the `htrack/lin_x64` folder
   - Copy `htrack.xpl` to your X-Plane plugin folder (usually `X-Plane 11/Resources/plugins`)

### LookPilot Configuration
1. Set protocol to `udp`
2. Set IP address to `127.0.0.1`
3. Set port to `4242`
4. Click **Start** to begin tracking

### X-Plane 11 Setup
1. Start X-Plane 11 and launch your aircraft
2. Once in the cockpit, move your mouse cursor to the top of the screen to open the menu bar
3. Click on **Plugins**
4. You should see **HeadTrack** in the menu
5. Click **Track Head Motion** to enable head tracking
6. Additional settings can be found in the **Settings...** option in the plugin's menu

## Windows via Wine

Use these methods if you're running the Windows version of X-Plane 11 via Wine/Proton.

### Option 1: Auto Protocol
1. Set protocol to `auto`
2. Launch X-Plane 11
3. Select the X-Plane 11 Wine prefix in the `Game's Wine prefix` dropdown
4. Click **Start tracking** to begin tracking and wait for about 10 seconds
5. Click **Stop tracking**
6. Restart the game
7. Click **Start tracking**

### Option 2: Freetrack (Wine)
If the auto method doesn't work, try using the freetrack (Wine) protocol:

1. Set protocol to `freetrack (Wine)`
2. Set launcher to `Other`
3. Find and select X-Plane 11's `Wine prefix` path
4. Find and select X-Plane 11's `Wine executable` path
5. Launch the game
6. Click **Start tracking** to begin tracking and wait for about 10 seconds
7. Click **Stop tracking**
8. Restart the game
9. Click **Start tracking**

### X-Plane 11 In-Game Setup (Wine)
1. In X-Plane 11, go to **Settings** > **Graphics**
2. **Important**: Check the **TrackIR** checkbox (located alongside the V-sync option)
3. Head tracking should now work with the auto and freetrack protocols

## Tips
1. For the UDP method, make initial adjustments and response curve settings in LookPilot first, then fine-tune in the plugin if needed
2. The UDP method eliminates Wine overhead and may provide better performance
3. The UDP method has been tested to work reliably on Ubuntu/Kubuntu 23.10

## Credits
The UDP solution is based on the work by Randy Bancroft (CannonFodderSE) documented in the [OpenTrack GitHub discussions](https://github.com/opentrack/opentrack/discussions/1836).
