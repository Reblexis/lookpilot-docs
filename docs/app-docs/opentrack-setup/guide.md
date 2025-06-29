## opentrack
**opentrack** is a free, open-source head-tracking program that manages and transmits pose information to games and simulators.

### Why pair it with LookPilot?
* **Fallback for tricky titles** – if a game’s built-in head tracking stutters or fails, routing motion through opentrack can restore smoothness.  
* **Broader compatibility** – for games without an official head-tracking API, opentrack can still drive them via outputs such as `Virtual Joystick` (vJoy), `SimConnect`, `OpenXR`, or raw `UDP`—options not exposed directly by **LookPilot**.  
* **Extra filters** – opentrack ships several alternative filtering algorithms (`Accela`, `Kalman`, `EWMA`, etc.) that some users prefer over LookPilot’s built-in choices.  
* **Open ecosystem** – a large community and an extensive plugin library make troubleshooting and experimentation easier.

### Installation
| Platform | Steps |
|----------|-------|
| **Windows** | 1. Download the latest installer from the [opentrack releases page](https://github.com/opentrack/opentrack/releases/latest).<br>2. Run the installer and follow the prompts. |
| **Linux** | Build from source using the official [Linux guide](https://github.com/opentrack/opentrack/wiki/Building-on-Linux). |

## How to set it up with LookPilot
1. Launch **opentrack**.  
2. In **LookPilot**, set **Protocol** to `opentrack`.  
3. In opentrack, set **Tracker** to **UDP over network**.  
4. Click **Start tracking** in LookPilot.  
5. Click **Start** in opentrack.  
6. The octopus model in opentrack should move as you move your head.

## How to use opentrack (quick version)
- In opentrack, choose an **Output** your game supports (e.g. `Freetrack`, `Virtual Joystick`, or `SimConnect`).  
- Click **Start** to begin tracking.  
- Pick a filter under **Filter** if you want smoothing beyond the default.

For a detailed walkthrough with screenshots, see the official [Quick-Start Guide](https://github.com/opentrack/opentrack/wiki/Quick-Start-Guide-%28WIP%29). Many video tutorials are also available on YouTube.

## Recommendations for LookPilot + opentrack
- Adjust mapping curves in **only one** app (either opentrack *or* LookPilot) and leave the other set to **Identity**.  
- To use LookPilot’s filtering (smoothing or deadzone), set **Filter** to **None** in opentrack.  
- To rely on opentrack’s filters instead, set **Deadzone** and **Smoothness** to **0** in LookPilot (under **Head-tracking settings** and **Eye-tracking settings**).
