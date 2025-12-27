import type {ReactNode} from 'react';
import '@fontsource/orbitron'; // Digital font
import clsx from 'clsx';
import Link from '@docusaurus/Link';
import useDocusaurusContext from '@docusaurus/useDocusaurusContext';
import Layout from '@theme/Layout';
import HomepageFeatures from '@site/src/components/HomepageFeatures';
import Heading from '@theme/Heading';

import styles from './index.module.css';

function HomepageHeader() {
  const {siteConfig} = useDocusaurusContext();
  return (
    <header className={clsx('hero hero--primary', styles.heroBanner)}>
      {/* Advanced Teacher Greeting Widget */}
      <div className="teacher-greeting-advanced">
        {/* Decorative Corners */}
        <div className="tech-corner tech-corner-tl"></div>
        <div className="tech-corner tech-corner-tr"></div>
        <div className="tech-corner tech-corner-bl"></div>
        <div className="tech-corner tech-corner-br"></div>

        <div className="greeting-header">
           <span className="status-indicator">● SYSTEM: SECURE</span>
           <span className="id-code">:: MENTOR_NODE_01 ::</span>
        </div>
        
        <div className="mentor-block">
            <span className="mentor-label">LEAD INSTRUCTOR</span>
            <h2 className="glitch-name">SIR AMEEN ALAM</h2>
        </div>

        <div className="mentor-block">
            <span className="mentor-label">CHIEF VISIONARY</span>
            <h2 className="glitch-name">SIR ZIA KHAN</h2>
        </div>
        
        <div className="scan-line"></div>
      </div>
      
      <div className="container">
        {/* Advanced AI Hero HUD */}
        <div className="ai-hero-hud">
            {/* Tech Corners */}
            <div className="tech-corner tech-corner-tl"></div>
            <div className="tech-corner tech-corner-tr"></div>
            <div className="tech-corner tech-corner-bl"></div>
            <div className="tech-corner tech-corner-br"></div>

            <div className="greeting-header" style={{justifyContent: 'center', gap: '20px'}}>
               <span className="status-indicator">● SYSTEM: ONLINE</span>
               <span className="id-code">:: NEURAL_CORE_V2 ::</span>
            </div>

            <div style={{
              display: 'flex',
              justifyContent: 'center',
              alignItems: 'center',
              position: 'relative',
              zIndex: 2,
              padding: '40px'
            }}>
              {/* Fully Custom 3D Animated AI Logo */}
              <div className="scene-3d">
                <div className="cube-3d">
                   <div className="cube-face face-front">AI</div>
                   <div className="cube-face face-back">AI</div>
                   <div className="cube-face face-right"></div>
                   <div className="cube-face face-left"></div>
                   <div className="cube-face face-top"></div>
                   <div className="cube-face face-bottom"></div>
                   {/* Inner Core */}
                   <div className="core-3d"></div>
                </div>
              </div>
            </div>
            
            <div className="scan-line"></div>
        </div>
        <Heading as="h1" className="hero__title" style={{
            position: 'relative', 
            zIndex: 10, 
            textShadow: '0 0 10px #000, 0 0 20px #00f2ff',
            backgroundColor: 'rgba(0,0,0,0.3)',
            backdropFilter: 'blur(5px)',
            borderRadius: '10px',
            padding: '10px',
            display: 'inline-block'
        }}>
          {siteConfig.title}
        </Heading>
        <p className="hero__subtitle">{siteConfig.tagline}</p>
        <div className={styles.buttons}>
          <Link
            className="button button--secondary button--lg"
            to="/docs/intro">
            Creater zahid
          </Link>
        </div>
      </div>
    </header>
  );
}

export default function Home(): ReactNode {
  const {siteConfig} = useDocusaurusContext();
  return (
    <Layout
      title={`Hello from ${siteConfig.title}`}
      description="Description will go into a meta tag in <head />">
      <HomepageHeader />
      <main>
        <HomepageFeatures />
      </main>
    </Layout>
  );
}
