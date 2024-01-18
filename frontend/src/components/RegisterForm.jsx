import { useState, useEffect } from "react";
import { isValidPassword, registerOrLogIn } from "../utilities";
import Button from "react-bootstrap/Button";
import Form from "react-bootstrap/Form";
import { useOutletContext } from "react-router-dom";

const RegisterForm = () => {
  const [type, setType] = useState(false);
  const [password, setPassword] = useState("");
  const [email, setEmail] = useState("");
  const [userName, setUserName] = useState("");
  const [valid, setValid] = useState(false);
  const [register, setRegister] = useState(true);
  const { setUser } = useOutletContext();

  useEffect(() => {
    setValid(isValidPassword(password));
  }, [password]);

  return (
    <Form
      onSubmit={async (e) => [
        setUser(
          await registerOrLogIn(e, register, email, userName, password, valid)
        ),
        setEmail(""),
        setPassword(""),
        setUserName(""),
        setValid(false),
        setType(false),
      ]}
    >
      {register ? (
        <Form.Group className="mb-3" controlId="formBasicEmail">
          <Form.Label>Email address</Form.Label>
          <Form.Control
            type="email"
            placeholder="Enter email"
            onChange={(e) => setEmail(e.target.value)}
            value={email}
          />
          <Form.Text className="text-muted">
            We'll never share your email with anyone else.
          </Form.Text>
        </Form.Group>
      ) : null}

      <Form.Group className="mb-3" controlId="formBasicUserName">
        <Form.Label>User Name</Form.Label>
        <Form.Control
          type="text"
          placeholder="Enter your user name"
          onChange={(e) => setUserName(e.target.value)}
          value={userName}
        />
        <Form.Text className="text-muted">
          This is the username you'll need to log in to your account.
        </Form.Text>
      </Form.Group>

      <Form.Group className="mb-3" controlId="formBasicPassword">
        <Form.Label>Password</Form.Label>
        <Form.Control
          type={type ? "text" : "password"}
          placeholder="Password"
          style={{ borderColor: valid ? "green" : "red" }}
          onChange={(e) => setPassword(e.target.value)}
          value={password}
        />
        <Form.Text className="text-muted">
          Your password must be a minimum of 6 characters and contain 1 special
          character and 1 number.
        </Form.Text>
      </Form.Group>
      <Form.Group className="mb-3" controlId="formBasicCheckbox">
        <Form.Check
          type="checkbox"
          label="view"
          onChange={(e) => setType(e.target.checked)}
        />
      </Form.Group>
      <Button onClick={(e) => setRegister(!register)}>
        {register ? "Sign In" : "Sign Up"}
      </Button>
      <Button variant="primary" type="submit">
        Submit
      </Button>
    </Form>
  );
};

export default RegisterForm;
