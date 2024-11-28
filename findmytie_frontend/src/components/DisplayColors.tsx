import { useState } from "react";
import ColorPicker from "./ColorPicker";
import ColorCard from "./ColorCard";
import { ColorResult } from "react-color";
import AddIcon from "@mui/icons-material/Add";

function DisplayColors() {
  const [colors, setColors] = useState([
    "red",
    "blue",
    "green",
    "yellow",
    "purple",
    "#8080ff",
  ]);
  const [selectedColor, setSelectedColor] = useState(-1);

  function onColorClick(id: number) {
    setSelectedColor(id);
  }

  function onDeleteCard(id: number) {
    const newColors = [...colors];
    newColors.splice(id, 1);
    setColors(newColors);
  }

  function onAddColor() {
    setColors([...colors, "#ffffff"]);
  }

  function onSearchClick() {
    var response = null;
    try {
      response = fetch("http://127.0.0.1:8000/api/create-search-query", {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json'
        },
        body: JSON.stringify({'colors': colors})
      });
    } catch (err: any) {
      console.log("Error: ", err);
    } finally {
    }

    console.log("Search Clicked");
    console.log(response);
  }

  return (
    <div className="container">
      <div className="row">
        {colors.map((color, index) => (
          <ColorCard
            color={color}
            id={index}
            onClick={onColorClick}
            onDeleteClick={onDeleteCard}
            key={index}
          />
        ))}
        {/* // add button to add new color */}
        <ColorCard
          color={"#cccccc"}
          id={-2}
          onClick={onAddColor}
          key={-2}
        >
          <AddIcon
            style={{ fontSize: 40, fill: "#000000", fillOpacity: "50%" }}
          />
        </ColorCard>
      </div>
      {/* if selectedColor is not -1, then show the color picker */}
      {selectedColor !== -1 && (
        <ColorPicker
          color={colors[selectedColor]}
          onColorChanged={(color: ColorResult) => {
            // console.log(color.hex);
            const newColors = [...colors];
            newColors[selectedColor] = color.hex;
            setColors(newColors);
          }}
          onCloseUpstream={() => setSelectedColor(-1)}
        />
      )}
      <button className="btn btn-primary" onClick={onSearchClick}> 
        Search
      </button>
    </div>
  );
}

export default DisplayColors;
