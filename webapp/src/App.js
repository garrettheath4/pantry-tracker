import React, { useState } from "react"
import Inventory from "./Inventory.jsx"
import { communalItemNames, garrettItemNames } from "./ItemLists"
import "./App.css"

function App() {
  // Raspberry Pi touchscreen resolution is 800 x 480

  const [garrettItemsVisible, setGarrettItemsVisible] = useState(false)

  const toggleGarrettItemsVisible = () =>
    setGarrettItemsVisible(!garrettItemsVisible)

  return (
    <div className="App">
      <div className="greeting">
        What food do we have? We'll order more if we get low.
      </div>
      <div className="inventoryHeader">Communal Items</div>
      <Inventory itemNames={communalItemNames} />
      <button
        className="pure-button inventoryHeader"
        onClick={toggleGarrettItemsVisible}
      >
        Show Garrett's items
      </button>
      {garrettItemsVisible
      && <Inventory itemNames={garrettItemNames} />}
    </div>
  )
}

export default App
