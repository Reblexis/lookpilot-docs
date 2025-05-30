# Contributing to LookPilot Guides

Thanks for helping expand LookPilot support! This guide explains how to contribute new game guides using standard Docusaurus practices.

## 🚀 Quick Start (4 Steps!)

### 1. Create the Directory Structure
```
docs/game-guides/[game-name-in-kebab-case]/
```

**Examples:**
- `docs/game-guides/cyberpunk-2077/`
- `docs/game-guides/war-thunder/`
- `docs/game-guides/assetto-corsa-competizione/`

### 2. Create the Category File
Add a `_category_.json` file in your game directory:
```json
{
  "label": "Your Game Name"
}
```

**Examples:**
- `{"label": "Cyberpunk 2077"}`
- `{"label": "War Thunder"}`
- `{"label": "Assetto Corsa Competizione"}`

### 3. Create Platform Files
Create markdown files with proper frontmatter:

**For Windows guides** (`windows.md`):
```markdown
---
sidebar_label: "Windows"
---

# Setting up LookPilot with [Game Name] (Windows)
```

**For Linux guides** (`linux.md`):
```markdown
---
sidebar_label: "Linux"
---

# Setting up LookPilot with [Game Name] (Linux)
```

### 4. Use the Template
Copy `templates/game-guide-template.md` and fill in the placeholders!

## 📁 Example Structure

```
docs/game-guides/
├── cyberpunk-2077/
│   ├── _category_.json          # {"label": "Cyberpunk 2077"}
│   ├── windows.md              # sidebar_label: "Windows"
│   └── linux.md                # sidebar_label: "Linux"
├── war-thunder/
│   ├── _category_.json          # {"label": "War Thunder"}
│   ├── windows.md              # sidebar_label: "Windows"
│   └── linux.md                # sidebar_label: "Linux"
└── assetto-corsa-competizione/
    ├── _category_.json          # {"label": "Assetto Corsa Competizione"}
    └── windows.md              # sidebar_label: "Windows"
```

This creates a clean sidebar structure:
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

## 🔧 Standard Docusaurus Approach

We use the standard Docusaurus configuration system:

### Required Files:
- ✅ `_category_.json` - Controls game name in sidebar
- ✅ `sidebar_label` frontmatter - Controls platform name in sidebar
- ✅ Proper directory structure - Enables autogeneration

### Benefits:
- **Precise control** over all labels and naming
- **Professional appearance** with proper capitalization
- **Consistent with Docusaurus best practices**
- **Easy to maintain** and understand

## 📝 Template Placeholders

When using the template, replace:
- `[GAME NAME]` → Actual game name
- `[PLATFORM]` → Windows/Linux/macOS
- `[PROTOCOL]` → freetrack 2.0 Enhanced, SimConnect, Mouse emulation, etc.
- `[GAME TYPE]` → flight simulation, competitive gaming, racing, etc.
- `[Menu Path]` → Exact menu navigation path

## 🤝 Need Help?

- Check existing guides for examples
- Look at the `_category_.json` files in existing game directories
- Open an issue if you're stuck
- The template has helpful comments

**Happy contributing!** 🚀 