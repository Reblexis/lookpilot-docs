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
4. **Follow the guide structure**:
   - LookPilot Configuration section
   - Game Setup section
   - Troubleshooting section
5. **Submit a pull request**

### Submit Issues

1. **Go to the [Issues tab](https://github.com/your-repo/lookpilot-docs/issues)** in this repository
2. **Click "New Issue"** to create a new issue
3. **Choose an appropriate issue type**:
   - Bug report for errors or problems in documentation
   - Feature request for suggesting new guides or improvements
   - General question for clarification or help
4. **Provide clear details**:
   - Descriptive title summarizing the issue
   - Detailed description of the problem or suggestion
   - Steps to reproduce (for bugs)
   - Screenshots if applicable
5. **Add relevant labels** to help categorize the issue
6. **Submit the issue** and our team will review it

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
