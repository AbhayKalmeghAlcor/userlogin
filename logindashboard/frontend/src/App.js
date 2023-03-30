
import './App.css';
import Header from './Components/Header';
import Home from './Components/Home';
import Login from './Components/Login';
import SignUp from './Components/SignUp';
import {BrowserRouter as Router,Routes, Route} from 'react-router-dom'

function App() {
  return (
    <Router>
      <Header/>
      <Routes>
        <Route path='/' element = {<Home/>}/>
        <Route path='/login' element = {<Login/>}/>
        <Route path='/signup' element = {<SignUp/>}/>
      </Routes>
    </Router>
  )
}

export default App;
