import axios from "axios";

export const api = axios.create({
  baseURL: import.meta.env.VITE_BASE_URL,
});

export const isValidPassword = (password) => {
  // Check if the password is at least 6 characters long
  if (password.length < 6 || password.length > 8) {
    return false;
  }
  // Check if the password contains at least 1 special character and 1 number
  const specialCharacterPattern = /[@_!#$%^&*()<>?/\|}{~:]/;
  const numberPattern = /\d/;
  if (
    !specialCharacterPattern.test(password) ||
    !numberPattern.test(password)
  ) {
    return false;
  }
  return true;
};

export const registerOrLogIn = async (
  event,
  registerStatus,
  email,
  username,
  password,
  validPassword
) => {
  event.preventDefault();
  if (!validPassword) {
    return null;
  }
  try {
    let body = {
      email: email,
      username: username,
      password: password,
    };
    //@#12ab
    console.log(body);
    let response = await api.post(
      registerStatus ? "users/" : "users/login/",
      body
    );
    if (response.data.status === 200 || response.data.status === 201) {
      let token = `Token ${response.data.token}`;
      api.defaults.headers.common["Authorization"] = token;
      localStorage.setItem("token", token);
      console.log(response);
      return response.data.user;
    }
  } catch (err) {
    console.error(err);
    alert(err.message || "An error occurred.");
  }
  return null;
};
