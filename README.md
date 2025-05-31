# LookPilot Documentation

Official documentation repository for LookPilot head and eye tracking software. This repository contains all user guides, setup instructions, and troubleshooting documentation that powers the [LookPilot website](https://lookpilot.app).

## 📚 What's in this Repository

This repository contains comprehensive Markdown-based documentation for LookPilot:

### Application Documentation (`docs/app-docs/`)
- **Installation Guide**: Step-by-step installation instructions
- **Configuration Guide**: How to configure LookPilot for optimal performance
- **Troubleshooting Guide**: Common issues and solutions
- **App Overview**: Complete walkthrough of the LookPilot interface

### Game Setup Guides (`docs/game-docs/`)
Platform-specific setup instructions for popular games:
- **DCS World** (Windows)
- **IL-2 Sturmovik** (Windows)
- **Microsoft Flight Simulator 2020** (Windows)
- **Elite Dangerous** (Windows)
- **Counter-Strike 2** (Linux)

Each game guide includes:
- LookPilot configuration steps
- In-game setup instructions
- Troubleshooting tips
- Platform-specific considerations

## 🤝 How to Contribute

We welcome community contributions! Here's how you can help improve LookPilot documentation:

### Adding a New Game Guide

1. **Fork this repository**
2. **Create a new directory** under `docs/game-docs/your-game-name/`
3. **Add required files**:
   - `manifest.json` - Game metadata (name, category, platforms, etc.)
   - `windows.md` and/or `linux.md` - Platform-specific guides
4. **Follow the guide structure**:
   - LookPilot Configuration section
   - Game Setup section
   - Troubleshooting section
5. **Update `docs/index.json`** to include your new game
6. **Test your guide** with LookPilot
7. **Submit a pull request**

### Improving Existing Documentation

1. **Fork this repository**
2. **Edit the relevant Markdown files**
3. **Test your changes** if possible
4. **Submit a pull request** with a clear description

### Content Guidelines

- **Be clear and concise**: Use simple language and step-by-step instructions
- **Include screenshots**: When helpful for complex UI interactions
- **Test thoroughly**: Ensure all steps work as described
- **Use consistent formatting**: Follow existing Markdown structure
- **Platform-specific**: Clearly indicate Windows/Linux differences

### File Structure

```
docs/
├── app-docs/
│   ├── app-overview/
│   │   ├── manifest.json
│   │   └── guide.md
│   └── [other-app-guides]/
├── game-docs/
│   ├── game-name/
│   │   ├── manifest.json
│   │   ├── windows.md
│   │   └── linux.md
│   └── [other-games]/
└── index.json
```

## 🔧 Technical Details

- **Format**: Markdown with JSON manifests
- **Integration**: Automatically loaded by the LookPilot website
- **Rendering**: Supports code blocks, alerts, and standard Markdown
- **Platform Support**: Windows and Linux guides

## 🎯 Priority Contributions

We're especially looking for guides for these popular games:
- **Cyberpunk 2077**
- **Star Citizen**
- **War Thunder**
- **Assetto Corsa Competizione**
- **BeamNG.drive**
- **Euro Truck Simulator 2**

## 📝 License

This documentation is provided under the MIT License. See [LICENSE](LICENSE) for details.

## 🌐 Website Integration

This documentation is dynamically loaded by the [LookPilot website](https://lookpilot.app) at:
- **Base URL**: `https://raw.githubusercontent.com/Reblexis/lookpilot-docs/main/`
- **Index**: `docs/index.json`
- **Guides**: Individual Markdown files rendered in real-time

---

**Made with ❤️ by the LookPilot community**
