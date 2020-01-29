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
        
    }

    // componentDidMount(){
    //     axios.get("http://127.0.0.1:8000/users/")
    //       .then(res =>
    //         this.setState({
    //             user:res.data
    //         }))
    //         .catch(err => console.log("Error",err));
    // }

    
    render() {
        return (
            <div>
                
            </div>
        )
    }
}
export default User;