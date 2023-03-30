import React, {useState} from 'react';
import axios from "axios";

const SignUp = () => {

  const [name, setName] = useState("");
  const [email, setEmail] = useState("");
  // const [phone, setPhone] = useState("");
  const [password, setPassword] = useState("");

  // const [data, setData] = useState({
  //   name : '',
  //   email: '',
  //   password: ''
  // });

  // const inputHandler = (e) => {
  //   setData({...data, data : e.target.value})
  //   console.log(data);
  // }

 const submitHandler = (e) => {
  e.preventDefault();
  axios.post('http://127.0.0.1:8000/api/login/', {
    name, email, password
  }).then(response => {
    console.log(response)
  }).catch((err) => {
    console.log(err);
  })
 };
 
  return (
   <div className='signupcontainer'>
   <div className='signUp'>Sign Up</div>
     <form onSubmit={submitHandler}>
     <input type="text" placeholder='User Name'  autoComplete="off" onChange = {(e) => setName(e.target.value)} value={name}  />
           <input type="text" placeholder='email' autoComplete="off" onChange = {(e) => setEmail(e.target.value)} value={email}   />
           <input type="text" placeholder='password'  autoComplete="off" onChange = {(e) => setPassword(e.target.value)} value={password} />
           <button type='Submit'>Register</button>
     </form>
   </div>
  )
}

export default SignUp
