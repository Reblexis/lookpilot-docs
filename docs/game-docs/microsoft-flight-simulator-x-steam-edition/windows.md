## LookPilot Configuration

1. Install opentrack from the [opentrack releases page](https://github.com/opentrack/opentrack/releases/latest).
2. Configure SimConnect in opentrack using the [SimConnect protocol documentation](https://mintlify.com/opentrack/opentrack/protocols/simconnect). For the Steam SimConnect MSI path, see [SimConnect FSX SDK for Steam edition](https://github.com/opentrack/opentrack/wiki/SimConnect-FSX-SDK-for-Steam-edition).
3. Follow [OpenTrack setup with LookPilot](../../app-docs/opentrack-setup/windows.md): protocol `opentrack`, opentrack tracker **UDP over network**.
4. Click **Start tracking** in LookPilot, then **Start** in opentrack.
5. Launch **Microsoft Flight Simulator X: Steam Edition** from Steam. If tracking fails after the first setup, fully quit and restart the sim.

## Microsoft Flight Simulator X: Steam Edition Setup

Head tracking should work automatically once opentrack is connected.

## Common issues

### Head tracking does not respond

1. See **Troubleshooting** in the [SimConnect protocol documentation](https://mintlify.com/opentrack/opentrack/protocols/simconnect).
2. Fully quit and restart the sim after the first opentrack connection.
