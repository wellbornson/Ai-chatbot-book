import React, { useState, useEffect } from 'react';

const DigitalClock: React.FC = () => {
  const [time, setTime] = useState(new Date());

  useEffect(() => {
    const timer = setInterval(() => setTime(new Date()), 1000);
    return () => clearInterval(timer);
  }, []);

  return (
    <div className="digital-clock-container">
      <div className="digital-clock">
        {time.toLocaleTimeString()}
      </div>
    </div>
  );
};

export default DigitalClock;
