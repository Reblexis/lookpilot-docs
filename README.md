# LookPilot Guides Documentation

This repository contains the documentation website for LookPilot game guides, built with [Docusaurus](https://docusaurus.io/).

*Last updated: $(date)*

## 🌐 Live Site

The documentation is available at: [guides.lookpilot.app](https://guides.lookpilot.app)

## 🚀 Quick Start

### Prerequisites

- Node.js 18 or higher
- npm or yarn

### Installation

```bash
npm install
```

### Local Development

```bash
npm start
```

This command starts a local development server and opens up a browser window. Most changes are reflected live without having to restart the server.

### Build

```bash
npm run build
```

This command generates static content into the `build` directory and can be served using any static contents hosting service.

### Test Build Locally

```bash
npm run serve
```

This command serves the built website locally to test the production build.

## 📁 Project Structure

```
lookpilot-docs/
├── docs/                          # Documentation files
│   ├── app-guides/                # LookPilot app guides
│   │   └── app-overview.md
│   └── game-guides/               # Game-specific guides
│       ├── counter-strike-2/
│       ├── dcs-world/
│       ├── elite-dangerous/
│       ├── il2-sturmovik/
│       └── microsoft-flight-simulator-2020/
├── src/                           # Custom React components
│   ├── components/
│   ├── css/
│   └── pages/
├── static/                        # Static assets
├── docusaurus.config.js          # Docusaurus configuration
└── sidebars.js                   # Sidebar configuration
```

## 🎨 Customization

### Branding

The site uses LookPilot's brand colors and styling defined in `src/css/custom.css`. The primary color scheme uses various shades of blue (#2e8bc0, #1c5f7a, etc.).

### Navigation

- **Sidebar navigation** is configured in `sidebars.js`
- **Top navigation** is configured in `docusaurus.config.js`
- **Homepage** can be customized in `src/pages/index.tsx`

### Adding New Guides

1. Create a new directory under `docs/game-guides/[game-name]/`
2. Add platform-specific markdown files (e.g., `windows.md`, `linux.md`)
3. Update `sidebars.js` to include the new guide in navigation
4. Follow the existing guide structure and formatting

## 🚀 Deployment

The site is automatically deployed to GitHub Pages when changes are pushed to the `main` branch using GitHub Actions.

### Manual Deployment

```bash
npm run build
npm run deploy
```

### Custom Domain

The site is configured to use the custom domain `guides.lookpilot.app` via the `static/CNAME` file.

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/new-guide`)
3. Make your changes
4. Test locally (`npm start`)
5. Build and test production (`npm run build && npm run serve`)
6. Commit your changes (`git commit -am 'Add new guide'`)
7. Push to the branch (`git push origin feature/new-guide`)
8. Create a Pull Request

### Guide Writing Guidelines

- Use clear, step-by-step instructions
- Include screenshots where helpful
- Test all steps before submitting
- Follow the existing markdown structure
- Include troubleshooting sections for common issues

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🔗 Related Repositories

- [LookPilot Guides Content](https://github.com/Reblexis/lookpilot-guides) - Community-driven guide content
- [LookPilot App](https://lookpilot.app) - Main LookPilot application

## 📞 Support

For questions about the documentation or contributing:

- Open an issue in this repository
- Visit [LookPilot.app](https://lookpilot.app) for app support
- Check the [community guides repository](https://github.com/Reblexis/lookpilot-guides) for content contributions
