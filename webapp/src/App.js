import React, { useState } from "react"
import Inventory from "./Inventory.jsx"
import { communalItemNames, garrettItemNames } from "./ItemLists"
import "./App.css"

function App() {
  // Raspberry Pi touchscreen resolution is 800 x 480

  const [garrettItemsVisible, setGarrettItemsVisible] = useState(true)

  const toggleGarrettItemsVisible = () =>
    setGarrettItemsVisible(!garrettItemsVisible)

  return (
    <div className="App">
      <div className="inventoryHeader">Communal Items</div>
      <Inventory itemNames={communalItemNames} />
      <div className="inventoryHeader">
        <button
          className="pure-button"
          onClick={toggleGarrettItemsVisible}
        >
          Show Garrett's items
        </button>
      </div>
      {garrettItemsVisible
      && <Inventory itemNames={garrettItemNames} />}
    </div>
  )
}

export default App
