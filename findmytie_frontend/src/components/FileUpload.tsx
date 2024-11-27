import React, { useState } from 'react';


interface Props {
  children?: React.ReactNode;
  onFileChange: (file: File) => void;
}

function FileUpload({ children, onFileChange }: Props) {

  const [selectedFile, setSelectedFile] = useState<File | null>(null);

  const handleFileChange = (event: any) => {
    setSelectedFile(event.target.files[0]);
    onFileChange(event.target.files[0]);
  };

  return (
    <div>
      <input type="file" onChange={handleFileChange} />
      {selectedFile && (
        children
      )}
    </div>
  );
}

export default FileUpload;