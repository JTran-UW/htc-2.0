import { cargo } from 'async';
import React, {useState, Suspense} from 'react';
import { BrowserRouter as Router, Switch, Link, Route, useRouteMatch, NavLink } from 'react-router-dom';
import './App.css';

function Rides(){

    var availableRides = [{vehicleType: "car"}]
  
    return (
      <div className="contentWrapper">
        <h2>Get a Ride</h2>
        {availableRides.map(()=>{
  
        })}
      </div>
    )
  }
  
  function GiveForm(){
    return (
      <div class="contentWrapper">
        <h2>Give a Ride</h2>
      <div>
      <form>
      <h4>Vehicle Type </h4>
        <input type="radio" name="vehicleType" id="vehicleType1"/>
        <label for="vehicleType1">Car/Van</label>
  
        <input type="radio" name="vehicleType" id="vehicleType2"/>
        <label for="vehicleType2">Truck</label>
       
        <h4> Location </h4>
        <input type="text"
          name="location"
          placeholder="Enter location here"
        />
        
        <h4> Dates Available </h4>
        <input type="date"
          name="beginDate"
        />
        <input type="date"
          name="endDate"
        />
  
        <h4> Location </h4>
        <input type="text"
          name="location"
          placeholder="Enter location here"
        />
  
        <h4> Pricing Model </h4>
        <input type="radio" name="pricingModel" id="pricingModel1"/>
        <label for="pricingModel1">Per mile</label>
  
        <input type="radio" name="pricingModel" id="pricingModel2"/>
        <label for="pricingModel2">Per Hour</label>
  
        <h4> Price </h4>
        <input type="number"
          name="price"
        /> <label for="price"> Dollars per mile</label>
  
        <h4> Max Load </h4>
        <input type="text"
          name="maxLoad"
        />
  
        <h4> size </h4>
        <input type="text"
          name="size"
          placeholder="Enter location here"
        /> <label for="size"> cubic ft</label>
      </form>
      <button /*onClick={onsubmit()}*/>submit</button>
      </div>
      </div>
    )
  }
  
  function RequestForm(){
    return (
      <div class="contentWrapper">
        <h2>Request a Ride</h2>
      <div>
      <form>
      <h4>Vehicle Type </h4>
        <input type="radio" name="vehicleType" id="vehicleType1"/>
        <label for="vehicleType1">Car/Van</label>
  
        <input type="radio" name="vehicleType" id="vehicleType2"/>
        <label for="vehicleType2">Truck</label>
       
        <h4> Location </h4>
        <input type="text"
          name="location"
          placeholder="Enter location here"
        />
        
        <h4> Dates Available </h4>
        <input type="date"
          name="beginDate"
        />
        <input type="date"
          name="endDate"
        />
  
        <h4> Location </h4>
        <input type="text"
          name="location"
          placeholder="Enter location here"
        />
  
        <h4> Pricing Model </h4>
        <input type="radio" name="pricingModel" id="pricingModel1"/>
        <label for="vehicleType1">Per mile</label>
  
        <input type="radio" name="pricingModel" id="pricingModel2"/>
        <label for="vehicleType2">Per Hour</label>
  
        <h4> Price </h4>
        <input type="number"
          name="price"
        /> <label for="price"> Dollars per mile</label>
  
        <h4> Max Load </h4>
        <input type="text"
          name="maxLoad"
        />
  
        <h4> size </h4>
        <input type="text"
          name="size"
          placeholder="Enter location here"
        /> <label for="size"> cubic ft</label>
      </form>
      <button /*onClick={onsubmit()}*/>submit</button>
      </div>
      </div>
    )
  }

export default function Dashboard() {
    let match = useRouteMatch();
  
    return (
      <div className="flexxer">
        <div className="sidebar">
          <NavLink to={`${match.url}/get`} activeClassName="activeSideLink" className="sideLink">GET A RIDE</NavLink>
          <NavLink to={`${match.url}/give`} activeClassName="activeSideLink" className="sideLink">GIVE A RIDE</NavLink>
          <NavLink to={`${match.url}/request`} activeClassName="activeSideLink" className="sideLink">REQUEST A RIDE</NavLink>
            <span />
        </div>
        <div>
        <Switch>
          <Route path={`${match.path}/get`}>
            <Rides />
          </Route>
          <Route path={`${match.path}/give`}>
            <GiveForm />
          </Route>
          <Route path={`${match.path}/request`}>
            <RequestForm />
          </Route>
          <Route path={`${match.path}`}>
            <Rides />
          </Route>
      </Switch>
      </div>
      </div>
    )
  }