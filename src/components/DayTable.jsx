import React from 'react'
import '../css/DayTable.css'
export default function DayTable({days, table}) {
  return (
    <div>
        <div>{days}</div>
        {table.map(item => (
        
          <li key={1}>
            {item.time} {item.pred}
          </li>
        
        ))}
    </div>
  )
}
