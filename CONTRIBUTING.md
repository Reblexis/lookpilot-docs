# Contributing to LookPilot Guides

Thanks for helping expand LookPilot support! Our system is designed to be **super simple** - no manual configuration needed!

## 🚀 Quick Start (3 Steps!)

### 1. Create the Directory Structure
```
docs/game-guides/[game-name-in-kebab-case]/
```

**Examples:**
- `docs/game-guides/cyberpunk-2077/`
- `docs/game-guides/war-thunder/`
- `docs/game-guides/assetto-corsa-competizione/`

### 2. Create Platform Files
Create markdown files named after the platform:
- `windows.md` for Windows guides
- `linux.md` for Linux guides
- `macos.md` for macOS guides (if needed)

### 3. Use the Template
Copy `templates/game-guide-template.md` and fill in the placeholders!

## ✨ Auto-Magic Features

Our system automatically:
- **Converts directory names** to proper titles
  - `counter-strike-2` → "Counter Strike 2"
  - `microsoft-flight-simulator-2020` → "Microsoft Flight Simulator 2020"
- **Converts file names** to platform labels
  - `windows.md` → "Windows"
  - `linux.md` → "Linux"
- **Generates sidebar navigation** - no manual configuration needed!
- **Handles all formatting** - just focus on content!

## 📁 Example Structure

```
docs/game-guides/
├── cyberpunk-2077/
│   ├── windows.md
│   └── linux.md
├── war-thunder/
│   ├── windows.md
│   └── linux.md
└── assetto-corsa-competizione/
    └── windows.md
```

This automatically creates:
```
📁 Game Guides
  📁 Assetto Corsa Competizione
    └── Windows
  📁 Cyberpunk 2077
    ├── Linux
    └── Windows  
  📁 War Thunder
    ├── Linux
    └── Windows
```

## 🎯 Writing Guidelines

- **Keep it simple** - max 10 steps per section
- **Be specific** - include exact menu paths
- **Test everything** - only include verified steps
- **Use the template** - it has all the right sections

## 🔧 No Configuration Needed!

Unlike other documentation systems, you don't need:
- ❌ Frontmatter in markdown files
- ❌ `_category_.json` files
- ❌ Manual sidebar configuration
- ❌ Complex setup

Just create the files and our system handles the rest! 🎉

## 📝 Template Placeholders

When using the template, replace:
- `[GAME NAME]` → Actual game name
- `[PLATFORM]` → Windows/Linux/macOS
- `[PROTOCOL]` → freetrack 2.0 Enhanced, SimConnect, Mouse emulation, etc.
- `[GAME TYPE]` → flight simulation, competitive gaming, racing, etc.
- `[Menu Path]` → Exact menu navigation path

## 🤝 Need Help?

- Check existing guides for examples
- Open an issue if you're stuck
- The template has helpful comments

**Happy contributing!** 🚀 