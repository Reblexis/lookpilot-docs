**opentrack** is a free, open-source head-tracking program that manages and transmits pose information to games and simulators.

## Where to Find Protocol Settings

All protocol settings described below can be found at the top of the **General** tab in **Tracking settings**. Click the **Settings** button in the output pose visualization to open the Tracking settings window.

## When do you need opentrack?

Most users don't need opentrack. LookPilot works directly with games through FreeTrack (TrackIR emulation) and Virtual Joystick protocols. However, opentrack is useful for specific edge cases:

* **Mouse emulation** – for games that only support mouse input for camera control
* **Additional output protocols** – such as `SimConnect`, `OpenXR`, or raw `UDP` not directly supported by LookPilot
* **Alternative filtering** – opentrack offers different filtering algorithms (`Accela`, `Kalman`, `EWMA`) that some users prefer

## Installation

For Linux users, we recommend using the Star Citizen-optimized fork which includes important compatibility fixes for Wine/Proton games and proper build instructions:

[**opentrack-StarCitizen**](https://github.com/Priton-CE/opentrack-StarCitizen) - Fork with improved compatibility for UMU-enabled launchers (like Lutris) and custom Proton prefixes, plus clear step-by-step build instructions.

Follow the build instructions in the repository to compile from source.

## How to set it up with LookPilot

1. Launch **opentrack**
2. In **LookPilot**, go to **Tracking settings** (click the **Settings** button in the output pose visualization)
3. At the top of the **General** tab, set **Protocol** to `opentrack`
4. In opentrack, set **Tracker** to **UDP over network**
5. Click **Start tracking** in LookPilot
6. Click **Start** in opentrack
7. The octopus model in opentrack should move as you move your head

## How to use opentrack (quick version)

- In opentrack, choose an **Output** your game supports (e.g. `Freetrack`, `Virtual Joystick`, `SimConnect`, or `mouse emulation`)
- Click **Start** to begin tracking
- Pick a filter under **Filter** if you want smoothing beyond the default

For a detailed walkthrough with screenshots, see the official [Quick-Start Guide](https://github.com/opentrack/opentrack/wiki/Quick-Start-Guide-%28WIP%29). Many video tutorials are also available on YouTube.

## Recommendations for LookPilot + opentrack

- Adjust mapping curves in **only one** app (either opentrack *or* LookPilot) and leave the other set to **Identity**
- To use LookPilot's filtering (smoothing or deadzone), set **Filter** to **None** in opentrack
- To rely on opentrack's filters instead, set **Deadzone** and **Smoothness** to **0** in LookPilot (under **Head-tracking settings** and **Eye-tracking settings**)

