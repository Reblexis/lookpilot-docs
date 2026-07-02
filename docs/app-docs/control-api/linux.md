> **Availability**: the control API ships in the next LookPilot release (after 1.9.17). If the discovery file described below does not appear when the app runs, your version does not have it yet; update LookPilot.

LookPilot runs a local control API that lets you trigger tracker actions from outside the app: your window manager or desktop environment keybinds, shell scripts, or any tool that can make an HTTP request. This is the recommended way to set up keybinds on Linux, especially on Wayland, where applications cannot reliably capture global hotkeys themselves. Your WM or DE can always run a command on a keypress, and that command can tell LookPilot what to do.

## Available Actions

| Action | What it does |
|---|---|
| `center` | Center tracking (same as the in-app Center hotkey) |
| `toggle` | Start / stop tracking |
| `pause` | Pause tracking (freezes the view at the current pose) |
| `set-game-center` | Save the current pose as the game-center offset |
| `status` | Print tracking state as JSON |
| `ping` | Check that LookPilot is running |

The actions behave exactly like pressing the matching in-app hotkey. The in-app hotkeys keep working; the control API is an addition, not a replacement.

## Quick Start with lookpilotctl

The `lookpilotctl` helper script ships with LookPilot in the `scripts/` folder of the install directory. It needs only Python 3, which every modern distribution ships. Copy it somewhere on your `PATH`:

```bash
cp "$HOME/.steam/root/steamapps/common/LookPilot/scripts/lookpilotctl" ~/.local/bin/
chmod +x ~/.local/bin/lookpilotctl
```

Test it while LookPilot is running:

```bash
lookpilotctl ping
lookpilotctl center
```

## Binding Keys in Your WM / DE

Use your normal keybind configuration and run `lookpilotctl <action>`.

**i3 / sway** (`~/.config/i3/config` or `~/.config/sway/config`):

```
bindsym $mod+c exec lookpilotctl center
bindsym $mod+t exec lookpilotctl toggle
bindsym $mod+p exec lookpilotctl pause
```

**Hyprland** (`~/.config/hypr/hyprland.conf`):

```
bind = $mainMod, C, exec, lookpilotctl center
bind = $mainMod, T, exec, lookpilotctl toggle
bind = $mainMod, P, exec, lookpilotctl pause
```

**KDE Plasma**: System Settings -> Shortcuts -> Custom Shortcuts -> add a command shortcut running `lookpilotctl center`.

**GNOME**: Settings -> Keyboard -> Keyboard Shortcuts -> Custom Shortcuts -> add a shortcut with command `lookpilotctl center`.

## How It Works (curl, scripts, other tools)

On startup LookPilot writes a discovery file at `~/.config/lookpilot/control.json` containing the API port and an access token:

```json
{"app": "LookPilot", "port": 41417, "token": "<random per app start>"}
```

Any tool can read that file and call the API on `127.0.0.1`:

```bash
PORT=$(python3 -c "import json;print(json.load(open('$HOME/.config/lookpilot/control.json'))['port'])")
TOKEN=$(python3 -c "import json;print(json.load(open('$HOME/.config/lookpilot/control.json'))['token'])")
curl -X POST -H "Authorization: Bearer $TOKEN" "http://127.0.0.1:$PORT/api/center"
```

Endpoints: `POST /api/center`, `POST /api/toggle`, `POST /api/pause`, `POST /api/set-game-center`, `GET /api/status`, `GET /api/ping` (ping needs no token). The token can also be passed as a `?token=` query parameter.

The API only listens on `127.0.0.1` (your own machine) and every request except `ping` needs the token, so nothing on your network can control the tracker.

## Notes

- Works with LookPilot installed through Steam, including when it runs inside the Steam Linux Runtime container: the port and the discovery file are both reachable from your normal session.
- If you run Steam as a Flatpak, the discovery file is at `~/.var/app/com.valvesoftware.Steam/config/lookpilot/control.json` instead. `lookpilotctl` checks both locations automatically.
- The token changes on every app start, so always read it from the file rather than hardcoding it.
- To turn the control API off entirely, launch LookPilot with the environment variable `LOOKPILOT_CONTROL_DISABLED=1`.

## Troubleshooting

- `lookpilotctl: LookPilot is not running`: start LookPilot first; the discovery file only exists while the app runs.
- Keybind does nothing but `lookpilotctl center` works in a terminal: your WM may run `exec` commands with a minimal `PATH`. Use the full path to the script in the keybind, e.g. `exec ~/.local/bin/lookpilotctl center`.
- `LookPilot is not responding (stale control.json?)`: the app quit without cleaning up (e.g. it crashed). Restart LookPilot; the file is rewritten on every start.
