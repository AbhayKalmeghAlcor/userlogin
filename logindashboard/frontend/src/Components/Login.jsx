import React, { useState, useEffect} from 'react'
import axios from "axios";

const Login = () => {

 const [email, setEmail] = useState("");
 const [password, setPassword] = useState("");

 const [data, setData] = useState([]);

 const submitHandler = (e) => {
  e.preventDefault();
  setData([...data, {email, password}])
  setEmail("");
  setPassword("");
  console.log(data)
 };

useEffect(() => {
  getUsers();
}, [])

const getUsers = async () => {
  const loginApi = await axios.get('http://127.0.0.1:8000/api/login/')
  console.log(loginApi.data);
}

  return (
    <div className='container'> 
    <div className='signIn'>Sign In</div>
      <form onSubmit={submitHandler}>
         <input type="text" placeholder='Email' value={email} onChange = {(e) => {setEmail(e.target.value)}} />
         <input type="password" placeholder='Password' value={password} onChange = {(e) => {setPassword(e.target.value)}}/>
         <button type='Submit'>Login</button>
      </form>
    </div>
  )
}

export default Login

//  const initialArray = localStorage.getItem("data")? JSON.parse(localStorage.getItem("data")) : [];
//  useEffect(() => {
//   localStorage.setItem("data", JSON.stringify(data));
//  }, [data])
 