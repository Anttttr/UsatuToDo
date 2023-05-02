import React, { Component } from 'react'
import List from '../components/List'

export default class Todo extends Component {
  render() {
    return (
    <div style = {{paddingInlineStart: 60}}>
      <List />
    </div>
    )
  }
}
