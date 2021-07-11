import { cargo } from 'async';
import React, {useState, Suspense, createContext, useContext} from 'react';
import { BrowserRouter as Router, Switch, Link, Route, Redirect, NavLink, useLocation } from 'react-router-dom';
import './App.css';

const Dashboard = React.lazy(()=>import('./Dash.js'));

const authContext = createContext();

function ProvideAuth({ children }) {
  const auth = useProvideAuth();
  return (
    <authContext.Provider value={auth}>
      {children}
    </authContext.Provider>
  );
}

function useAuth() {
  return useContext(authContext);
}

function useProvideAuth() {
  const [user, setUser] = useState(null); 

  // Define const signin
  // Define const signout

  return {user /*signin, signout*/}
}

function PrivateRoute({ children, ...rest}) {
  let auth = useAuth();
  return (
  <Route {...rest}
    render={({location}) =>
      auth.user ? (children):<Redirect to={{pathname: "/login", state: {from: location}}} /> }
  />
  )
};

function Login() {
  let auth= useAuth();

  let login = () => {
    // if authenticated
    auth.signin()
  }

  return (
    <div class="contentWrapper">
    <h2>Login</h2>
    <form>
      <input type="text"
        name="username"
        placeholder="username"
      ></input> <br />
      <input type="password"
        name="password"
        placeholder="password"
      ></input> <br />
      <input type="submit" value="Submit" class="buttonLink"></input>
    </form>
    </div> )
}

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
    } else {

    }
  }

  return (
    <div class="contentWrapper">
    <h2>Register</h2>
    <form action="https://htc-hacks.herokuapp.com/api/users/" method="POST">
    <input type="text"
        name="first"
        placeholder="First Name"
      ></input>
      <input type="text"
        name="last"
        placeholder="Last Name"
      ></input> <br />
      <input type="text"
        name="bio"
        placeholder="Bio"
      ></input> <br />
      <input type="email"
        name="email"
        placeholder="Email"
      ></input> <br />
      <input type="tel"
        name="phone"
        placeholder="Phone Number"
      ></input> <br />
      <input type="password"
        name="password"
        placeholder="Password"
        /*value={password}
        onChange={(e)=> changePassword(e.target.value)}*/
      ></input> <br />
      <input type="password"
        name="confirmp"
        placeholder="Confirm Password"
        /*value={password2}
        onChange={(e)=> changePassword2(e.target.value)}*/
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
    <ProvideAuth>
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
      <PrivateRoute path="/dash">
        <Dashboard />
      </PrivateRoute>
      <Route path="/about">
        <About />
      </Route>
      <Route path="/register">
        <Register/>
      </Route>
      <Route path="/login">
        <Login/>
      </Route>
    </Switch>
    </div>
    </Suspense>
    </Router>
    </ProvideAuth>
  );
}

export default App;
