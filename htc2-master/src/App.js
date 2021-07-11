import { cargo } from 'async';
import React, {useState, Suspense} from 'react';
import { BrowserRouter as Router, Switch, Link, Route, useRouteMatch, NavLink } from 'react-router-dom';
import './App.css';

const Dashboard = React.lazy(()=>import('./Dash.js'));

function Home(){

  return (
    <div className="contentWrapper" id="homeWrapper">
      <div className="highlightDiv">
      <h2>Welcome to APPNAME</h2>
      <h3>A Ridesharing Delivery App for Local Businesses and Drivers</h3>
      <Link to="/register" className="buttonLink">Register Now</Link>
      </div>
    </div>
  )
}

function About() {

  return (
    <div className="contentWrapper">
    <h2>About</h2>
    </div>
  )
}

function Register() {

  const [password, changePassword] = useState("")
  const [password2, changePassword2] = useState("")

  const handleSubmit = (evt) => {
    if (password != password2) {
      evt.preventDefault();
      alert("Passwords do not match! Please try again.")
    }
  }

  return (
    <div class="contentWrapper">
    <h2>Register</h2>
    <form onSubmit={handleSubmit}>
      <input type="text"
        name="username"
        placeholder="username"
      ></input> <br />
      <input type="password"
        name="password"
        placeholder="password"
        value={password}
        onChange={(e)=> changePassword(e.target.value)}
      ></input> <br />
      <input type="password"
        name="confirmp"
        placeholder="confirm password"
        value={password2}
        onChange={(e)=> changePassword2(e.target.value)}
      ></input> <br />
      <input type="submit" value="Submit" class="buttonLink"></input>
    </form>
    </div>
  )
}

function App() {

  const [loggedIn, setLoggedIn] = useState(false);
  const setHome = () => {

  }

  return (
    <Router>
      <Suspense fallback={<h2>Loading...</h2>}>
      <div>
      <div className="App">
      <div id="header">
        <h1>Our App</h1>
        <span />
        <NavLink to="/" exact={true} activeClassName="activeNavLink" className="navLink">Home</NavLink>
        <NavLink to="/dash" className="navLink" activeClassName="activeNavLink">Dashboard</NavLink>
        <NavLink to="/about" className="navLink" activeClassName="activeNavLink">About</NavLink> 
      </div>
    </div>
    <Switch>
    <Route exact path="/">
        <Home />
      </Route>
      <Route path="/dash">
        <Dashboard />
      </Route>
      <Route path="/about">
        <About />
      </Route>
      <Route path="/register">
        <Register/>
      </Route>
    </Switch>
    </div>
    </Suspense>
    </Router>
  );
}

export default App;
