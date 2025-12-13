## Where to Find Tracking Settings

Click the **Settings** button (gear icon) in the output pose visualization in the Gaming tab to open the Tracking settings window.

## Window Structure

The Tracking settings window contains multiple tabs:

- **General**: Protocol settings, visualizations, axis toggles, and global settings
- Individual axis tabs (Yaw, Pitch, Roll, X, Y, Z for head; Yaw, Pitch for eye) - only visible when that axis is enabled

## General Tab

The General tab contains protocol settings at the top, followed by visualizations and global tracking controls.

### Protocol Settings

**Protocol**: Select the communication protocol to send tracking data to the game. See the [Connect to Any Game](https://lookpilot.app/guides/connect-to-any-game) guide for details on protocols and their settings.

### Visualizations

Two side-by-side 3D visualizations show:
- **Input visualization** (left): Tracking data after smoothing and centering, but before mapping curves are applied
- **Output visualization** (right): Final output after mapping curves are applied

### Axis Toggles

Enable or disable individual tracking axes. Each enabled axis gets its own tab for detailed configuration.

**Head axes**:
- **Yaw**: Left/right head rotation - Essential for all games
- **Pitch**: Up/down head rotation - Essential for all games
- **Roll**: Head tilting left/right - Adds immersion, particularly in flight/racing
- **X**: Left/right head movement (leaning) - Useful in cockpit games for looking around panels
- **Y**: Up/down head movement (leaning) - Useful in cockpit games
- **Z**: Forward/backward head movement (leaning) - Useful in cockpit games for reading instruments

**Eye axes**:
- **Yaw**: Left/right eye movement - Adds precision for target acquisition
- **Pitch**: Up/down eye movement - Adds precision for target acquisition

### Global Settings

These settings apply to all axes as a base value:

**Rotation sensitivity** (0.1 - 5.0): Global sensitivity multiplier for rotation axes (Yaw, Pitch, Roll) for both head and eye tracking. Increase for larger displays or if you prefer smaller head movements.

**Movement sensitivity** (0.1 - 5.0): Global sensitivity multiplier for movement axes (X, Y, Z) for head tracking. Adjust based on how much physical leaning you want to translate to in-game movement.

**Smoothness** (0.0 - 3.0): Global smoothing amount applied to both head and eye tracking. Higher values reduce jitter but add latency. Increase if tracking feels jittery, decrease if it feels sluggish.

**Deadzone** (0.0 - 3.0): Global deadzone amount applied to both head and eye tracking. Creates a zone where small movements are ignored, preventing drift when sitting still. Increase if camera drifts, decrease if tracking feels unresponsive.

**Confidence threshold** (0.0 - 1.0): Minimum tracking confidence score required before the tracking search region resets. Lower values allow tracking in poor lighting or with lower quality cameras but may be less accurate. Increase for more stable tracking in good conditions.

**TrueView**: Maintains physical movement directions relative to your current view orientation, even when using non-linear rotation mapping curves. Keep enabled unless you prefer traditional head tracking behavior.

## Individual Axis Tabs

Each enabled axis has its own tab with axis-specific controls. These tabs only appear when the axis is enabled in the General tab.

### Visualization

Shows real-time input and output for this specific axis, helping you see the effect of your settings.

### Axis-Specific Settings

**Maps to** (Virtual joystick only): Select which joystick axis this tracking axis should control (Left Stick X/Y, Right Stick X/Y, Triggers, or None). A red indicator appears if multiple tracking axes map to the same joystick axis.

**Sensitivity** (0.1 - 5.0): Per-axis sensitivity multiplier applied after the global rotation or movement sensitivity. Final sensitivity = Global sensitivity × Axis sensitivity. When changed, automatically scales the mapping curve heights proportionally, preserving the curve shape. Adjust individual axes if one feels too fast/slow relative to others.

**Offset** (-180 to 180 for rotation, -300 to 300 for movement, -1 to 1 for joystick): Adds a constant value to the final mapped output, shifting the neutral position. Useful if your camera is mounted off-center or you sit at an angle.

**Max input**: Sets the maximum input range for the horizontal axis of the mapping curve. Higher values mean you need larger head movements to reach the curve's edge. Decrease if you have limited head mobility or prefer smaller movements.

**Smoothness** (0.0 - 1.0): Per-axis smoothing multiplier. Final smoothness = Global smoothness × Axis smoothness. Adjust if one axis is jitterier than others (increase) or needs more responsiveness (decrease).

**Deadzone** (0.0 - 1.0): Per-axis deadzone multiplier. Final deadzone = Global deadzone × Axis deadzone. Adjust if one axis drifts more than others (increase) or feels less responsive (decrease).

### Mapping Curves

The mapping curve defines how input values (your head/eye movement) translate to output values (in-game camera movement). 

**Positive curve**: Maps positive movements (right, up, forward, clockwise)
**Negative curve**: Maps negative movements (left, down, backward, counterclockwise) - editable only when Asymmetric is enabled

#### Curve Controls

**Inverted**: Flips the direction of the input axis (e.g., looking left moves camera right). Use if the game has inverted controls or you prefer reversed movement.

**Asymmetric**: When enabled, the negative curve can be edited independently from the positive curve, allowing different response curves for each direction. Useful when you need different behavior in each direction (e.g., looking down vs up in flight sims).

#### Editing Curves

- **Left click**: Add or move control points on the curve
- **Right click**: Remove control points
- The curve determines the response: steep = fast response, flat = slow response
- Linear (straight diagonal) = 1:1 mapping
- Exponential (curved up) = slow near center, fast at extremes  
- Logarithmic (curved down) = fast near center, slow at extremes

#### Common Curve Setups

- **Default (Linear)**: Straight diagonal line, natural 1:1 response
- **Precision mode**: Flatter near center for fine control, steeper at edges for quick turns
- **Fast scanning**: Steeper curve throughout for quicker camera movement
- **Reduced range**: Lower max output to limit how far the camera can turn

## How Settings Interact

The processing pipeline in order:

1. **Raw tracking input** from camera →
2. **Smoothing & Deadzone** - applied before everything else →
3. **Centering** - subtract center position/rotation set when you press Center →
4. **Inversions** - flip axis direction if enabled →
5. **Mapping curves & Sensitivity** - transform through spline (sensitivity scales curve heights proportionally) →
6. **Offset** - constant added to final mapped output →
7. **Combine head + eye** - simple addition of head and eye rotations →
8. **TrueView** (if enabled) - rotates translation directions to match your current view orientation →
9. **Send to game**

Key formula interactions:
- **Final smoothness** = Global smoothness × Axis smoothness multiplier
- **Final deadzone** = Global deadzone × Axis deadzone multiplier  
- **Final sensitivity** = Global sensitivity (rotation/movement) × Axis sensitivity
- **Combined rotation** = Head rotation (after mapping) + Eye rotation (after mapping)

## Quick Start Recommendations

**General use**:
- Enable: Yaw, Pitch for head; optionally Roll
- Global smoothness: 0.3
- Global deadzone: 0.1
- Keep curves at default (linear)
- Adjust per-axis sensitivity if specific axes feel too fast/slow

**Flight simulation**:
- Enable: All head axes (Yaw, Pitch, Roll, X, Y, Z)
- Global smoothness: 0.2-0.4
- Global deadzone: 0.05-0.1
- Consider asymmetric curves for more precise control in specific directions

**Racing**:
- Enable: Yaw, Pitch, Roll, X for leaning into turns
- Global smoothness: 0.4-0.5
- Consider higher deadzone (0.15) for stability

**First-person shooters**:
- Enable: Only Yaw and Pitch for head
- Global smoothness: 0.2-0.3
- Global deadzone: 0.05-0.1
- Consider adding eye tracking (influence 0.2-0.4) for target acquisition
