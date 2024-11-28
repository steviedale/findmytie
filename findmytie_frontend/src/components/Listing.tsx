import React, { useState, useEffect } from "react";

interface Item {
  id: number;
  code: string;
  colors: string;
  host: string;
  created_at: string;
}

function Listing() {
  const [listings, setListings] = useState<Item[]>([]);
  const [isLoading, setIsLoading] = useState(true);
  const [error, setError] = useState<any>(null);

  useEffect(() => {
    const fetchData = async () => {
      setIsLoading(true);
      try {
        const host = "wmedhdai0ccmw90bd9qnh0kcd313kxmi";
        const response = await fetch(
          "http://127.0.0.1:8000/api/get-search-query?host=" + host
        );
        const data = await response.json();

        setListings(
          data.map((item: any) => {
            return {
              id: item.id,
              code: item.code,
              colors: item.colors,
              host: item.host,
              created_at: item.created_at,
            };
          })
        );
      } catch (err: any) {
        setError(err);
      } finally {
        setIsLoading(false);
      }
    };

    fetchData();
  }, []);

  if (isLoading) {
    return <div>Loading...</div>;
  }

  if (error) {
    if (error instanceof Error) {
      return <div>Error: {error.message}</div>;
    }
  }

  return (
    <ul>
      {listings.map((listing) => (
        <li key={listing.id}>
          {/* Display listing data here */}
          <h2>{listing.id}</h2>
          <p>{listing.host}</p>
          <p>{listing.colors}</p>
        </li>
      ))}
    </ul>
    // <p>{listings}</p>
    // <p>dummy</p>
  );
}

export default Listing;
