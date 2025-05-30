import {themes as prismThemes} from 'prism-react-renderer';
import type {Config} from '@docusaurus/types';
import type * as Preset from '@docusaurus/preset-classic';

// This runs in Node.js - Don't use client-side code here (browser APIs, JSX...)

const config: Config = {
  title: 'LookPilot Guides',
  tagline: 'Community-driven guides for LookPilot head tracking',
  favicon: 'img/favicon.ico',

  // Future flags, see https://docusaurus.io/docs/api/docusaurus-config#future
  future: {
    v4: true, // Improve compatibility with the upcoming Docusaurus v4
  },

  // Set the production url of your site here
  url: 'https://guides.lookpilot.app',
  // Set the /<baseUrl>/ pathname under which your site is served
  // For GitHub pages deployment, it is often '/<projectName>/'
  baseUrl: '/',

  // GitHub pages deployment config.
  // If you aren't using GitHub pages, you don't need these.
  organizationName: 'Reblexis', // Usually your GitHub org/user name.
  projectName: 'lookpilot-guides', // Usually your repo name.

  onBrokenLinks: 'throw',
  onBrokenMarkdownLinks: 'warn',

  // Even if you don't use internationalization, you can use this field to set
  // useful metadata like html lang. For example, if your site is Chinese, you
  // may want to replace "en" with "zh-Hans".
  i18n: {
    defaultLocale: 'en',
    locales: ['en'],
  },

  presets: [
    [
      'classic',
      {
        docs: {
          sidebarPath: './sidebars.ts',
          // Please change this to your repo.
          // Remove this to remove the "edit this page" links.
          editUrl:
            'https://github.com/Reblexis/lookpilot-guides/tree/main/',
        },
        blog: false, // Disable blog
        theme: {
          customCss: './src/css/custom.css',
        },
      } satisfies Preset.Options,
    ],
  ],

  themeConfig: {
    // Replace with your project's social card
    image: 'img/lookpilot-social-card.jpg',
    navbar: {
      title: 'LookPilot Guides',
      logo: {
        alt: 'LookPilot Logo',
        src: 'img/logo.svg',
      },
      items: [
        {
          type: 'docSidebar',
          sidebarId: 'appGuidesSidebar',
          position: 'left',
          label: 'App Guides',
        },
        {
          type: 'docSidebar',
          sidebarId: 'gameGuidesSidebar',
          position: 'left',
          label: 'Game Guides',
        },
        {
          href: 'https://github.com/Reblexis/lookpilot-guides',
          label: 'GitHub',
          position: 'right',
        },
        {
          href: 'https://lookpilot.app',
          label: 'LookPilot App',
          position: 'right',
        },
      ],
    },
    footer: {
      style: 'dark',
      links: [
        {
          title: 'Guides',
          items: [
            {
              label: 'App Guides',
              to: '/docs/app-guides/app-overview',
            },
            {
              label: 'Game Guides',
              to: '/docs/game-guides/dcs-world/windows',
            },
          ],
        },
        {
          title: 'Community',
          items: [
            {
              label: 'GitHub',
              href: 'https://github.com/Reblexis/lookpilot-guides',
            },
            {
              label: 'Contribute',
              href: 'https://github.com/Reblexis/lookpilot-guides/blob/main/CONTRIBUTING.md',
            },
          ],
        },
        {
          title: 'More',
          items: [
            {
              label: 'LookPilot App',
              href: 'https://lookpilot.app',
            },
            {
              label: 'Steam',
              href: 'https://store.steampowered.com/app/3326890/Clearsight_Eye_Tracker/',
            },
          ],
        },
      ],
      copyright: `Copyright © ${new Date().getFullYear()} LookPilot. Built with Docusaurus.`,
    },
    prism: {
      theme: prismThemes.github,
      darkTheme: prismThemes.dracula,
    },
    colorMode: {
      defaultMode: 'dark',
      disableSwitch: true,
      respectPrefersColorScheme: false,
    },
  } satisfies Preset.ThemeConfig,
};

export default config;
