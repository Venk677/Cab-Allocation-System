import React, { Component } from 'react'
import {NavLink} from 'react-router-dom';
import axios from 'axios';

class Setting extends Component {
    constructor(props) {
      super(props)
    
      this.state = {
         username:"",
         drivername:"",
        }
        this.userSubmit = this.userSubmit.bind(this);
        this.driverSubmit = this.driverSubmit.bind(this);
    }


    driverSubmit =(drivername) =>{
        axios.post(`http://127.0.0.1:8000/drivers/`,{drivername})
        .then(res =>{
            console.log("Successfully posted",res.data);
        })
        .catch(err => console.log("Error",err))
        this.setState({
            drivername:""
        })
    }
    
    userSubmit =(username) =>{
        axios.post(`http://127.0.0.1:8000/users/`,{username})
        .then(res => {
            console.log("Successfully posted",res.data);
        })
        .catch(err => console.log("Error",err))
        this.setState({
            username:"",
        });
    }
    
  render() {
    return (
       <div className="driver-home">
                <div className="driver-header" >
                <NavLink to="/">Home</NavLink>
                <NavLink to="/driver">Driver</NavLink>
                <NavLink to="/user">User</NavLink>
                {/* For creating a new user  */}
                </div>
                <div style ={{marginTop:'100px'}}>
                    <input placeholder = "Please enter username" type="text" value={this.state.username} onChange={() => this.setState({username:event.target.value})} />
                </div>
                    <button onClick={() => this.userSubmit(this.state.username)}>Create</button>
                
                {/* For creating a new driver  */}
                <div style ={{marginTop:'100px'}}>
                    <input placeholder = "Please enter drivername" type="text" value={this.state.drivername} onChange={() => this.setState({drivername:event.target.value})} />
                </div>
                    <button onClick={() => this.driverSubmit(this.state.drivername)}>Create</button>
            
      </div>
    )
  }
}
export default Setting;