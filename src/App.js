import logo from './logo.svg';
import './App.css';
import Home from './pages/Home'
import Todo from'./pages/Todo'
import Timetable from './pages/Timetable'
import { BrowserRouter, Routes, Route } from 'react-router-dom';
import Header from './components/Header';
import Adder from './pages/Adder';
function App() {
  return (
    <BrowserRouter>
     <Routes>
       <Route path="/" element={<Header />} >
          <Route index element={<Home />}/>
          <Route path="timetable" element={<Timetable />}/>
          <Route path="todo" element={<Todo />} />
          <Route path="adder" element={<Adder/>}/>
        </Route>
     </Routes>
   </BrowserRouter>
  );
}

export default App;
