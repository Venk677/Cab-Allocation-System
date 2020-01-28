import React, { Component } from 'react';
import Home from './components/home'
import './App.css';
import BasicRouter from './components/router';
import { BrowserRouter } from "react-router-dom";

class App extends Component {
  render() {
    return (
      <div>
        <BrowserRouter>
          <BasicRouter/>
        </BrowserRouter>
      </div>
      
    );
  }
}

export default App;
