import React, { useState } from 'react';

const AuthButtons: React.FC = () => {
  const [showModal, setShowModal] = useState(false);
  const [activeTab, setActiveTab] = useState<'signin' | 'signup'>('signin');
  const [username, setUsername] = useState('');
  const [password, setPassword] = useState('');
  const [user, setUser] = useState<string | null>(null);
  const [msg, setMsg] = useState('');

  const handleAuth = async (e: React.FormEvent) => {
    e.preventDefault();
    setMsg('');
    const endpoint = activeTab === 'signin' ? '/login' : '/register';
    
    try {
      const res = await fetch(`http://localhost:8000${endpoint}`, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ username, password })
      });
      const data = await res.json();
      
      if (!res.ok) throw new Error(data.detail || 'Error');

      if (activeTab === 'signup') {
        setMsg('Registered! Please sign in.');
        setActiveTab('signin');
      } else {
        setUser(data.username);
        setShowModal(false);
        setMsg('');
      }
    } catch (err: any) {
      setMsg(err.message);
    }
  };

  const logout = () => {
    setUser(null);
    setUsername('');
    setPassword('');
  };

  if (user) {
    return (
      <div style={{
        position: 'fixed',
        top: '20px',
        right: '180px', // Left of clock
        zIndex: 200,
        display: 'flex',
        gap: '10px',
        alignItems: 'center'
      }}>
        <div style={{
          color: '#00f2ff',
          fontFamily: 'Orbitron',
          textShadow: '0 0 5px #00f2ff',
          fontWeight: 'bold'
        }}>
          HELLO, {user.toUpperCase()}
        </div>
        <button 
          onClick={logout}
          style={{
            background: 'rgba(255, 0, 0, 0.2)',
            border: '1px solid #ff0000',
            color: '#ff0000',
            padding: '5px 15px',
            borderRadius: '5px',
            cursor: 'pointer',
            fontFamily: 'Orbitron'
          }}>
          LOGOUT
        </button>
      </div>
    );
  }

  return (
    <>
      <div style={{
        position: 'fixed',
        top: '20px',
        right: '160px', // Left of clock
        zIndex: 200,
        display: 'flex',
        gap: '10px'
      }}>
        <button 
          onClick={() => { setShowModal(true); setActiveTab('signin'); }}
          style={btnStyle}
        >
          SIGN IN
        </button>
        <button 
          onClick={() => { setShowModal(true); setActiveTab('signup'); }}
          style={btnStyle}
        >
          SIGN UP
        </button>
      </div>

      {showModal && (
        <div style={overlayStyle}>
          <div style={modalStyle}>
            <div style={headerStyle}>
              <span 
                onClick={() => setActiveTab('signin')}
                style={activeTab === 'signin' ? activeTabStyle : tabStyle}
              >
                SIGN IN
              </span>
              <span 
                onClick={() => setActiveTab('signup')}
                style={activeTab === 'signup' ? activeTabStyle : tabStyle}
              >
                SIGN UP
              </span>
              <button onClick={() => setShowModal(false)} style={closeBtnStyle}>×</button>
            </div>
            
            <form onSubmit={handleAuth} style={{ padding: '20px', display: 'flex', flexDirection: 'column', gap: '15px' }}>
              <input 
                type="text" 
                placeholder="Username" 
                value={username}
                onChange={e => setUsername(e.target.value)}
                style={inputStyle}
              />
              <input 
                type="password" 
                placeholder="Password" 
                value={password}
                onChange={e => setPassword(e.target.value)}
                style={inputStyle}
              />
              <button type="submit" style={submitBtnStyle}>
                {activeTab === 'signin' ? 'ACCESS SYSTEM' : 'INITIALIZE USER'}
              </button>
              {msg && <div style={{ color: '#ff00ff', textAlign: 'center' }}>{msg}</div>}
            </form>
          </div>
        </div>
      )}
    </>
  );
};

// Styles
const btnStyle = {
  background: 'rgba(0, 0, 0, 0.7)',
  border: '1px solid #00f2ff',
  color: '#00f2ff',
  padding: '8px 20px',
  borderRadius: '4px',
  cursor: 'pointer',
  fontFamily: 'Orbitron',
  fontWeight: 'bold',
  boxShadow: '0 0 10px rgba(0, 242, 255, 0.2)',
  transition: 'all 0.3s'
} as React.CSSProperties;

const overlayStyle = {
  position: 'fixed',
  top: 0, left: 0, right: 0, bottom: 0,
  background: 'rgba(0, 0, 0, 0.8)',
  backdropFilter: 'blur(5px)',
  zIndex: 1000,
  display: 'flex',
  justifyContent: 'center',
  alignItems: 'center'
} as React.CSSProperties;

const modalStyle = {
  width: '350px',
  background: '#050a14',
  border: '2px solid #00f2ff',
  borderRadius: '10px',
  boxShadow: '0 0 30px rgba(0, 242, 255, 0.3)',
  overflow: 'hidden'
} as React.CSSProperties;

const headerStyle = {
  display: 'flex',
  borderBottom: '1px solid #333'
} as React.CSSProperties;

const tabStyle = {
  flex: 1,
  padding: '15px',
  textAlign: 'center',
  cursor: 'pointer',
  color: '#666',
  fontFamily: 'Orbitron',
  background: '#0a1020'
} as React.CSSProperties;

const activeTabStyle = {
  ...tabStyle,
  color: '#00f2ff',
  background: '#050a14',
  borderBottom: '2px solid #00f2ff'
} as React.CSSProperties;

const inputStyle = {
  padding: '12px',
  background: 'rgba(255,255,255,0.05)',
  border: '1px solid #333',
  color: 'white',
  borderRadius: '4px',
  outline: 'none',
  fontFamily: 'monospace'
} as React.CSSProperties;

const submitBtnStyle = {
  padding: '12px',
  background: 'linear-gradient(45deg, #00f2ff, #0099ff)',
  border: 'none',
  color: 'black',
  fontWeight: 'bold',
  fontFamily: 'Orbitron',
  cursor: 'pointer',
  marginTop: '10px'
} as React.CSSProperties;

const closeBtnStyle = {
  position: 'absolute',
  top: '-40px',
  right: '0',
  background: 'none',
  border: 'none',
  color: 'white',
  fontSize: '24px',
  cursor: 'pointer'
} as React.CSSProperties;

export default AuthButtons;
