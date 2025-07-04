# Communication Settings

This guide explains the different protocols LookPilot uses to communicate tracking data to games, and how to configure them for your system.

## What are Communication Protocols?

Communication protocols are the methods LookPilot uses to send your head tracking data to games. Different games support different protocols, so choosing the right one is essential for compatibility.

## Available Protocols

### Windows Protocols

#### FreeTrack (Recommended)
- **Best for**: Most modern games with head tracking support
- **How it works**: Uses shared memory to communicate with games that support the FreeTrack standard
- **Setup required**: None - works automatically with compatible games
- **Games**: War Thunder, DCS World, Arma 3, Elite Dangerous, and many others

#### SimConnect
- **Best for**: Microsoft Flight Simulator 2020/2024 (only if FreeTrack doesn't work)
- **How it works**: Directly communicates with MSFS through the SimConnect API
- **Setup required**: None - automatically integrates with MSFS
- **Games**: Microsoft Flight Simulator 2020, Microsoft Flight Simulator 2024
- **Note**: Try FreeTrack first - MSFS supports FreeTrack and it usually works better

#### UDP
- **Best for**: Custom applications or games requiring manual network configuration
- **How it works**: Sends tracking data over UDP network protocol
- **Setup required**: Configure IP address and port
- **Configuration**:
  - **IP Address**: Target application's IP (127.0.0.1 for local)
  - **Port**: Target application's port (varies by application)

#### OpenTrack
- **Best for**: Integration with OpenTrack software
- **How it works**: Sends UDP data in OpenTrack format to localhost:4242
- **Setup required**: Configure OpenTrack to receive UDP input
- **Configuration**: Automatically uses 127.0.0.1:4242 (not configurable)

### Linux Protocols

#### FreeTrack (Proton) (Recommended)
- **Best for**: Windows games running through Steam Proton
- **How it works**: Runs FreeTrack protocol inside the Proton environment
- **Setup required**: Configure Steam installation and target game
- **Configuration**:
  - **Steam Installation**: Select your Steam installation directory
  - **Game**: Choose the specific game to run tracking for
- **Requirements**: 
  - Game must be in your Steam library
  - Game must have been launched at least once to create Proton prefix

#### SimConnect (Proton)
- **Best for**: Microsoft Flight Simulator running through Proton (only if FreeTrack doesn't work)
- **How it works**: Runs SimConnect protocol inside the Proton environment
- **Setup required**: Same as FreeTrack (Proton)
- **Configuration**: Same Steam and game selection as FreeTrack (Proton)
- **Note**: Try FreeTrack (Proton) first - MSFS supports FreeTrack and it usually works better

#### UDP
- **Best for**: Native Linux games or applications
- **How it works**: Same as Windows UDP protocol
- **Setup required**: Configure IP address and port for target application

#### OpenTrack
- **Best for**: Native Linux OpenTrack installations
- **How it works**: Same as Windows OpenTrack protocol
- **Setup required**: Configure OpenTrack to receive UDP input

## Configuration Details

### Proton Protocol Setup (Linux Only)

When using FreeTrack (Proton) or SimConnect (Proton):

1. **Steam Installation Selection**:
   - LookPilot automatically detects common Steam installation locations
   - If your Steam is in a custom location, you may need to browse for it
   - Common locations: `~/.steam`, `~/.local/share/Steam`

2. **Game Selection**:
   - Only games in your Steam library that have been launched at least once will appear
   - The game must have a valid Proton prefix (created when first launched)
   - If a game doesn't appear, try launching it through Steam first

3. **How it Works**:
   - LookPilot copies the tracking protocol into the game's Proton prefix
   - The protocol runs inside the Windows compatibility layer
   - Games see it as a native Windows head tracking solution

### UDP Protocol Setup

When using UDP protocol:

1. **IP Address Configuration**:
   - `127.0.0.1` (localhost): For applications running on the same computer
   - Other IP addresses: For applications on other computers (network play)
   - Format: xxx.xxx.xxx.xxx (standard IPv4 format)

2. **Port Configuration**:
   - Must match the port your target application is listening on
   - Common ports: 4242 (OpenTrack), 5000-6000 (custom applications)
   - Valid range: 1-65535

3. **Data Format**:
   - LookPilot sends JSON-formatted tracking data
   - Includes head position (x, y, z) and rotation (yaw, pitch, roll)
   - Eye tracking data included if enabled

## Protocol Selection Guide

### For Windows Users

| Game/Application | Recommended Protocol | Alternative |
|------------------|---------------------|-------------|
| War Thunder | FreeTrack | UDP |
| DCS World | FreeTrack | - |
| Microsoft Flight Simulator | FreeTrack | SimConnect |
| Elite Dangerous | FreeTrack | - |
| Arma 3 | FreeTrack | - |
| OpenTrack | OpenTrack | UDP |
| Custom Applications | UDP | - |

### For Linux Users

| Game/Application | Recommended Protocol | Alternative |
|------------------|---------------------|-------------|
| War Thunder (Proton) | FreeTrack (Proton) | UDP* |
| DCS World (Proton) | FreeTrack (Proton) | - |
| MSFS (Proton) | FreeTrack (Proton) | SimConnect (Proton) |
| Elite Dangerous (Proton) | FreeTrack (Proton) | - |
| Native Linux Games | UDP | - |
| OpenTrack (Native) | OpenTrack | UDP |

*UDP may work for some Proton games but requires additional network configuration

## Troubleshooting

### Windows Issues

**Game doesn't detect head tracking**:
- Verify the game supports FreeTrack/head tracking
- Try restarting the game after starting LookPilot tracking
- Check game settings for head tracking enable options

**SimConnect not working with MSFS**:
- Ensure MSFS is fully updated
- Try restarting both MSFS and LookPilot
- Check Windows firewall isn't blocking the connection

### Linux Issues

**Proton protocol fails to start**:
- Ensure the selected game has been launched at least once through Steam
- Check that Steam is running and logged in
- Verify the game has a valid Proton prefix in `steamapps/compatdata/`

**Game not appearing in list**:
- Launch the game through Steam first to create Proton prefix
- Restart LookPilot to refresh the game list
- Check that the game is actually in your Steam library

**Steam installation not detected**:
- Browse manually for your Steam installation folder
- Ensure Steam is installed in a standard location
- Check permissions on the Steam directory

### General UDP Issues

**Connection refused**:
- Verify the target application is running and listening on the specified port
- Check firewall settings on both sender and receiver
- Ensure IP address and port are correct

**No data received**:
- Confirm LookPilot tracking is started
- Check that the target application supports the data format
- Verify network connectivity between devices (if using remote IP)

For game-specific setup instructions, see the individual [game setup guides](https://lookpilot.app/game-guides). 