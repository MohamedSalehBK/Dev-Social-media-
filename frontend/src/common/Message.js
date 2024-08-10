import React from 'react';

const Message = ({ onClose, variant, dismissible, children }) => {
  return (
    <div>
      {children}
      {dismissible && <div onClick={onClose}>✕</div>}
    </div>
  );
};

export default Message;
