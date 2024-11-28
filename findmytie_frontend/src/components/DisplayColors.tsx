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
    console.log(colors);
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
