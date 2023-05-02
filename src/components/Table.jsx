import React from 'react'
import { useEffect } from 'react';
import { useState } from 'react';
import DayTable from './DayTable';
var days = [
    'Воскресенье',
    'Ponedelnik',
    'Vtornik',
    'Sreda',
    'Chetverg',
    'Pyatnica',
    'Sybbota'
    ];
var d = new Date();
var n = d.getDay();

export default function Table() {
    const [error, setError] = useState(null);
    const [isLoaded, setIsLoaded] = useState(false);
    const [week, setWeek] = useState('ЗАГРУЗКА')
    const [items, setItems] = useState([]);
    useEffect(() => {
      fetch("http://192.168.0.94:5000/week/")
          .then(res => res.json())
          .then(
            (result) => {
              setWeek(result["week"])
            },
            (error) => {
              setIsLoaded(true);
              setError(error);
            }
          );
        fetch("http://192.168.0.94:5000/table/")
          .then(res => res.json())
          .then(
            (result) => {
              setIsLoaded(true);
              setItems(result);
            },
            (error) => {
              setIsLoaded(true);
              setError(error);
            }
          )
          
      }, [])
  return (
    <div>
      Расписание для недели {week}
        <ul >
            {items.map(item => (
            <li key={item.id} style={{verticalAlign: 'top'}}>
                <DayTable
                days = {item.days}
                table = {item.table}
                />
            </li>
            
            ))}
            
        </ul>
    </div>
  )
}
