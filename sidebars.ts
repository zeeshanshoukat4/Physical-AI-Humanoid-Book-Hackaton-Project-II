import type {SidebarsConfig} from '@docusaurus/plugin-content-docs';

// This runs in Node.js - Don't use client-side code here (browser APIs, JSX...)

/**
 * Creating a sidebar enables you to:
 - create an ordered group of docs
 - render a sidebar for each doc of that group
 - provide next/previous navigation

 The sidebars can be generated from the filesystem, or explicitly defined here.

 Create as many sidebars as you want.
 */
const sidebars: SidebarsConfig = {
  bookSidebar: [
    'intro',
    'foundations-of-embodied-intelligence',
    'sensor-systems',
    'ros-2-fundamentals',
    'robot-simulation',
    'nvidia-isaac-platform',
    'humanoid-robot-kinematics-dynamics',
    'bipedal-locomotion-manipulation',
    'natural-human-robot-interaction',
    'conversational-robotics-gpt-integration',
  ],
};

export default sidebars;
