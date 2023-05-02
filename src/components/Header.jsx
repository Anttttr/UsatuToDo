import { Outlet, Link } from "react-router-dom";
import '../css/Header.css'

const Header = () => {
  return (
    <div >
        <nav>
          <ul>
            <li>
              <Link style ={{paddingRight: 10}} to="/">Главная</Link>
            </li>
            <li>
              <Link style ={{paddingRight: 10}} to="/todo">Что нужно сделать</Link>
            </li>
            <li>
              <Link style ={{paddingRight: 10}} to="/timetable">Расписание</Link>
            </li>
            <li>
              <Link style ={{paddingRight: 10}} to="/adder">Добавить задание</Link>
            </li>
          </ul>
        </nav>
      <div className = "container">
        <Outlet />
      </div>
    </div>
  )
};

export default Header;