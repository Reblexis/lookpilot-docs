# Tracking Settings

This guide explains all the tracking settings in LookPilot, including head tracking, eye tracking, and how to fine-tune them for the best experience.

## Head Tracking

Head tracking uses your webcam to track the movement and rotation of your head, translating this into camera movement in games.

### Head Tracking Axes

You can enable or disable individual axes of head movement:

#### Rotation Axes
- **Yaw**: Left and right head movement (looking left/right)
- **Pitch**: Up and down head movement (looking up/down) 
- **Roll**: Head tilting side to side

#### Translation Axes  
- **X**: Left and right head movement (leaning left/right)
- **Y**: Up and down head movement (leaning up/down)
- **Z**: Forward and backward head movement (leaning forward/back)

**Recommendations**:
- **Always enable**: Yaw and Pitch (essential for natural looking around)
- **Usually enable**: Roll (adds immersion for aircraft/vehicles)
- **Optional**: X, Y, Z translation (can be useful for cockpit games but may feel unnatural in some games)

### Head Tracking Settings

#### Smoothness (0.0 - 1.0)
Controls how much filtering is applied to reduce jitter in the tracking data.

- **Lower values (0.0 - 0.3)**: More responsive but potentially jittery
- **Higher values (0.4 - 1.0)**: Smoother but with more latency
- **Recommended**: 0.3 for most users
- **Adjust if**: You experience jitter (increase) or too much lag (decrease)

#### Deadzone (0.0 - 1.0)  
Sets a central area where small movements are ignored to prevent drift.

- **Lower values (0.0 - 0.1)**: More sensitive but may drift when stationary
- **Higher values (0.2 - 0.5)**: Less sensitive but more stable when still
- **Recommended**: 0.1 for most users
- **Adjust if**: You experience drift when sitting still (increase) or tracking feels unresponsive (decrease)

#### Mapping
Advanced response curve configuration for each axis. Click "Mapping" in the head tracking settings to open the mapping editor.

- **Linear mapping**: Output matches input directly (default)
- **Custom curves**: Create non-linear responses for different feel
- **Asymmetric mapping**: Different curves for positive and negative movement
- **Axis inversion**: Flip the direction of an axis

## Eye Tracking

Eye tracking adds an additional layer of control by tracking where you're looking and blending it with head movement.

### Eye Tracking Axes

- **Yaw**: Horizontal eye movement (looking left/right with your eyes)
- **Pitch**: Vertical eye movement (looking up/down with your eyes)

Note: Eye tracking only supports rotation axes, not translation.

### Eye Tracking Settings

#### Smoothness (0.0 - 1.0)
Same concept as head tracking smoothness but for eye movements.

- **Default**: 0.75 (higher than head tracking due to rapid eye movements)
- **Recommended range**: 0.6 - 0.9
- **Adjust if**: Eye tracking feels too jittery (increase) or laggy (decrease)

#### Deadzone (0.0 - 1.0)
Central area where small eye movements are ignored.

- **Default**: 0.2 (higher than head tracking due to natural eye micro-movements)  
- **Recommended range**: 0.1 - 0.3
- **Adjust if**: Eyes feel too sensitive (increase) or unresponsive (decrease)

### Eye Tracking Influence (0.0 - 1.0)
Controls how much eye tracking affects the final camera movement.

- **0.0**: Pure head tracking (eye tracking disabled)
- **0.5**: 50% head tracking, 50% eye tracking
- **1.0**: Pure eye tracking (head tracking disabled for rotation)
- **Recommended**: 0.2 - 0.4 for most users
- **Use cases**:
  - **0.1 - 0.3**: Subtle eye tracking enhancement
  - **0.4 - 0.6**: Balanced head and eye tracking
  - **0.7 - 1.0**: Eye-dominant tracking (advanced users only)

## Advanced Features

### TrueView
When enabled, movement directions stay relative to your view orientation even after rotation mapping.

- **Enabled**: Natural movement regardless of in-game camera rotation
- **Disabled**: Movement is always relative to the original orientation
- **Recommended**: Enabled for most users
- **Disable if**: You prefer traditional head tracking behavior

### Mapping Curves

Click "Mapping" in either head or eye tracking settings to open the advanced curve editor.

#### Curve Types
- **Linear**: Direct 1:1 mapping (default)
- **Exponential**: Slow near center, fast at extremes
- **Logarithmic**: Fast near center, slow at extremes
- **S-Curve**: Slow at center and extremes, fast in middle

#### Curve Editing
- **Left click**: Add or move control points
- **Right click**: Remove control points
- **Asymmetric**: Enable to create different curves for positive/negative movement
- **Invert**: Flip the direction of the axis

#### Common Curve Setups
- **Precision aiming**: Slower response near center for fine control
- **Fast scanning**: Faster response for quick camera movement
- **Dead zone**: Flat area at center to prevent small movements

### Centering
Press the "Center" button or use the keybind (default: Ctrl+Space) to set your current position as the neutral center point.

**When to center**:
- After adjusting your seating position
- When starting a new gaming session
- If tracking feels offset from where you're looking
- After changing head tracking settings

## Optimal Settings by Use Case

### General Gaming
- **Head**: Yaw ✓, Pitch ✓, Roll ✓, X/Y/Z ✗
- **Smoothness**: 0.3 (head), 0.75 (eye)
- **Deadzone**: 0.1 (head), 0.2 (eye)
- **Eye Influence**: 0.0 - 0.2

### Flight Simulation
- **Head**: All axes enabled
- **Smoothness**: 0.2 - 0.4 (more responsive for precise control)
- **Deadzone**: 0.05 - 0.1 (lower for precision)
- **Eye Influence**: 0.1 - 0.3

### Racing Games
- **Head**: Yaw ✓, Pitch ✓, Roll ✓, X ✓ (lean into turns), Y/Z ✗
- **Smoothness**: 0.4 - 0.5 (smoother for racing)
- **Deadzone**: 0.1 - 0.15
- **Eye Influence**: 0.0 - 0.1

### First-Person Shooters
- **Head**: Yaw ✓, Pitch ✓, Roll ✗, X/Y/Z ✗
- **Smoothness**: 0.2 - 0.3 (responsive for quick aiming)
- **Deadzone**: 0.05 - 0.1 (low for precision)
- **Eye Influence**: 0.2 - 0.4 (eye tracking useful for target acquisition)

## Troubleshooting

### Tracking feels unresponsive
- Decrease smoothness values
- Decrease deadzone values
- Check camera positioning and lighting
- Ensure good contrast between your face and background

### Tracking is too jittery
- Increase smoothness values
- Improve lighting conditions
- Stabilize camera mounting
- Consider using a higher resolution

### Tracking drifts over time
- Increase deadzone values
- Ensure consistent lighting
- Check for reflections or background movement
- Press Center to reset neutral position

### Eye tracking not working well
- Ensure good lighting on your face
- Position camera at eye level
- Increase eye tracking smoothness
- Lower eye tracking influence
- Consider that eye tracking works best with good quality cameras

### Movements feel backwards
- Use the "Invert" option in mapping settings for affected axes
- Check that TrueView is configured correctly
- Verify game-specific settings aren't also inverting controls

For game-specific tracking recommendations, see the individual [game setup guides](https://lookpilot.app/game-guides). 