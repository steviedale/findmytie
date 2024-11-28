import DisplayColors from "./components/DisplayColors";
import ReferenceImageArea from "./components/ReferenceImageArea";
import SandBox from "./components/SandBox";
import ShowListings from "./components/ShowListings";
import { BrowserRouter, Routes, Route } from "react-router-dom";


function App() {
  return (
    <BrowserRouter>
      <Routes>

        <Route path="/" element={<DisplayColors />} />
        <Route path="/reference" element={<ReferenceImageArea />} />
        <Route path="/sandbox" element={<SandBox />} />
        <Route path="/show-listings/:searchQueryId" element={<ShowListings />} />

      </Routes>
    </BrowserRouter>
  );
}

export default App;