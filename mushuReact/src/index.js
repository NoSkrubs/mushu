//Components
import React, { Component } from 'react';
import ReactDOM from 'react-dom';
import { BrowserRouter, Route, Link } from 'react-router-dom';
import registerServiceWorker from './registerServiceWorker';

//Modules
import App from './App';
import About from './About';

//CSS
import './index.css';

ReactDOM.render(
  <BrowserRouter>
    <div>
      <Route exact path="/" component={App}/>
      <Route path="/about" component={About}/>
    </div>
  </BrowserRouter>
  , document.getElementById('root')
);

registerServiceWorker();
