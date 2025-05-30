import React from 'react';
import styles from './styles.module.css';

interface GuideLayoutProps {
  title: string;
  platform: 'Windows' | 'Linux';
  game: string;
  children: React.ReactNode;
  protocolTip?: string;
  gameTip?: string;
}

export default function GuideLayout({
  title,
  platform,
  game,
  children,
  protocolTip,
  gameTip
}: GuideLayoutProps): React.ReactElement {
  const platformIcon = platform === 'Windows' ? '🪟' : '🐧';
  const platformClass = platform.toLowerCase();

  return (
    <div className={styles.guideContainer}>
      <div className={styles.guideHeader}>
        <div className={`${styles.platformBadge} ${styles[platformClass]}`}>
          {platformIcon} {platform}
        </div>
        <h1>{title}</h1>
        <p className={styles.subtitle}>
          Setting up LookPilot with {game} on {platform}
        </p>
      </div>

      <div className={styles.guideContent}>
        {children}
      </div>

      {protocolTip && (
        <div className={`${styles.tip} ${styles.protocolTip}`}>
          <span className={styles.tipIcon}>💡</span>
          <strong>Protocol Tip:</strong> {protocolTip}
        </div>
      )}

      {gameTip && (
        <div className={`${styles.tip} ${styles.gameTip}`}>
          <span className={styles.tipIcon}>🎮</span>
          <strong>Game Tip:</strong> {gameTip}
        </div>
      )}

      <div className={styles.guideFooter}>
        <p>
          <em>
            Part of the{' '}
            <a 
              href="https://github.com/Reblexis/lookpilot-guides" 
              target="_blank" 
              rel="noopener noreferrer"
            >
              LookPilot Guides
            </a>{' '}
            community project.
          </em>
        </p>
      </div>
    </div>
  );
} 