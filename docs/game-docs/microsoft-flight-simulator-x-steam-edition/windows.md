## LookPilot configuration

FSX: Steam Edition is **more involved** than games that only need a single LookPilot protocol. External head pose is delivered through **SimConnect**, not LookPilot’s FreeTrack-style protocol. The supported approach matches [Beam Eye Tracker’s FSX: Steam Edition notes](https://beam.eyeware.tech/games/microsoft-flight-simulator-x-steam-edition/): **LookPilot → opentrack → Microsoft FSX SimConnect**.

1. Install **opentrack** from the [opentrack releases page](https://github.com/opentrack/opentrack/releases/latest).
2. Follow [OpenTrack setup with LookPilot](../../app-docs/opentrack-setup/windows.md): in LookPilot set **Protocol** to `opentrack`; in opentrack set **Tracker** to **UDP over network**.
3. In opentrack, set **Output** to **Microsoft FSX SimConnect**.
4. Click **Start tracking** in LookPilot, then **Start** in opentrack and confirm the preview moves with your head.
5. Launch **Microsoft Flight Simulator X: Steam Edition** from Steam. After the first-time setup of this chain, **fully quit and restart** the sim if it does not react—FSX often only notices SimConnect clients after a clean launch.

## Microsoft Flight Simulator X: Steam Edition setup

No separate in-game “enable TrackIR” step is usually required once opentrack is running with **Microsoft FSX SimConnect** output.
