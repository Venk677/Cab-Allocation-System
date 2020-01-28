import React, { Component } from 'react';
import  axios from 'axios';
import { NavLink } from 'react-router-dom';

class User extends Component {
    constructor(props) {
        super(props)
    
        this.state = {
             username : "",
             user : []
        }
        this.userSubmit = this.userSubmit.bind(this);
    }

    componentDidMount(){
        axios.get("http://127.0.0.1:8000/users/")
          .then(res =>
            this.setState({
                user:res.data
            }))
            .catch(err => console.log("Error",err));
    }
    userSubmit = (username) =>{
        axios.post(`http://127.0.0.1:8000/users/`, {
             username
    })
    .then(res => {
        console.log("Successful",res.data);
    })
    .catch(err => console.log("Error",err))
    this.setState({
        username : "",
    })
    }
    
    render() {
        return (
            <div className="driver-home">
                <div className="driver-header" >
                <NavLink to="/">Home</NavLink>
                <NavLink to="/driver">Driver</NavLink>
                {/* For creating a new user  */}
                </div>
                <div style ={{marginTop:'100px'}}>
                    <input type ="text" placeholder = "Enter User Name" value = {this.state.username} onChange = {() =>this.setState({ username : event.target.value})}></input>
                </div>
                <button onClick = {() => this.userSubmit(this.state.username)}>Create</button>
                {console.log("Recieving",this.state.username)}
            </div>
        )
    }
}
export default User;