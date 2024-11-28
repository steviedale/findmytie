import React, { useState, useEffect } from "react";
import { useParams } from 'react-router-dom';


interface Listing {
  id: number;
  title: string;
  price: number;
  url: string;
  image_url: string;
  created_at: string;
}


function ShowListings() {
  const [listings, setListings] = useState<Listing[]>([]);
  const [isLoading, setIsLoading] = useState(true);
  const [error, setError] = useState<any>(null);

  const { searchQueryId } = useParams();

  useEffect(() => {
    const fetchData = async () => {
      setIsLoading(true);
      try {
        const response = await fetch(
          "http://127.0.0.1:8000/api/get-listings?search-query-id=" + searchQueryId
        );
        const data = await response.json();

        setListings(
          data.map((item: any) => {
            return {
              id: item.id,
              title: item.title,
              price: item.price,
              url: item.url,
              image_url: item.url_image,
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
          <h2>{listing.title}</h2>
          <p>Price: {listing.price}</p>
        </li>
      ))}
    </ul>
  );
}

export default ShowListings;
