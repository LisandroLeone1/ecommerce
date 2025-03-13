import { BrowserRouter as Router, Route, Routes } from "react-router-dom";
import ProductDetail from "./ProductoDetail";


function App() {
  return (
    <Router>
      <Routes>
        <Route path="/producto/:id" element={<ProductDetail />} />
      </Routes>
    </Router>
  );
}

export default App;

