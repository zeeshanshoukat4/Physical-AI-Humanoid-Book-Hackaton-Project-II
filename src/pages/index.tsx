import React from 'react';
import LayoutWrapper from '@site/src/components/LayoutWrapper';
import Link from '@docusaurus/Link'; // Import Link component
import useBaseUrl from '@docusaurus/useBaseUrl'; // Import useBaseUrl

export default function Home() {
  return (
    <LayoutWrapper
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
        }}>
        <h1 style={{ 
            fontSize: '3.5rem', 
            marginBottom: '1rem', 
            color: '#1a1a1a',
            textShadow: '0 0 10px #C58AF9, 0 0 20px #C58AF9, 0 0 30px #F0D5F5, 0 0 40px #F0D5F5, 0 0 50px #B7A0C7, 0 0 60px #B7A0C7, 0 0 70px #B7A0C7' 
          }}>
          Physical AI & Humanoid Robotics
        </h1>
        <p style={{ 
            fontSize: '1.5rem', 
            marginBottom: '2rem',
            color: '#1a1a1a',
            textShadow: '0 0 5px #C58AF9, 0 0 10px #C58AF9, 0 0 15px #F0D5F5, 0 0 20px #F0D5F5, 0 0 25px #B7A0C7, 0 0 30px #B7A0C7, 0 0 35px #B7A0C7'
          }}>
          Your journey into embodied intelligence begins here.
        </p>
      <Link
  className="button button--secondary button--lg"
  to={useBaseUrl('/docs/intro')}>
  Start Reading
</Link>


      </header>
    </LayoutWrapper>
  );
}