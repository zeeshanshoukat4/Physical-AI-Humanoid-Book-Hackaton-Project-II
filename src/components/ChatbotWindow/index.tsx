import React, { useState, useRef, useEffect } from 'react';
import styles from './styles.module.css';

interface Message {
  text: string;
  sender: 'user' | 'bot';
}

interface ChatbotWindowProps {
  isOpen: boolean;
  onClose: () => void;
}

const ChatbotWindow = ({ isOpen, onClose }: ChatbotWindowProps) => {
  const [messages, setMessages] = useState<Message[]>([]);
  const [input, setInput] = useState('');
  const [isLoading, setIsLoading] = useState(false);
  const chatBodyRef = useRef<HTMLDivElement>(null);

  useEffect(() => {
    if (chatBodyRef.current) {
      chatBodyRef.current.scrollTop = chatBodyRef.current.scrollHeight;
    }
  }, [messages]);
  
  if (!isOpen) {
    return null;
  }

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();
    if (!input.trim()) return;

    const userMessage: Message = { text: input, sender: 'user' };
    setMessages(prev => [...prev, userMessage]);
    setInput('');
    setIsLoading(true);

    try {
      const response = await fetch('http://localhost:8000/api/v1/chat', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({ query: input }),
      });

      if (!response.ok) {
        throw new Error('Network response was not ok');
      }

      const data = await response.json();
      const botMessage: Message = { text: data.response, sender: 'bot' };
      setMessages(prev => [...prev, botMessage]);

    } catch (error) {
      console.error('There was a problem with the fetch operation:', error);
      const errorMessage: Message = { text: 'Sorry, I am having trouble connecting to the server.', sender: 'bot' };
      setMessages(prev => [...prev, errorMessage]);
    } finally {
      setIsLoading(false);
    }
  };

  return (
    <div className={`${styles.chatbotWindow} ${isOpen ? styles.open : ''}`}>
      <div className={styles.chatHeader}>
        <span>AI Chatbot</span>
        <button onClick={onClose} className={styles.closeButton}>&times;</button>
      </div>
      <div className={styles.chatBody} ref={chatBodyRef}>
        {messages.map((msg, index) => (
          <div key={index} className={`${styles.message} ${styles[msg.sender]}`}>
            {msg.text}
          </div>
        ))}
        {isLoading && (
          <div className={`${styles.message} ${styles.bot}`}>...</div>
        )}
      </div>
      <form className={styles.chatInputForm} onSubmit={handleSubmit}>
        <input
          type="text"
          placeholder="Type a message..."
          className={styles.chatInput}
          value={input}
          onChange={(e) => setInput(e.target.value)}
        />
        <button type="submit" className={styles.sendButton}>&#x27A4;</button>
      </form>
    </div>
  );
};

export default ChatbotWindow;
