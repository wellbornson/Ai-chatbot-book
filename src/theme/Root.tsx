import React from 'react';
import ChatWidget from '@site/src/components/ChatWidget';
import DigitalClock from '@site/src/components/DigitalClock';
import AuthButtons from '@site/src/components/AuthButtons';

// Default implementation, that you can customize
export default function Root({children}) {
  return (
    <>
      {children}
      <AuthButtons />
      <DigitalClock />
      <ChatWidget />
    </>
  );
}
