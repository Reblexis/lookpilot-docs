## LookPilot Configuration

FSX uses **SimConnect** for external head pose. LookPilot does not speak SimConnect directly; use **opentrack** as the bridge (UDP from LookPilot, SimConnect output from opentrack).

1. Install opentrack from the [opentrack releases page](https://github.com/opentrack/opentrack/releases/latest).
2. Configure SimConnect in opentrack using opentrack’s [SimConnect protocol documentation](https://mintlify.com/opentrack/opentrack/protocols/simconnect) (install the SimConnect client, set Output to **Microsoft FSX SimConnect**, pick the manifest for your FSX version, troubleshooting).
3. Follow [OpenTrack setup with LookPilot](../../app-docs/opentrack-setup/windows.md): set protocol to `opentrack` in LookPilot and **UDP over network** as the tracker in opentrack.
4. Click **Start tracking** in LookPilot, then **Start** in opentrack.
5. Launch the game. If tracking does not work after the first setup, fully quit and restart the sim.

## Microsoft Flight Simulator X Setup

Head tracking should work once opentrack is connected with SimConnect. You usually do not need a separate TrackIR option in the sim.

## Common issues

### Head tracking does not respond

1. Use the **Troubleshooting** section in opentrack’s [SimConnect protocol documentation](https://mintlify.com/opentrack/opentrack/protocols/simconnect) (manifest, SDK install, errors).
2. Fully quit and restart FSX after the first time you connect opentrack.
