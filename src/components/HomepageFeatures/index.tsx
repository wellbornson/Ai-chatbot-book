import type {ReactNode} from 'react';
import clsx from 'clsx';
import Heading from '@theme/Heading';
import styles from './styles.module.css';

type FeatureItem = {
  title: string;
  Svg: React.ComponentType<React.ComponentProps<'svg'>>;
  description: ReactNode;
};

const FeatureList: FeatureItem[] = [
  {
    title: 'ADVANCED TECHNOLOGY', // Changed from "Easy to Use"
    Svg: require('@site/static/img/undraw_docusaurus_mountain.svg').default,
    description: (
      <>
        Experience the cutting edge of documentation systems. Designed for 
        high-performance teams building the future of digital knowledge.
      </>
    ),
  },
  {
    title: 'FOCUS ON WHAT MATTERS',
    Svg: require('@site/static/img/undraw_docusaurus_tree.svg').default,
    description: (
      <>
        Streamline your workflow with our intelligent core. We handle the 
        complex rendering logic so you can deploy critical data instantly.
      </>
    ),
  },
  {
    title: 'POWERED BY REACT',
    Svg: require('@site/static/img/undraw_docusaurus_react.svg').default,
    description: (
      <>
        Built on the robust React ecosystem. Extend functionality with 
        component-driven architecture and seamless integration.
      </>
    ),
  },
];

function Feature({title, Svg, description}: FeatureItem) {
  return (
    <div className={clsx('col col--4')}>
      {/* Added "feature-card" class for the glassmorphism/3D effect */}
      <div className="feature-card"> 
        <div className="text--center">
          <Svg className="featureSvg" role="img" />
        </div>
        <div className="text--center padding-horiz--md">
          <Heading as="h3" className="feature-title">{title}</Heading>
          <p>{description}</p>
        </div>
      </div>
    </div>
  );
}

export default function HomepageFeatures(): ReactNode {
  return (
    <section className="features">
      <div className="container">
        <div className="row">
          {FeatureList.map((props, idx) => (
            <Feature key={idx} {...props} />
          ))}
        </div>
      </div>
    </section>
  );
}