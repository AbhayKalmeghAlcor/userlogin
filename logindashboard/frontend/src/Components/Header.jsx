import React from 'react';
import { Link } from 'react-router-dom';

const Header = () => {
  return (
    <div>
      <nav>
        <p>Header</p>
        <div className='links'>
        <Link to="/login">Login</Link>
        <Link to="/signup">SignUp</Link>
      </div>
      </nav>    
    </div>
  )
}

export default Header