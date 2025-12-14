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
    '01-introduction-to-physical-ai',
    '02-foundations-of-embodied-intelligence',
    '03-sensor-systems',
    '04-ros-2-fundamentals',
    '05-robot-simulation',
    '06-nvidia-isaac-platform',
    '07-humanoid-robot-kinematics-dynamics',
    '08-bipedal-locomotion-manipulation',
    '09-natural-human-robot-interaction',
    '10-conversational-robotics-gpt-integration',
  ],
};

export default sidebars;
