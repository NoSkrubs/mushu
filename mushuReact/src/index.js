//Components
import React, { Component } from 'react';
import ReactDOM from 'react-dom';
import { Router, Route, browserHistory, IndexRoute } from 'react-router';
import registerServiceWorker from './registerServiceWorker';

//Modules
import App from './App';
import About from './About';

//CSS
import './index.css';

ReactDOM.render(
  <Router history={hashHistory}>
    <Route path="/" component={App}/>
    <Route path="/about" component={About}/>
  </Router>
 , document.getElementById('root')
);

registerServiceWorker();
