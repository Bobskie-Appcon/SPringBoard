import React from "react";
import { Routes, Route } from "react-router-dom";
import Login from "./pages/Login";
import LandingPage from "./pages/LandingPage";
import Register from "./pages/Register";
import RequireAuth from "./components/Authentication/RequireAuth";
import S_Dashboard from "./pages/S_Dashboard";

function App() {
  return (
    <Routes>
      <Route path="/" exact element={<LandingPage />} />
      <Route path="/login" element={<Login choose={0} />} />
      <Route path="/login-student" element={<Login choose={1} />} />
      <Route path="/login-teacher" element={<Login choose={2} />} />
      <Route path="/login-admin" element={<Login choose={3} />} />
      <Route path="/register" element={<Register choose={0} />} />
      <Route path="/register-student" element={<Register choose={1} />} />
      <Route path="/register-teacher" element={<Register choose={2} />} />

      <Route path="/student/join-group" element={<Register choose={3} />} />
      <Route path="/student/create-group" element={<Register choose={4} />} />
      <Route path="/group/:groupid">
        <Route
          index={true}
          element={
            <RequireAuth>
              <S_Dashboard choose={0} />
            </RequireAuth>
          }
        />
        <Route
          path="project/:projectid"
          index={true}
          element={
            <RequireAuth>
              <S_Dashboard choose={0} />
            </RequireAuth>
          }
        />
      </Route>
    </Routes>
  )
}

export default App
