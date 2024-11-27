import DisplayColors from "./components/DisplayColors";
import ReferenceImageArea from "./components/ReferenceImageArea";
import SandBox from "./components/SandBox";
import { BrowserRouter, Routes, Route } from "react-router-dom";


function App() {
  return (
    <BrowserRouter>
      <Routes>

        <Route path="/" element={<DisplayColors />} />
        <Route path="/reference" element={<ReferenceImageArea />} />
        <Route path="/sandbox" element={<SandBox />} />

      </Routes>
    </BrowserRouter>
  );
}

export default App;