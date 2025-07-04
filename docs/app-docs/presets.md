# Presets

Presets are saved configurations that store all your tracking and communication settings in one place. They allow you to quickly switch between different setups for different games or use cases.

## What's Stored in a Preset

Each preset contains:
- **Communication settings**: Protocol selection and configuration
- **Head tracking settings**: Which axes are enabled, smoothness, deadzone, and mapping curves
- **Eye tracking settings**: Which axes are enabled, smoothness, deadzone, and mapping curves  
- **Eye tracking influence**: How much eye movement affects the final tracking output
- **TrueView setting**: Whether TrueView is enabled
- **Keybind**: Optional keyboard shortcut to switch to this preset

## Managing Presets

### Viewing and Switching Presets

1. In the Gaming tab, click the preset name button (shows current preset)
2. This opens the Presets window showing all available presets
3. Click any preset to switch to it immediately
4. The current preset is highlighted with a blue border

### Creating New Presets

1. In the Presets window, click the "+" button
2. Enter a name for your preset
3. Choose how to initialize the settings:
   - **From preset**: Copy settings from an existing preset
   - **Default settings**: Start with the application's default configuration
   - **From file**: Import settings from a previously exported preset file

### Preset Options

For any preset except "Default", click the options button (⋯) to access:

- **Set Keybind**: Assign a keyboard shortcut to quickly switch to this preset
- **Rename**: Change the preset name
- **Share**: Export the preset as a JSON file that others can import
- **Delete**: Remove the preset permanently

### The Default Preset

- The "Default" preset cannot be deleted or renamed
- It serves as a fallback and starting point for new presets
- You can modify its settings, but it will always exist

## Quick Switching with Keybinds

### Setting Up Preset Keybinds

1. Click the options button for any preset
2. Click in the keybind area (shows "None" if no keybind is set)
3. Press the key combination you want to use
4. The keybind is saved automatically

### Using Preset Keybinds

- Press your assigned key combination while LookPilot is running
- The preset will switch immediately, even if the main window is minimized
- If tracking is active and communication settings would change, tracking stops automatically

## Organization Tips

### Naming Conventions

Consider organizing presets by:
- **Game type**: "Flight Sim", "Racing", "FPS"
- **Specific games**: "DCS World", "MSFS 2020", "Elite Dangerous"
- **Use case**: "Precise", "Smooth", "High Sensitivity"

### Preset Hierarchy

- Start with the Default preset as your baseline
- Create game-specific presets by copying and modifying existing ones
- Use descriptive names that make the preset's purpose clear

## Import and Export

### Sharing Presets

1. Click the Share option for any preset
2. Choose where to save the JSON file
3. Others can import this file when creating a new preset

### Importing Presets

1. When creating a new preset, select "From file"
2. Browse to the exported JSON file
3. The preset will be created with those settings

## Best Practices

### Backup Important Presets

- Export presets you've spent time fine-tuning
- Store them in a safe location as backup files
- This protects against accidental deletion or corruption

### Testing Changes

- Always test new settings before overwriting an existing preset
- Create a copy first if you're unsure about changes
- The Default preset provides a safe fallback option

### Keybind Management

- Use logical key combinations that don't conflict with games
- Consider using modifier keys (Ctrl, Alt, Shift) to avoid conflicts
- Document your keybinds if you have many presets

## Troubleshooting

If presets aren't working correctly:

1. **Preset won't switch**: Check if tracking is active - some changes require stopping tracking first
2. **Settings not saving**: Ensure you have write permissions to the LookPilot data folder
3. **Keybind not working**: Verify the key combination isn't blocked by other applications
4. **Import fails**: Check that the JSON file is a valid LookPilot preset export

For additional support, contact: support@lookpilot.app 