interface Props {
  children?: React.ReactNode;
  color?: string;
  id: number;
  onClick: (id: number, color: string) => void;
  onDeleteClick?: (id: number) => void;
}

function ColorCard({ 
    color = "red", 
    id, 
    onClick, 
    onDeleteClick,
    children
  }: Props) {

  return (
    <div style={{'width': 'fit-content', 'padding': '0.5vw'}}>
      {onDeleteClick && (
        <button className="btn btn-close" onClick={() => onDeleteClick(id)}></button>
      )}
      <button
        className="card"
        style={{ width: "15rem", height: "15rem", backgroundColor: color }}
        onClick={() => onClick(id, color)}
      >
        <div style={{ display: 'flex', justifyContent: 'center', alignItems: 'center', height: '100%', width: '100%' }}>
          {children}
        </div>
      </button>
    </div>
  );
}

export default ColorCard;
