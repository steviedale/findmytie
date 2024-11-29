import { useEffect, useState } from 'react';
import useWebSocket, { ReadyState } from "react-use-websocket"


function MyComponent() {
  const [ messages, setMessages ] = useState<string[]>([])

  const WS_URL = "ws://localhost:8000/ws/api/consumer"    
  const { sendJsonMessage, lastJsonMessage, readyState } = useWebSocket(
    WS_URL,
    {
      share: false,
      shouldReconnect: () => true,
    },
  )

  // Run when the connection state (readyState) changes
  useEffect(() => {
    console.log("Connection state changed")
    if (readyState === ReadyState.OPEN) {
      sendJsonMessage({
        event: "subscribe",
        data: {
          channel: "general-chatroom",
        },
      })
    }
  }, [readyState])

  // Run when a new WebSocket message is received (lastJsonMessage)
  useEffect(() => {
    console.log(lastJsonMessage)
    if (lastJsonMessage) {
      setMessages(lastJsonMessage);
    }
  }, [lastJsonMessage])

    // ... Rest of your component logic
    return (
      <div>
        <p>Websocket test</p>
        <ul>
          {messages.map((message, idx) => (
            <li key={idx}>{message}</li>
          ))}
        </ul>
      </div>
    );
};

export default MyComponent;