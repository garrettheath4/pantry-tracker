import React from 'react'
import Inventory from './Inventory.jsx'
import './App.css'

function App() {
  return (
    <div className="App">
      <div className="pure-u">
        <div className="greeting">
          What food do we have? We'll order more if we get low.
        </div>
        <Inventory itemNames={["Apples", "Bananas"]} />
      </div>
    </div>
  )
}

export default App
