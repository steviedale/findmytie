import "./ColorCard.css";

interface Props {
  color: string;
  id: number;
  onClick: (id: number, color: string) => void;
  onDeleteClick: (id: number) => void;
}

function ColorCard({ color = "red", id, onClick, onDeleteClick }: Props) {
  const handleColorChangeEvent = (
    event: React.ChangeEvent<HTMLInputElement>
  ) => {
    // console.log(event.target.value);
    onClick(id, event.target.value);
  };

  return (
    <div id='color-container'>
      <button
        className="overlay-button btn-close"
        onClick={() => onDeleteClick(id)}
      />
      <input
        type="color"
        value={color}
        onChange={handleColorChangeEvent}
        style={{}}
      />
    </div>
  );
}

export default ColorCard;
