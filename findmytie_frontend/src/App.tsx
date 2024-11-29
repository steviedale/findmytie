import { BrowserRouter, Routes, Route } from "react-router-dom";

import SelectedColorsDisplay from "./components/SelectedColorsDisplay";
import ReferenceImageArea from "./components/ReferenceImageArea";
import QueryPage from "./components/QueryPage";
import SandBox from "./components/SandBox";
import ShowListings from "./components/ShowListings";
import MyComponent from "./components/TestWebsocket";


function App() {
  return (
    <BrowserRouter>
      <Routes>

        <Route path="/" element={<QueryPage />} />
        <Route path="/query-page" element={<QueryPage />} />
        {/* <Route path="/selected-colors-display" element={<SelectedColorsDisplay />} /> */}
        <Route path="/reference" element={<ReferenceImageArea />} />
        <Route path="/sandbox" element={<SandBox />} />
        <Route path="/show-listings/:searchQueryId" element={<ShowListings />} />
        <Route path="/test-websocket" element={<MyComponent />} />

      </Routes>
    </BrowserRouter>
  );
}

export default App;