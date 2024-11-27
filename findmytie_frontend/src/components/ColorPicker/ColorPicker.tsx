import { useState } from "react";
import { SketchPicker, ColorResult } from "react-color";

import Draggable from "react-draggable";
// import styles from "./ColorPicker.module.css";
import "./ColorPicker.css";

interface Props {
  color: string;
  onColorChanged: (color: ColorResult) => void;
  onCloseUpstream: () => void;
}

function ColorPicker({ color, onColorChanged, onCloseUpstream }: Props) {
  const [displayColorPicker, setDisplayColorPicker] = useState(true);

  const handleClose = () => {
    setDisplayColorPicker(false);
    onCloseUpstream();
  }

  return (
    <div>
      {displayColorPicker && (
        <Draggable>
          <div className="draggable-color-picker">
            <button className="btn btn-close" onClick={handleClose}></button>
            <SketchPicker color={color} onChange={onColorChanged} disableAlpha={true}  />
          </div>
        </Draggable>
      )}
    </div>
  );
}

export default ColorPicker;
