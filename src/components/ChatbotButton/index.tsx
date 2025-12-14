import React from 'react';

const ChatbotButton = () => {
  return (
    <button
      style={{
        position: 'fixed',
        bottom: '30px',
        right: '30px',
        width: '60px',
        height: '60px',
        borderRadius: '50%',
        backgroundColor: 'var(--ifm-color-primary)',
        color: 'white',
        border: 'none',
        cursor: 'pointer',
        boxShadow: '0 0 10px var(--ifm-color-primary), 0 0 20px var(--ifm-color-primary)',
        display: 'flex',
        alignItems: 'center',
        justifyContent: 'center',
        fontSize: '2rem',
        zIndex: 1000,
      }}
      onClick={() => alert('Chatbot clicked!')} // Placeholder action
    >
      🤖
    </button>
  );
};

export default ChatbotButton;
