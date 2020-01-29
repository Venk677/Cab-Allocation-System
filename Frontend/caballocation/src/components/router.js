import { Route } from "react-router-dom";
import Home from './home';
import User from './Users';
import Driver from './Driver';
import React, { Component } from 'react'
import Setting from './settings'

class BasicRouter extends Component {
    render() {
        return (
            <div>
             <Route exact path = "/" component={Home}/>   
             <Route exact path = "/user" component ={User}/>
             <Route exact path ="/driver" component ={Driver} />
             <Route exact path ="/settings" component= {Setting} />
            </div>
        )
    }
}
export default BasicRouter;
