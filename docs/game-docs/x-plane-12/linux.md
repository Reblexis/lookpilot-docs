## LookPilot Configuration
1. Set protocol to `auto`
2. Launch X-Plane 12
3. Select the X-Plane 12 Wine prefix in the `Game's Wine prefix` dropdown
4. Click **Start tracking** to begin tracking and wait for about 10 seconds
5. Click **Stop tracking**
6. Restart the game
7. Click **Start tracking**

### Fallback Option 1: Freetrack (Wine)
If the above method doesn't work, try using the freetrack (Wine) protocol:

1. Set protocol to `freetrack (Wine)`
2. Set launcher to `Other`
3. Find and select X-Plane 12's `Wine prefix` path
4. Find and select X-Plane 12's `Wine executable` path
5. Launch the game
6. Click **Start tracking** to begin tracking and wait for about 10 seconds
7. Click **Stop tracking**
8. Restart the game
9. Click **Start tracking**

### Fallback Option 2: UDP Protocol
If both methods above fail, you can use the UDP protocol with a third-party plugin:

#### Prerequisites
1. Install the headtrack plugin for X-Plane 12:
   - Download the headtrack plugin from GitHub: [amyinorbit/headtrack](https://github.com/amyinorbit/headtrack)
   - Get the latest release: [2209.1r2](https://github.com/amyinorbit/headtrack/releases/tag/2209.1r2) (as of the original writing)
   - Download the release zip file: [htrack-1010-2209.1r2.zip](https://github.com/amyinorbit/headtrack/releases/download/2209.1r2/htrack-1010-2209.1r2.zip)
   - Extract the zip file and navigate to the `htrack/lin_x64` folder
   - Copy `htrack.xpl` to your X-Plane plugin folder (usually `X-Plane 12/Resources/plugins`)

#### LookPilot Configuration
1. Set protocol to `udp`
2. Set IP address to `127.0.0.1`
3. Set port to `4242`
4. Click **Start** to begin tracking

#### X-Plane 12 Setup
1. Start X-Plane 12 and launch your aircraft
2. Once in the cockpit, move your mouse cursor to the top of the screen to open the menu bar
3. Click on **Plugins**
4. You should see **HeadTrack** in the menu
5. Click **Track Head Motion** to enable head tracking
6. Additional settings can be found in the **Settings...** option in the plugin's menu

## X-Plane 12 Setup
Head tracking should work out of the box once properly configured. No additional in-game setup is required for the auto and freetrack protocols.

## Tips
1. For the UDP method, make initial adjustments and response curve settings in LookPilot first, then fine-tune in the plugin if needed
2. The UDP method eliminates Wine overhead and may provide better performance
3. If you experience issues with the standard methods, the UDP fallback has been tested to work reliably on Ubuntu/Kubuntu 23.10

## Credits
The UDP fallback solution is based on the work by Randy Bancroft (CannonFodderSE) documented in the [OpenTrack GitHub discussions](https://github.com/opentrack/opentrack/discussions/1836).
