import React, { useState, useRef, useEffect } from 'react';
import { Send, Bot, User, Settings } from 'lucide-react';

const ChatbotInterface = () => {
  const [messages, setMessages] = useState([]);
  const [inputMessage, setInputMessage] = useState('');
  const [isLoading, setIsLoading] = useState(false);
  const [sessionId, setSessionId] = useState('');
  const [userId, setUserId] = useState('');
  const [agentName, setAgentName] = useState('sample_agent');
  const [showSettings, setShowSettings] = useState(false);
  const messagesEndRef = useRef(null);
  const inputRef = useRef(null);

  useEffect(() => {
    setSessionId(`session_${Date.now()}_${Math.random().toString(36).substr(2, 9)}`);
    setUserId(`user_${Math.random().toString(36).substr(2, 9)}`);
  }, []);

  useEffect(() => {
    messagesEndRef.current?.scrollIntoView({ behavior: 'smooth' });
  }, [messages]);

  const sendMessage = async () => {
    if (!inputMessage.trim() || isLoading) return;

    const userMessage = {
      id: Date.now(),
      type: 'user',
      content: inputMessage.trim(),
      timestamp: new Date()
    };

    setMessages(prev => [...prev, userMessage]);
    setInputMessage('');
    setIsLoading(true);

    try {
      const response = await fetch('http://localhost:8000/api/generate', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({
          session_id: sessionId,
          user_id: userId,
          agent_name: agentName,
          input_query: userMessage.content
        })
      });

      if (!response.ok) throw new Error(`HTTP error! status: ${response.status}`);

      const data = await response.json();

      const botMessage = {
        id: Date.now() + 1,
        type: 'bot',
        content: data.response || 'No response received',
        timestamp: new Date()
      };

      setMessages(prev => [...prev, botMessage]);
    } catch (error) {
      const errorMessage = {
        id: Date.now() + 1,
        type: 'bot',
        content: `Error: ${error.message}`,
        timestamp: new Date(),
        isError: true
      };
      setMessages(prev => [...prev, errorMessage]);
    } finally {
      setIsLoading(false);
      inputRef.current?.focus();
    }
  };

  const handleKeyPress = (e) => {
    if (e.key === 'Enter' && !e.shiftKey) {
      e.preventDefault();
      sendMessage();
    }
  };

  const clearChat = () => {
    setMessages([]);
    setSessionId(`session_${Date.now()}_${Math.random().toString(36).substr(2, 9)}`);
  };

  return (
    <div className="flex flex-col h-screen bg-gradient-to-br from-gray-100 to-white">
      {/* Header */}
      <div className="bg-white shadow-md p-4 border-b">
        <div className="max-w-4xl mx-auto flex items-center justify-between">
          <div className="flex items-center space-x-3">
            <Bot className="w-6 h-6 text-blue-600" />
            <h1 className="text-lg font-semibold text-gray-900">AI Chatbot</h1>
          </div>
          <button
            onClick={() => setShowSettings(!showSettings)}
            className="p-2 hover:bg-gray-100 rounded-lg text-gray-600"
          >
            <Settings className="w-5 h-5" />
          </button>
        </div>
      </div>

      {/* Settings */}
      {showSettings && (
        <div className="bg-white border-b shadow-sm">
          <div className="max-w-4xl mx-auto p-4 space-y-4">
            <h3 className="font-medium text-gray-800">Settings</h3>
            <div className="grid grid-cols-1 md:grid-cols-3 gap-4">
              <div>
                <label className="block text-sm font-medium text-gray-700 mb-1">Agent</label>
                <select
                  value={agentName}
                  onChange={(e) => setAgentName(e.target.value)}
                  className="w-full px-3 py-2 border rounded-lg"
                >
                  <option value="sample_agent">Sample Agent</option>
                  <option value="hrmanager_agent">HR Manager Agent</option>
                </select>
              </div>
              <div>
                <label className="block text-sm font-medium text-gray-700 mb-1">User ID</label>
                <input
                  value={userId}
                  onChange={(e) => setUserId(e.target.value)}
                  className="w-full px-3 py-2 border rounded-lg"
                />
              </div>
              <div>
                <label className="block text-sm font-medium text-gray-700 mb-1">Session ID</label>
                <input
                  value={sessionId}
                  onChange={(e) => setSessionId(e.target.value)}
                  className="w-full px-3 py-2 border rounded-lg"
                />
              </div>
            </div>
            <button
              onClick={clearChat}
              className="px-4 py-2 bg-red-600 text-white rounded hover:bg-red-700"
            >
              Clear Chat & Start New
            </button>
          </div>
        </div>
      )}

      {/* Messages */}
      <div className="flex-1 overflow-y-auto px-4 py-6">
        <div className="max-w-4xl mx-auto space-y-6">
          {messages.length === 0 && (
            <div className="text-center py-20 text-gray-400">
              <Bot className="w-10 h-10 mx-auto mb-4 text-blue-400" />
              <p className="text-base">Start chatting with the AI...</p>
            </div>
          )}

          {messages.map((message) => (
            <div
              key={message.id}
              className={`flex items-start ${
                message.type === 'user' ? 'justify-end' : 'justify-start'
              }`}
            >
              <div
                className={`px-4 py-3 rounded-2xl text-sm max-w-xl ${
                  message.type === 'user'
                    ? 'bg-blue-600 text-white'
                    : message.isError
                    ? 'bg-red-100 text-red-800'
                    : 'bg-gray-100 text-gray-900'
                }`}
              >
                <p className="whitespace-pre-wrap">{message.content}</p>
                <div className="text-[11px] text-gray-500 mt-1 text-right">
                  {message.timestamp.toLocaleTimeString()}
                </div>
              </div>
            </div>
          ))}

          {isLoading && (
            <div className="flex items-center space-x-2 px-4 py-3 bg-gray-100 text-gray-500 rounded-2xl text-sm w-fit animate-pulse">
              <span className="animate-bounce">●</span>
              <span className="animate-bounce delay-100">●</span>
              <span className="animate-bounce delay-200">●</span>
            </div>
          )}

          <div ref={messagesEndRef} />
        </div>
      </div>

      {/* Input */}
      <div className="sticky bottom-0 bg-white border-t p-4">
        <div className="max-w-4xl mx-auto flex items-center space-x-2">
          <textarea
            ref={inputRef}
            value={inputMessage}
            onChange={(e) => setInputMessage(e.target.value)}
            onKeyPress={handleKeyPress}
            placeholder="Ask something..."
            rows="1"
            disabled={isLoading}
            className="flex-1 px-4 py-3 text-sm border border-gray-300 rounded-full focus:ring-2 focus:ring-blue-500 focus:outline-none resize-none disabled:opacity-50"
          />
          <button
            onClick={sendMessage}
            disabled={!inputMessage.trim() || isLoading}
            className="p-3 bg-blue-600 hover:bg-blue-700 text-white rounded-full transition-colors disabled:opacity-50"
          >
            <Send className="w-5 h-5" />
          </button>
        </div>
      </div>
    </div>
  );
};

export default ChatbotInterface;
