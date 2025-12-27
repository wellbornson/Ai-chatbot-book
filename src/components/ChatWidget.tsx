import React, { useState, useRef, useEffect } from 'react';
import ReactMarkdown from 'react-markdown';

// Types for messages
interface Message {
  id: string;
  role: 'user' | 'agent';
  content: string;
}

const ChatWidget: React.FC = () => {
  const [isOpen, setIsOpen] = useState(false);
  const [messages, setMessages] = useState<Message[]>([]);
  const [inputValue, setInputValue] = useState('');
  const [isLoading, setIsLoading] = useState(false);
  const [error, setError] = useState<string | null>(null);
  const [threadId, setThreadId] = useState<string | null>(null);
  const messagesEndRef = useRef<HTMLDivElement>(null);

  const toggleChat = () => setIsOpen(!isOpen);

  const scrollToBottom = () => {
    messagesEndRef.current?.scrollIntoView({ behavior: 'smooth' });
  };

  useEffect(() => {
    scrollToBottom();
  }, [messages, isOpen]);

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();
    if (!inputValue.trim() || isLoading) return;

    const userMessage: Message = {
      id: Date.now().toString(),
      role: 'user',
      content: inputValue,
    };

    setMessages((prev) => [...prev, userMessage]);
    setInputValue('');
    setIsLoading(true);
    setError(null);

    try {
      // TODO: If deploying frontend to Vercel, this URL must be your DEPLOYED backend URL (e.g. Render/Railway), not localhost.
      const response = await fetch('http://localhost:8000/chat', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({
          query: userMessage.content,
          thread_id: threadId,
        }),
      });

      if (!response.ok) {
        throw new Error('Failed to fetch response');
      }

      const data = await response.json();

      if (data.thread_id) {
        setThreadId(data.thread_id);
      }

      const agentMessage: Message = {
        id: (Date.now() + 1).toString(),
        role: 'agent',
        content: data.response,
      };

      setMessages((prev) => [...prev, agentMessage]);
    } catch (err) {
      console.error(err);
      setError('Failed to get response from agent. Is the backend running?');
    } finally {
      setIsLoading(false);
    }
  };

  return (
    <div style={{
      position: 'fixed',
      bottom: '30px',
      right: '30px',
      zIndex: 9999,
      fontFamily: 'Orbitron, monospace'
    }}>
      {/* Chat Window */}
      {isOpen && (
        <div className="chat-window-3d" style={{
          width: '400px',
          height: '550px',
          background: 'rgba(5, 10, 20, 0.85)', // More transparent for glass effect
          backdropFilter: 'blur(12px)',
          borderRadius: '20px',
          boxShadow: '0 0 30px rgba(0, 242, 255, 0.5), inset 0 0 15px rgba(0, 242, 255, 0.2)',
          display: 'flex',
          flexDirection: 'column',
          marginBottom: '20px',
          border: '1px solid rgba(0, 242, 255, 0.4)',
          overflow: 'hidden',
          position: 'relative',
        }}>
          {/* Animated border effect */}
          <div style={{
            position: 'absolute',
            top: 0,
            left: 0,
            right: 0,
            height: '3px',
            background: 'linear-gradient(90deg, transparent, #00f2ff, #bd00ff, #00f2ff, transparent)',
            animation: 'slide 3s linear infinite',
            zIndex: 10
          }}></div>

          {/* Header */}
          <div style={{
            padding: '20px',
            background: 'rgba(5, 10, 20, 0.8)',
            color: '#00f2ff',
            fontWeight: 'bold',
            display: 'flex',
            justifyContent: 'space-between',
            alignItems: 'center',
            borderBottom: '1px solid rgba(0, 242, 255, 0.3)',
            position: 'relative'
          }}>
            <div style={{ display: 'flex', alignItems: 'center', gap: '10px' }}>
              <div style={{
                width: '12px',
                height: '12px',
                borderRadius: '50%',
                background: '#00f2ff',
                boxShadow: '0 0 10px #00f2ff',
                animation: 'pulse 1.5s infinite'
              }}></div>
              <span style={{ fontFamily: 'Orbitron, monospace', fontSize: '1.2rem' }}>AI Assistant</span>
            </div>
            <button
              onClick={toggleChat}
              style={{
                background: 'none',
                border: 'none',
                color: '#00f2ff',
                cursor: 'pointer',
                fontSize: '24px',
                fontFamily: 'Orbitron, monospace',
                textShadow: '0 0 10px rgba(0, 242, 255, 0.7)'
              }}
            >
              ×
            </button>
          </div>

          {/* Messages Area */}
          <div style={{
            flex: 1,
            padding: '20px',
            overflowY: 'auto',
            background: 'rgba(5, 10, 20, 0.6)',
            position: 'relative'
          }}>
            {/* Grid background */}
            <div style={{
              position: 'absolute',
              top: 0,
              left: 0,
              right: 0,
              bottom: 0,
              backgroundImage: `
                linear-gradient(rgba(0, 242, 255, 0.05) 1px, transparent 1px),
                linear-gradient(90deg, rgba(0, 242, 255, 0.05) 1px, transparent 1px)
              `,
              backgroundSize: '30px 30px',
              pointerEvents: 'none',
              zIndex: 0
            }}></div>

            <div style={{ position: 'relative', zIndex: 1 }}>
              {messages.length === 0 && (
                <div style={{
                  textAlign: 'center',
                  color: '#a8b2d1',
                  marginTop: '20px',
                  fontFamily: 'Orbitron, monospace',
                  fontSize: '1.1rem',
                  textShadow: '0 0 10px rgba(168, 178, 209, 0.5)'
                }}>
                  🤖 Hello! I'm your AI assistant. Ask me anything!
                </div>
              )}

              {messages.map((msg) => (
                <div key={msg.id} style={{
                  marginBottom: '15px',
                  textAlign: msg.role === 'user' ? 'right' : 'left',
                  position: 'relative',
                  zIndex: 2
                }}>
                  <div style={{
                    display: 'inline-block',
                    padding: '12px 16px',
                    borderRadius: '16px',
                    maxWidth: '85%',
                    backgroundColor: msg.role === 'user'
                      ? 'linear-gradient(135deg, #00f2ff, #00a1aa)'
                      : 'rgba(15, 23, 42, 0.8)',
                    color: msg.role === 'user' ? '#000' : '#e3e3e3',
                    border: msg.role === 'agent' ? '1px solid rgba(0, 242, 255, 0.3)' : 'none',
                    whiteSpace: 'pre-wrap',
                    textAlign: 'left',
                    fontFamily: 'Orbitron, monospace',
                    boxShadow: msg.role === 'user'
                      ? '0 0 15px rgba(0, 242, 255, 0.4)'
                      : '0 0 10px rgba(0, 242, 255, 0.2)',
                    fontWeight: msg.role === 'user' ? 'bold' : 'normal'
                  }}>
                    {msg.role === 'agent' ? (
                      <ReactMarkdown>{msg.content}</ReactMarkdown>
                    ) : (
                      msg.content
                    )}
                  </div>
                </div>
              ))}

              {isLoading && (
                <div style={{ textAlign: 'left', marginBottom: '15px', position: 'relative', zIndex: 2 }}>
                  <div style={{
                    display: 'inline-block',
                    padding: '12px 16px',
                    backgroundColor: 'rgba(15, 23, 42, 0.8)',
                    borderRadius: '16px',
                    border: '1px solid rgba(0, 242, 255, 0.3)',
                    color: '#a8b2d1',
                    fontFamily: 'Orbitron, monospace',
                    boxShadow: '0 0 10px rgba(0, 242, 255, 0.2)'
                  }}>
                    <div style={{ display: 'flex', alignItems: 'center', gap: '8px' }}>
                      <div style={{
                        width: '8px',
                        height: '8px',
                        borderRadius: '50%',
                        background: '#00f2ff',
                        boxShadow: '0 0 8px #00f2ff',
                        animation: 'pulse 1.5s infinite'
                      }}></div>
                      <span>Processing...</span>
                    </div>
                  </div>
                </div>
              )}

              {error && (
                <div style={{
                  color: '#ff6b6b',
                  fontSize: '0.9rem',
                  textAlign: 'center',
                  marginTop: '10px',
                  fontFamily: 'Orbitron, monospace',
                  textShadow: '0 0 5px rgba(255, 107, 107, 0.5)'
                }}>
                  {error}
                </div>
              )}

              <div ref={messagesEndRef} />
            </div>
          </div>

          {/* Input Area */}
          <form onSubmit={handleSubmit} style={{
            padding: '20px',
            borderTop: '1px solid rgba(0, 242, 255, 0.3)',
            backgroundColor: 'rgba(5, 10, 20, 0.8)',
            display: 'flex',
            gap: '10px'
          }}>
            <input
              type="text"
              value={inputValue}
              onChange={(e) => setInputValue(e.target.value)}
              placeholder="Ask anything..."
              style={{
                flex: 1,
                padding: '12px 16px',
                borderRadius: '25px',
                border: '1px solid rgba(0, 242, 255, 0.3)',
                outline: 'none',
                background: 'rgba(15, 23, 42, 0.6)',
                color: '#e3e3e3',
                fontFamily: 'Orbitron, monospace',
                fontSize: '1rem'
              }}
            />
            <button
              type="submit"
              disabled={isLoading || !inputValue.trim()}
              style={{
                padding: '12px 20px',
                background: 'linear-gradient(135deg, #00f2ff, #bd00ff)',
                color: '#000',
                border: 'none',
                borderRadius: '25px',
                cursor: 'pointer',
                opacity: isLoading ? 0.7 : 1,
                fontFamily: 'Orbitron, monospace',
                fontWeight: 'bold',
                boxShadow: '0 0 15px rgba(0, 242, 255, 0.5)',
                transition: 'all 0.3s ease'
              }}
              onMouseEnter={(e) => {
                (e.target as HTMLElement).style.transform = 'scale(1.05)';
                (e.target as HTMLElement).style.boxShadow = '0 0 20px rgba(0, 242, 255, 0.8)';
              }}
              onMouseLeave={(e) => {
                (e.target as HTMLElement).style.transform = 'scale(1)';
                (e.target as HTMLElement).style.boxShadow = '0 0 15px rgba(0, 242, 255, 0.5)';
              }}
            >
              Send
            </button>
          </form>
        </div>
      )}

      {/* Toggle Button - Enhanced Digital Look */}
      <button
        onClick={toggleChat}
        style={{
          width: '80px',
          height: '80px',
          borderRadius: '50%',
          background: 'rgba(0,0,0,0.5)', // Transparent to show cube better
          border: '1px solid #00f2ff',
          boxShadow: '0 0 25px rgba(0, 242, 255, 0.5)',
          cursor: 'pointer',
          display: 'flex',
          alignItems: 'center',
          justifyContent: 'center',
          position: 'relative',
          transition: 'all 0.3s ease'
        }}
        onMouseEnter={(e) => {
          (e.currentTarget as HTMLElement).style.transform = 'scale(1.1)';
          (e.currentTarget as HTMLElement).style.boxShadow = '0 0 35px rgba(0, 242, 255, 0.9)';
        }}
        onMouseLeave={(e) => {
          (e.currentTarget as HTMLElement).style.transform = 'scale(1)';
          (e.currentTarget as HTMLElement).style.boxShadow = '0 0 25px rgba(0, 242, 255, 0.5)';
        }}
      >
        {isOpen ? (
           <span style={{color: '#00f2ff', fontSize: '30px'}}>✕</span>
        ) : (
           <div className="mini-cube-wrapper">
               <div className="mini-cube-face mini-front">AI</div>
               <div className="mini-cube-face mini-back">AI</div>
               <div className="mini-cube-face mini-right"></div>
               <div className="mini-cube-face mini-left"></div>
               <div className="mini-cube-face mini-top"></div>
               <div className="mini-cube-face mini-bottom"></div>
           </div>
        )}
      </button>

    </div>
  );
};

export default ChatWidget;
