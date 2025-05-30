# Setting up LookPilot with DCS World (Windows)

This guide will help you configure LookPilot for an immersive head tracking experience in DCS World on Windows.

## LookPilot Configuration

1.  **Launch LookPilot** and ensure your head tracking device is connected and detected.
2.  In the **Output** tab, select `freetrack 2.0 Enhanced` protocol. This is the most common protocol for DCS World.
3.  Click **Start** to begin tracking.
4.  Go to the **Mapping** tab. It's recommended to adjust sensitivity curves for smooth and responsive movement in the cockpit. Start with default curves and fine-tune as needed.

## DCS World Setup

1.  Ensure LookPilot is running **before** you launch DCS World.
2.  Launch **DCS World**.
3.  Navigate to **Options** (cogwheel icon) → **Controls**.
4.  In the aircraft profile dropdown (e.g., "A-10C II Tank Killer Sim"), select the **Axis Commands** category.
5.  Bind the following head tracking axes:
    *   **View Horizontal** (or similar): Assign to `TrackIR Yaw` (or the equivalent axis LookPilot is sending via freetrack).
    *   **View Vertical** (or similar): Assign to `TrackIR Pitch`.
    *   **View Roll** (or similar, optional): Assign to `TrackIR Roll`.
    *   **View Zoom** (optional): Assign to `TrackIR Z` (for Z-axis translation if you use it).
    *   You may also need to bind **Head-Tracker X, Y, Z** for positional tracking if your device supports it and LookPilot is configured to send these.
6.  Adjust **Axis Tune** for each bound axis if needed (deadzone, saturation, curvature) to fine-tune the response within DCS.

<div class="alert alert-info">
    💡 **Tip:** DCS World often picks up TrackIR/freetrack input automatically once it's running. However, verifying bindings is crucial. Press `Right Ctrl + Enter` in-game to toggle the control input display and check if tracking inputs are being received.
</div>

## Troubleshooting

<div class="troubleshooting-item">
    <h4>No tracking detected in DCS World</h4>
    <ul>
        <li>Ensure LookPilot is started <strong>before</strong> launching DCS World.</li>
        <li>Verify that the <code>freetrack 2.0 Enhanced</code> protocol is selected in LookPilot's Output tab.</li>
        <li>Double-check that head tracking axes are correctly bound in DCS World controls for your specific aircraft module.</li>
        <li>Restart both LookPilot and DCS World.</li>
        <li>Check if other software (like OpenTrack) might be conflicting. Ensure only LookPilot is sending freetrack data.</li>
    </ul>
</div>

<div class="troubleshooting-item">
    <h4>Jittery or unstable movement</h4>
    <ul>
        <li>Increase smoothing values in LookPilot's Mapping tab (e.g., Accela filter).</li>
        <li>Adjust filter settings within LookPilot for your specific tracking source if available.</li>
        <li>Ensure your play area has adequate and consistent lighting if using a webcam.</li>
    </ul>
</div>

<div class="troubleshooting-item">
    <h4>Incorrect range of motion or view feels off</h4>
    <ul>
        <li>Adjust sensitivity curves in LookPilot's Mapping tab. You may need to make pitch and yaw curves asymmetrical.</li>
        <li>Use the **Axis Tune** panel in DCS World controls to modify deadzone, saturation X/Y, and curvature for each head tracking axis.</li>
        <li>Ensure your seating position is consistent and re-center LookPilot if your view drifts.</li>
    </ul>
</div>

---

[← Back to Game Guides](https://guides.lookpilot.app/game-guides.html) | [Home](https://guides.lookpilot.app/index.html) 