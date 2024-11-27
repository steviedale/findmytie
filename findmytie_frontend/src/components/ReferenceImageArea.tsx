import { useState } from "react";
import FileUpload from "./FileUpload";

function ReferenceImageArea() {
  const [selectedFile, setSelectedFile] = useState<File | null>(null);

  const handleFileChange = (file: File) => {
    setSelectedFile(file);
  };

  return (
    // Set background color of div to light blue
    <div style={{ 
      backgroundColor: "powderblue", 
      // width: "50%", 
      // height: "500px",  
      height: "100%",  
      // height: "50vh",  
      border: '5px solid #555' 
    }}>
      <FileUpload onFileChange={handleFileChange}>
        <p>Selected File: {selectedFile?.name}</p>
        {selectedFile && (
          <center>
            <img
              src={URL.createObjectURL(selectedFile)}
              alt="Reference Image"
              width="50%"
              style={{
                backgroundColor: "powderblue", 
                width: "10%",   
                // height: "100%",   
                // height: "100px",   
                border: '5px solid #555',
              }}
            />
          </center>
        )}
      </FileUpload>
    </div>
  );
}

export default ReferenceImageArea;
