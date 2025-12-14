import React from 'react';
import Layout from '@theme/Layout';
import type { Props } from '@theme/Layout';
import ChatbotButton from '../ChatbotButton';

const LayoutWrapper = (props: Props): JSX.Element => {
  return (
    <>
      <Layout {...props}>
        {props.children}
      </Layout>
      <ChatbotButton />
    </>
  );
};

export default LayoutWrapper;
