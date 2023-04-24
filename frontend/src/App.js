import './App.css';
import { Routes, Route } from "react-router-dom";

import Navbar from './components/NavBar';

import Home from './routes/Home';
import Model from './routes/Model'
import Axios from "axios";

Axios.defaults.baseURL = "http://127.0.0.1:8000/api/";

const App = () => {
  return (
    <>
      <Navbar />
      <Routes>
        <Route exact path="/" element={<Home />} />
        <Route exact path="/model" element={<Model />} />
      </Routes>
    </>
  )
}

export default App;
