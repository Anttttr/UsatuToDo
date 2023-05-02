import React, { Component } from 'react'

export default class List extends Component {
  render() {
    return (
      <div>
        <div style = {{display: 'inline'}}>
            <div style = {{display: 'inline', paddingRight: 223}}>Важно и срочно</div>
            <div style = {{display: 'inline'}}>Важно и не срочно</div>
        </div>
        <div>
            <div style = {{display: 'inline', paddingRight: 200}}>Не важно и срочно</div>
            <div style = {{display: 'inline'}}>Не важно и не срочно</div>
        </div>
        </div>
    )
  }
}
