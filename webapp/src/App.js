import React from 'react'
import InventoryTable from './InventoryTable.jsx'
import './App.css'

function App() {
  return (
    <div className="App">
      <div className="pure-u">
        <div className="greeting">
          What food do we have? We'll order more if we get low.
        </div>
        <InventoryTable />
      </div>
    </div>
  )
}

export default App
