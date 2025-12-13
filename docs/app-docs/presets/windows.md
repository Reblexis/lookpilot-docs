Presets are saved configurations that store all your tracking and communication settings in one place. They allow you to quickly switch between different setups for different games or use cases.

## Types of Presets

LookPilot offers two types of presets:

- **Local Presets**: Your personal configurations stored on your device. You have full control to create, modify, and manage them.
- **Community Presets**: Configurations shared by other users. These are read-only until you save them as your own local preset.

## What's Stored in a Preset

Each preset contains:

- **Communication protocol settings**: Protocol type (FreeTrack, Virtual Joystick, opentrack, etc.) and configuration
- **Head tracking settings**: Which axes are enabled, mapping curves, per-axis sensitivity/smoothness/deadzone multipliers
- **Eye tracking settings**: Which axes are enabled, mapping curves, per-axis sensitivity/smoothness/deadzone multipliers
- **Rotation and movement sensitivity**: Global sensitivity multipliers for rotation and translation
- **TrueView setting**: Whether TrueView is enabled
- **Optional keybind**: Keyboard shortcut to quickly switch to this preset

**Note**: Center position and rotation are **not** stored in presets, as these are device-specific and depend on your physical setup.

## Accessing Presets

1. In the **Gaming** tab, click the preset button (displays the current preset name)
2. Click to open the **Preset Management** window with:
   - **Search field**: Filter presets by name, author, or game
   - **+ button**: Create new local preset
   - **Globe icon**: Toggle to show/hide community presets
   - **Refresh button**: Reload community presets from the database
   - **Preset list**: All available presets

## Local Presets

### Creating a New Preset

1. Click the **+** button in the Preset Management window
2. Enter a name for your preset
3. Choose how to initialize the settings:
   - **From preset**: Copy settings from an existing preset (local or community)
   - **Default settings**: Start with the application's default configuration
   - **From file**: Import settings from a preset JSON file
4. The new preset is created and automatically selected

### Managing Local Presets

**Switching Presets**: Click any preset to switch to it immediately. The current preset is highlighted with a blue border.

**Options Menu** (⋯ button):
- **Set Keybind**: Assign a keyboard shortcut to quickly switch to this preset
- **Rename**: Change the preset name
- **Share**: Upload the preset to the community database
- **Reset**: Reset the preset to default settings
- **Delete**: Remove the preset permanently

The **Default** preset cannot be deleted or renamed, but you can modify its settings.

### Sharing to Community

The Share option uploads your preset to the community database where other users can discover and use it:

1. Click the options button (⋯) on a local preset
2. Select **Share**
3. If this is your first time sharing, you'll be prompted to set a display name
4. Fill in the upload form:
   - **Name**: Preset name (pre-filled)
   - **Description**: Explain what makes this preset useful
   - **Tags**: Add descriptive tags (e.g., "smooth", "high-sensitivity", "racing")
   - **Games**: List compatible games (e.g., "DCS World", "MSFS 2020")
5. Click **Upload**

**Note**: After uploading, you cannot edit the preset's tracking settings. Metadata (name, description, tags, games) can be edited if you're the author. Preset files are stored locally in `%LOCALAPPDATA%\Lookpilot\presets\` and can be manually backed up or shared as JSON files.

### Importing from File

If someone shares a preset JSON file with you externally:

1. Click the **+** button to create a new preset
2. Select **From file** in the load settings dropdown
3. Browse to the JSON file
4. Enter a name for the preset
5. The preset will be created with those settings

## Community Presets

Community presets allow you to discover and use configurations created by other LookPilot users.

### Accessing and Browsing

1. In the Preset Management window, click the **globe icon** (community toggle)
2. Community presets load and appear below your local presets
3. **Search**: Filter by preset name, author name, or game
4. **Sorting**: Your liked presets appear first, then by like count
5. **Metadata**: Hover to see author, description, tags, games, likes, and downloads

### Using a Community Preset

1. Click on a community preset to apply it
2. The preset button in the Gaming tab shows the name with **(Community)** suffix
3. A local copy is automatically created and stored on your device
4. Click the **heart icon** to like/unlike presets (liked presets appear at the top)

### Modifying Community Presets

When you use a community preset, you can freely modify its settings:

1. Any changes you make are automatically saved to your local copy
2. Your modifications don't affect the original community preset
3. The preset remains marked as **(Community)** even after modifications
4. Use the **Reinstall** option (see below) to reset to the original settings if needed

### Reinstalling Community Presets

When you download and use a community preset, a local copy is created. If you modify settings, those changes are stored locally:

1. Click the options button (⋯) on the community preset
2. Select **Reinstall**
3. The preset is reset to the original settings from the community database

This is useful if you've made experimental changes and want to return to the original configuration.

## Preset Keybinds

Keybinds work for both local and community presets, allowing instant preset switching.

### Setting a Keybind

1. Open the Preset Management window
2. Click the options button (⋯) for any preset
3. Click in the keybind field (shows "None" if not set)
4. Press the key combination you want to use (e.g., `Ctrl+Alt+1`)
5. The keybind is saved automatically

### Using Keybinds

- Press your assigned key combination while LookPilot is running
- The preset switches immediately, even if the main window is minimized
- If tracking is active and the new preset has different communication settings, tracking stops automatically

**Best Practices**:
- Use modifier keys (Ctrl, Alt, Shift) to avoid conflicts with games
- Choose logical combinations (e.g., `Ctrl+Alt+F` for a flight sim preset)
- Avoid common game hotkeys

## Best Practices

### Backup and Organization

- Preset files are stored in `%LOCALAPPDATA%\Lookpilot\presets\` and can be manually copied for backup
- Share important presets to the community as an additional backup
- Use descriptive names: "Flight Sim - High Sensitivity", "Racing - Smooth", "DCS World"
- Create a copy before making experimental changes

### Community Etiquette

When sharing to the community:
- Write clear descriptions explaining what games it's for and what makes it unique
- Use appropriate tags to help others find your preset
- List compatible games you've tested
- Test thoroughly before sharing

## Support

For additional help:
- Join our [Discord community](https://discord.gg/RbhTxhFnCF)
- Visit [game-specific guides](https://lookpilot.app/game-guides)
- Contact support: support@lookpilot.app
