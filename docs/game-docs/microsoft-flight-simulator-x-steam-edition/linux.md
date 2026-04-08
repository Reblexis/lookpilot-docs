## LookPilot configuration

FSX’s native head-tracking path is **SimConnect** (see [OpenTrack setup with LookPilot](../../app-docs/opentrack-setup/linux.md) and [Beam Eye Tracker’s FSX: Steam Edition guide](https://beam.eyeware.tech/games/microsoft-flight-simulator-x-steam-edition/)). That stack is aimed at **Windows**; under Wine/Proton it is often unreliable or impractical.

Do **not** use the **`auto`** protocol here—it assumes FreeTrack-style integration, which does not match how FSX consumes external view pose. **`freetrack (Wine)`** is likewise not a useful route for FSX with LookPilot.

**Practical approach on Linux:** drive the **camera with a virtual joystick** instead (same idea as in the generic [Virtual joystick](../../app-docs/connect-to-any-game/linux.md#2-virtual-joystick) section):

1. Set protocol to `virtual joystick`
2. In **Tracking settings**, open each axis tab and use **Mapping** to choose which joystick axes carry yaw, pitch, and any other motion you want (see the linked guide above)
3. Launch **Microsoft Flight Simulator X: Steam Edition** from Steam (or your runner)
4. Click **Start tracking**

## Microsoft Flight Simulator X: Steam Edition setup

In FSX **Settings → Controls**, assign **pan / tilt** (or cockpit view) to the virtual joystick axes you mapped. Prefer **absolute** (non-relative) behavior where the sim offers it so the view stays aligned with your head pose.

For full SimConnect-based behavior, use FSX on **Windows**: the [Windows guide](windows.md) for LookPilot + opentrack, and opentrack’s [SimConnect protocol documentation](https://mintlify.com/opentrack/opentrack/protocols/simconnect) for SimConnect setup. Steam install paths for the SDK are in opentrack’s [SimConnect FSX SDK for Steam edition](https://github.com/opentrack/opentrack/wiki/SimConnect-FSX-SDK-for-Steam-edition) wiki page.
