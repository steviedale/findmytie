import { useState } from "react";
import ColorCard from "../ColorCard/ColorCard";
import AddIcon from "@mui/icons-material/Add";
import "./SelectedColorsDisplay.css";

function SelectedColorsDisplay() {
  const defaultColor = "#996699";
  const [colors, setColors] = useState<string[]>([defaultColor, defaultColor, defaultColor]);

  function onColorChanged(id: number, color: string) {
    setColors((prevColors) => {
      const newColors = [...prevColors];
      newColors[id] = color;
      return newColors;
    });
  }

  function onDeleteCard(id: number) {
    const newColors = [...colors];
    newColors.splice(id, 1);
    setColors(newColors);
  }

  function onAddColor() {
    setColors([defaultColor, ...colors]);
  }

  return (
    <div>
      {/* // add button to add new color */}
      <button onClick={onAddColor} id="add-button">
        <AddIcon />
      </button>
      {colors.map((color, index) => (
        <ColorCard
          color={color}
          id={index}
          onClick={onColorChanged}
          onDeleteClick={onDeleteCard}
          key={index}
        />
      ))}
    </div>
  );
}

export default SelectedColorsDisplay;
