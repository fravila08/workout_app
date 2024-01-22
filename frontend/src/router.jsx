import { createBrowserRouter } from "react-router-dom";
import App from "./App";
import HomePage from "./pages/HomePage.jsx";
import RegisterPage from "./pages/RegisterPage.jsx";
import CalendarPage from "./pages/CalendarPage.jsx";

const router = createBrowserRouter([
  {
    path: "/",
    element: <App />,
    children: [
      {
        index: true,
        element: <HomePage />,
      },
      {
        path: "users",
        element: <RegisterPage />,
      },
      {
        path:"calendar",
        element:<CalendarPage />
      }
    ],
  },
]);

export default router;
