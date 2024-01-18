import { useEffect, useState } from "react";
import { Outlet } from "react-router-dom";
import { api } from "./utilities";
import "./App.css";
import Button from "react-bootstrap/esm/Button";
import NavBar from "./components/NavBar";

function App() {
  const [user, setUser] = useState(null);

  const getInfo = async () => {
    let response = await api.get("users/info/");
    if (response.status === 200) {
      setUser(response.data.user.username);
    }
  };

  const logOut = async () => {
    let response = await api.post("users/logout/");
    if (response.status === 200) {
      delete api.defaults.headers.common["Authorization"];
      localStorage.removeItem("token");
      setUser(null);
    }
  };

  useEffect(() => {
    let token = localStorage.getItem("token");
    if (token) {
      api.defaults.headers.common["Authorization"] = token;
      getInfo();
    }
  }, []);

  return (
    <>
      <NavBar />
      <h1>Welcome{user ? ` ${user}` : null}!</h1>
      {user ? <Button onClick={logOut}>Log Out</Button> : null}
      <Outlet context={{ user, setUser }} />
    </>
  );
}

export default App;
