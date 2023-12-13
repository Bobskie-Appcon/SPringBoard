import React from "react";
import { Routes, Route } from "react-router-dom";
import Login from "./pages/Login";
import LandingPage from "./pages/LandingPage";


function App() {
  return (
    <Routes>
      <Route path="/landing" element={<LandingPage />} />
      <Route path="/" exact element={<Login choose={0} />} />
      <Route path="/login" element={<Login choose={0} />} />
      <Route path="/login-student" element={<Login choose={1} />} />
      <Route path="/login-teacher" element={<Login choose={2} />} />
      <Route path="/login-admin" element={<Login choose={3} />} />
    </Routes>
  )
}

export default App
