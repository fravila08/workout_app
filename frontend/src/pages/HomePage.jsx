import logo from "../assets/2024.png";

const HomePage = () => {
  return (
    <>
      <h1>HomePage</h1>
      <div>
        <img src={logo} style={{ float: "left" }} />
        <p>
          Are you tired of the same monotonous workouts and struggling to stay
          motivated on your fitness journey? Look no further! Introducing our
          revolutionary fitness app that goes beyond the ordinary, providing you
          with the ultimate tool to sculpt your dream physique. Imagine creating
          personalized workouts tailored to your goals, seamlessly tracking your
          progress, and gaining access to visually immersive guides for each
          exercise – all at your fingertips. Whether you're a fitness enthusiast
          or a beginner, our app is designed to elevate your workout experience.
          Say goodbye to guesswork and hello to a dynamic, engaging fitness
          routine. It's time to transform your workouts, crush your fitness
          goals, and embrace a healthier, happier you. Download our app now and
          embark on a fitness journey like never before! Your dream body is just
          a tap away.
        </p>
      </div>
    </>
  );
};

export default HomePage;
