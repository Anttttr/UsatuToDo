import React from 'react'
import Select from 'react-select'
import { useState } from 'react'
const options = [
  { value: 'srv', label: 'Срочно и важно' },
  { value: 'nsrv', label: 'Несрочно и важно' },
  { value: 'srn', label: 'Срочно и не важно' },
  { value: 'nsrn', label: 'Несрочно и не важно' }
]

export default function Adder() {
  const [inp, setInp] = useState('')
  const [sel, setSel] = useState('')
  const handleClick = () => {
  console.log(inp, sel);
}
  return (
    
    <div>
      <div>
        <div style={{display:'inline'}}>
          <input value = {inp} onChange = {(event) => setInp(event.target.value)}/>
        </div>
      <div style = {{width: 230, display: 'inline-block', paddingLeft: 10}}>
        <Select options={options} onChange= {(e) => setSel(e.value)}/>
      </div>
      <button onClick={handleClick}>ASD</button>
      </div>
    </div>
  )
}
