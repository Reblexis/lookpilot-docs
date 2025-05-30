---
title: "Windows Setup"
---

# Setting up LookPilot with DCS World (Windows)

## LookPilot Configuration

1. Launch LookPilot and ensure your head tracking device is connected
2. In the **Output** tab, select `freetrack 2.0 Enhanced` protocol
3. Click **Start** to begin tracking
4. Go to the **Mapping** tab to adjust curves for smooth movement

## DCS World Setup

1. Launch DCS World (ensure LookPilot is running first)
2. Go to **Options** → **Controls**
3. Bind the following head tracking axes:
   - **View Horizontal:** TrackIR Yaw
   - **View Vertical:** TrackIR Pitch
   - **View Roll:** TrackIR Roll
   - **View Zoom:** TrackIR Z

> **💡 Tip:** Press `Right Ctrl + Enter` in-game to check tracking status.

## Troubleshooting

### No tracking detected
- Ensure LookPilot is started before DCS
- Check that freetrack 2.0 Enhanced protocol is selected
- Verify head tracking axes are bound in DCS controls

### Jittery movement
- Increase smoothing in LookPilot mapping
- Adjust filter settings in LookPilot

### Incorrect range
- Adjust curves in LookPilot Mapping tab
- Fine-tune using DCS Axis Tune options

---

*Part of the [LookPilot Guides](https://github.com/Reblexis/lookpilot-guides) community project.* 