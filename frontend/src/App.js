import './App.css';
import { Routes, Route } from "react-router-dom";

import Navbar from './components/NavBar';

import Model from './routes/Model'
import Axios from "axios";

Axios.defaults.baseURL = "http://127.0.0.1:8000/api/";

const App = () => {
  return (
    <>
      <Navbar />
      <Routes>
        <Route exact path="/" element={<Model />} />
      </Routes>
    </>
  )
}

export default App;
