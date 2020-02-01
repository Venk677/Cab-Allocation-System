import React from "react";
import { NavLink } from "react-router-dom";
import "./components.css";
import image from '../images/Cab-booking.jpg';

class Home extends React.Component {
    render() {
        return (
            <div className="home">
                <div className="home-header">
                    <h1>Welcome To Cab Allocation System Application</h1>
                </div>
                <div style={{ display: 'flex', justifyContent: 'flex-start', flexDirection: 'row',  marginRight:200, marginLeft:50}}>
                {/* <div >   
                    <div style={{  width:'100%' ,height:'100%'}}>
                        <img src={image} alt="base" />
                    </div>      
                </div> */}
                <div className="home-content">
                    <div style={{fontSize:50, marginTop:20}}>Login as </div>
                    <div style={{fontSize:30, marginTop:20}}>
                    <NavLink to="user">User</NavLink>
                    </div>
                    <div style={{fontSize:20, marginTop:20, color:"red"}}>OR</div>
                    <div style={{fontSize:30, marginTop:20}}>
                    <NavLink to="driver">Driver</NavLink>
                    </div>
                    <div style={{fontSize:20, marginTop:20, color:"red"}}>OR</div>
                    <div style={{fontSize:30, marginTop:20}}>
                    <NavLink to="settings">Settings</NavLink>
                    </div>
                </div>
                </div>  
            </div>      
        )
    }
}

export default Home;