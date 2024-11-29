import { useState } from "react";
import SelectedColorsDisplay from "./SelectedColorsDisplay/SelectedColorsDisplay";
import ReferenceImageArea from "./ReferenceImageArea";


function QueryPage() {
  const [colors, setColors] = useState<string[]>([]);

  const handleColorChange = (newColors: string[]) => {
    setColors(newColors);
    console.log(newColors);
  };

  const handleClick = async () => {
    console.log("Search Clicked");
    try {
      const response = await fetch("http://127.0.0.1:8000/api/create-search-query", {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({
          'colors': colors,
        }),
      });

      if (!response.ok) {
        throw new Error('Network response was not ok');
      }

      const responseData = await response.json();
      // setData(responseData);
      console.log(responseData);

    } catch (error) {
      console.error('Error:', error);
      // Handle error, e.g., display an error message
    }

  };

  return (
    <div>
      <ReferenceImageArea />
      <SelectedColorsDisplay />
      <button className="btn btn-primary" onClick={handleClick} > 
        Search
      </button>
    </div>
  );
}

export default QueryPage;