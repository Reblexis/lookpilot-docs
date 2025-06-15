# LookPilot Documentation

Official documentation repository for LookPilot head and eye tracking software. This repository contains all user guides, setup instructions, and troubleshooting documentation that powers the [LookPilot website](https://lookpilot.app).

## 📚 What's in this Repository

This repository contains comprehensive Markdown-based documentation for LookPilot:

- Application Documentation (`docs/app-docs/`)
- Game Setup Guides (`docs/game-docs/`)

Each game is split into Linux and Windows guides and each guide includes:
- LookPilot configuration steps
- In-game setup instructions
- Troubleshooting tips

## 🤝 How to Contribute

We welcome community contributions! Here's how you can help improve LookPilot documentation:

### Adding a New Game Guide

1. **Fork this repository**
2. **Create a new directory** under `docs/game-docs/your-game-name/`
3. **Add required files**:
   - `manifest.json` - Game metadata (name)
   - `windows.md` and/or `linux.md` - Platform-specific guides
4. **Submit a pull request**

### Submit Issues

In issues, you can describe any problems that you have encountered using the guides, request games to be added, describe game guides or generally give any suggestions.

1. **Go to the [Issues tab](https://github.com/your-repo/lookpilot-docs/issues](https://github.com/Reblexis/lookpilot-docs/issues)** in this repository
2. **Click "New Issue"** to create a new issue
3. **Provide clear details**:
   - Descriptive title summarizing the issue
   - Detailed description of the problem, suggestion or game setup
   - Steps to reproduce (for bugs)
   - Screenshots if applicable
4. **Submit the issue** and our team will review it

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
```
## 📝 License

This documentation is provided under the MIT License. See [LICENSE](LICENSE) for details.
