## LookPilot configuration

Microsoft Flight Simulator X is **more involved** than games that only need a single LookPilot protocol. External head pose goes through **SimConnect**, which **opentrack** drives—not a SimConnect option inside LookPilot.

**LookPilot:** set **Protocol** to **`opentrack`** (UDP into opentrack).

**Opentrack and SimConnect:** install opentrack from the [opentrack releases page](https://github.com/opentrack/opentrack/releases/latest), then follow opentrack’s **[SimConnect protocol documentation](https://mintlify.com/opentrack/opentrack/protocols/simconnect)** for the SimConnect client (`SimConnect.msi`), choosing **Microsoft FSX SimConnect** as output, picking the right manifest, starting opentrack, and troubleshooting.

**With LookPilot:** use [OpenTrack setup with LookPilot](../../app-docs/opentrack-setup/windows.md) (LookPilot **Protocol** `opentrack`, opentrack **Tracker** **UDP over network**). After SimConnect is configured in opentrack, click **Start tracking** in LookPilot, **Start** in opentrack, then launch FSX. **Fully quit and restart** FSX once after the first-time setup if the sim does not react.

A similar overall workflow is described in [Beam Eye Tracker’s FSX: Steam Edition guide](https://beam.eyeware.tech/games/microsoft-flight-simulator-x-steam-edition/).

## Microsoft Flight Simulator X setup

Usually no separate in-game “enable TrackIR” step is required once opentrack’s SimConnect output is working. If the camera still does not move, use the **Troubleshooting** section in opentrack’s [SimConnect protocol documentation](https://mintlify.com/opentrack/opentrack/protocols/simconnect).
