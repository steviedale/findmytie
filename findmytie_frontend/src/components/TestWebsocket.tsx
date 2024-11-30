import { useEffect, useState } from 'react';
import useWebSocket, { ReadyState } from "react-use-websocket"


interface Listing {
  listing_id: string;
  title: string;
  price: number;
  url: string;
  image_url: string;
  created_at: string;
}


function MyComponent() {
  const [ listings, setListings] = useState<Listing[]>([])
  const [ listingsReceived, setListingsReceived] = useState(false);

  const WS_URL = "ws://localhost:8000/ws/api/consumer"    
  const { sendJsonMessage, lastJsonMessage, readyState } = useWebSocket(
    WS_URL,
    {
      share: false,
      shouldReconnect: () => true,
    },
  )

  // Run when the connection state (readyState) changes
  // this is run once when the component is mounted
  useEffect(() => {
    console.log("Connection state changed")
    if (readyState === ReadyState.OPEN) {
      console.log("Sending message");
      sendJsonMessage({'search_query_id': 2});
    }
  }, [readyState])

  // TODO: send out a message to the websocket server to get the listings on an interval, stop when listingsReceived is true

  // Run when a new WebSocket message is received (lastJsonMessage)
  useEffect(() => {
    console.log(lastJsonMessage)
    if (lastJsonMessage) {
      console.log("New message received")
      console.log(lastJsonMessage)
      if (lastJsonMessage.hasOwnProperty('listings')) {
        setListingsReceived(true);
        setListings(lastJsonMessage.listings.map((listing: any) => {
          const listingObj: Listing = {
            listing_id: listing.listing_id,
            title: listing.title,
            price: Number(listing.price),
            url: listing.url,
            image_url: listing.image_url,
            created_at: listing.created_at,
          }
          return listingObj;
        }));
      }
    }
  }, [lastJsonMessage])

    // ... Rest of your component logic
    return (
      <div>
        <ul>
          {listings.map((listing, idx) => (
            <li key={idx}>
              {listing.title} - {listing.price} - {listing.created_at}
            </li>
          ))}
        </ul>
      </div>
    );
};

export default MyComponent;