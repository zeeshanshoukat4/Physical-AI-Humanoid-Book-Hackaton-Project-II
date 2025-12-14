import React from 'react';
import Layout from '@theme/Layout';
import Link from '@docusaurus/Link'; // Import Link component
import useBaseUrl from '@docusaurus/useBaseUrl'; // Import useBaseUrl

export default function Home() {
  return (
    <Layout
      title="Physical AI & Humanoid Robotics"
      description="A comprehensive guide to Physical AI and Humanoid Robotics.">
      <header
        style={{
          display: 'flex',
          flexDirection: 'column',
          alignItems: 'center',
          justifyContent: 'center',
          height: '80vh',
          backgroundImage: 'url("https://images.unsplash.com/photo-1518779578993-ec3579df2cc0?q=80&w=2940&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D")', // Placeholder futuristic background
          backgroundSize: 'cover',
          backgroundPosition: 'center',
          color: 'white',
          textAlign: 'center',
          textShadow: '0 0 10px rgba(0,255,118,0.8), 0 0 20px rgba(0,255,118,0.6)',
        }}>
        <h1 style={{ fontSize: '3.5rem', marginBottom: '1rem', textShadow: '0 0 15px rgba(0,255,118,0.9), 0 0 25px rgba(0,255,118,0.7)' }}>
          Physical AI & Humanoid Robotics
        </h1>
        <p style={{ fontSize: '1.5rem', marginBottom: '2rem' }}>
          Your journey into embodied intelligence begins here.
        </p>
        <Link
          className="button button--secondary button--lg"
          to={useBaseUrl('/docs/01-introduction-to-physical-ai')}>
          Start Reading
        </Link>
      </header>
    </Layout>
  );
}