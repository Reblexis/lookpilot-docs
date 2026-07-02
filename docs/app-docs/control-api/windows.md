> **Availability**: the control API ships in the next LookPilot release (after 1.9.17). If the discovery file described below does not appear when the app runs, your version does not have it yet; update LookPilot.

LookPilot runs a local control API that lets external tools trigger tracker actions: Stream Deck buttons, AutoHotkey scripts, voice command tools like VoiceAttack, or anything that can make an HTTP request. The in-app hotkeys keep working; the control API is an addition, not a replacement.

## Available Actions

| Action | What it does |
|---|---|
| `center` | Center tracking (same as the in-app Center hotkey) |
| `toggle` | Start / stop tracking |
| `pause` | Pause tracking (freezes the view at the current pose) |
| `set-game-center` | Save the current pose as the game-center offset |
| `status` | Get tracking state as JSON |
| `ping` | Check that LookPilot is running |

## How It Works

On startup LookPilot writes a discovery file at `%APPDATA%\lookpilot\control.json` containing the API port and an access token:

```json
{"app": "LookPilot", "port": 41417, "token": "<random per app start>"}
```

Any tool can read that file and call the API on `127.0.0.1`. PowerShell example:

```powershell
$c = Get-Content "$env:APPDATA\lookpilot\control.json" | ConvertFrom-Json
Invoke-RestMethod -Method Post -Uri "http://127.0.0.1:$($c.port)/api/center" -Headers @{Authorization = "Bearer $($c.token)"}
```

Endpoints: `POST /api/center`, `POST /api/toggle`, `POST /api/pause`, `POST /api/set-game-center`, `GET /api/status`, `GET /api/ping` (ping needs no token). The token can also be passed as a `?token=` query parameter, which is handy for tools that only let you configure a URL.

The API only listens on `127.0.0.1` (your own machine) and every request except `ping` needs the token, so nothing on your network can control the tracker.

## Stream Deck

Use any "HTTP request" / "API request" plugin from the Stream Deck store:

1. Read the port and token from `%APPDATA%\lookpilot\control.json` (open it in Notepad).
2. Configure the button URL as `http://127.0.0.1:<port>/api/center?token=<token>` with method POST.

Note that the token changes each time LookPilot starts. For a set-and-forget setup, point the button at a small PowerShell script (saved as a `.ps1` file with the snippet above) instead of a raw URL, so the token is read fresh on every press.

## AutoHotkey

```autohotkey
; Ctrl+Alt+C centers tracking
^!c::
    Run, powershell -WindowStyle Hidden -Command "$c = Get-Content \"$env:APPDATA\lookpilot\control.json\" | ConvertFrom-Json; Invoke-RestMethod -Method Post -Uri \"http://127.0.0.1:$($c.port)/api/center\" -Headers @{Authorization = \"Bearer $($c.token)\"}",, Hide
    return
```

## Notes

- The token changes on every app start, so always read it from the file rather than hardcoding it.
- To turn the control API off entirely, launch LookPilot with the environment variable `LOOKPILOT_CONTROL_DISABLED=1`.
- If a request fails with connection refused, LookPilot is not running (the discovery file is only valid while the app runs).
