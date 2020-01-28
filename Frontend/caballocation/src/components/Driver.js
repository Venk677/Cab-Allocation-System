import React, { Component } from 'react';
import { NavLink } from 'react-router-dom';
import axios from 'axios';


class Driver extends Component {
    constructor(props) {
        super(props)
    
        this.state = {
             driver :''
        }
    }

    driverSubmit(driver){
        axios.post(`http://127.0.0.1:8000/drivers/`,{
            driver 
        })
        .then(res => {
            this.setState({
                driver : res.data
            })
        })
    }
    
    render() {
        return (
            <div>
                <div>
                <div className="driver-home">
                   <div className="driver-header" >
                <h2>DRIVERS DETAILS</h2>
                <NavLink to = "/">Home</NavLink>
                <NavLink to = "/user">Users</NavLink>
                </div>
                <div className="driver-home">
                   <div className="driver-header" >
                   <div style ={{marginTop:'100px'}}>
                    <input type = "text" value={this.state.driver} onChange={()=>this.setState({driver:event.target.value})} />
                    <button onClick = {this.driverSubmit(this.state.driver)}>Create</button> 
                    {console.log("Recieving",this.state.driver)}
                    </div>
                </div>
            </div>
            </div>
            </div>
            </div>
        )
    }
}
export default Driver;