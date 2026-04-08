## LookPilot Configuration

FSX is usually set up with SimConnect through opentrack on **Windows**; the `auto` and `freetrack (Wine)` paths used for many other games are not appropriate here.

1. Set protocol to `virtual joystick`
2. In **Tracking settings**, open each axis tab and use **Mapping** to assign joystick axes for yaw, pitch, and any other motion you want (see [Virtual joystick](../../app-docs/connect-to-any-game/linux.md#2-virtual-joystick)).
3. Launch **Microsoft Flight Simulator X: Steam Edition** from Steam (or your runner)
4. Click **Start tracking**

## Microsoft Flight Simulator X: Steam Edition Setup

1. In **Settings → Controls**, bind pan and tilt (or cockpit view) to the virtual joystick axes you mapped. Prefer non-relative (absolute) control where the sim offers it.

For SimConnect-based head tracking on Windows, use the [Windows guide](windows.md), opentrack’s [SimConnect protocol documentation](https://mintlify.com/opentrack/opentrack/protocols/simconnect), and for the Steam SDK layout opentrack’s wiki [SimConnect FSX SDK for Steam edition](https://github.com/opentrack/opentrack/wiki/SimConnect-FSX-SDK-for-Steam-edition).
