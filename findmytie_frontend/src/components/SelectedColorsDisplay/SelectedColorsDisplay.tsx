import { useState } from "react";
import ColorCard from "../ColorCard/ColorCard";
import AddIcon from "@mui/icons-material/Add";
import "./SelectedColorsDisplay.css";


interface Props {
  parentHandleColorChange: (colors: string[]) => void;
}


function SelectedColorsDisplay( { parentHandleColorChange }: Props) {
  const defaultColor = "#996699";
  const [colors, setColors] = useState<string[]>([defaultColor, defaultColor, defaultColor]);

  function onColorChanged(id: number, color: string) {
    const newColors = [...colors];
    newColors[id] = color;
    parentHandleColorChange(newColors);
    setColors(newColors);
  }

  function onDeleteCard(id: number) {
    const newColors = [...colors];
    newColors.splice(id, 1);
    parentHandleColorChange(newColors);
    setColors(newColors);
  }

  function onAddColor() {
    const newColors = [defaultColor, ...colors];
    parentHandleColorChange(newColors);
    setColors(newColors);
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
