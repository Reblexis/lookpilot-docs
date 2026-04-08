## LookPilot configuration

FSX: Steam Edition is **more involved** than games that only need a single LookPilot protocol. External head pose goes through **SimConnect**, which **opentrack** drives—not a SimConnect option inside LookPilot.

**LookPilot:** set **Protocol** to **`opentrack`** (UDP into opentrack).

**Opentrack and SimConnect:** install opentrack from the [opentrack releases page](https://github.com/opentrack/opentrack/releases/latest), then follow opentrack’s **[SimConnect protocol documentation](https://mintlify.com/opentrack/opentrack/protocols/simconnect)** for the SimConnect client (`SimConnect.msi`), choosing **Microsoft FSX SimConnect** as output, picking the right manifest, starting opentrack, and troubleshooting. For the **Steam** install layout and where to run the MSI, opentrack also documents this in **[SimConnect FSX SDK for Steam edition](https://github.com/opentrack/opentrack/wiki/SimConnect-FSX-SDK-for-Steam-edition)** (wiki).

**With LookPilot:** use [OpenTrack setup with LookPilot](../../app-docs/opentrack-setup/windows.md) (LookPilot **Protocol** `opentrack`, opentrack **Tracker** **UDP over network**). After SimConnect is configured in opentrack, click **Start tracking** in LookPilot, **Start** in opentrack, then launch **Microsoft Flight Simulator X: Steam Edition** from Steam. **Fully quit and restart** the sim once after the first-time setup if it does not react.

The same overall workflow is described in [Beam Eye Tracker’s FSX: Steam Edition guide](https://beam.eyeware.tech/games/microsoft-flight-simulator-x-steam-edition/).

## Microsoft Flight Simulator X: Steam Edition setup

Usually no separate in-game “enable TrackIR” step is required once opentrack’s SimConnect output is working. If the camera still does not move, use **Troubleshooting** in opentrack’s [SimConnect protocol documentation](https://mintlify.com/opentrack/opentrack/protocols/simconnect).
