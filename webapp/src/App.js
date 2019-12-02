import React, { useState } from "react"
import { library as fontAwesomeLibrary } from "@fortawesome/fontawesome-svg-core"
import { faMinus, faPlus } from "@fortawesome/free-solid-svg-icons"

import Inventory from "./Inventory.jsx"
import { communalItemNames, garrettItemNames } from "./ItemLists"
import "./App.css"

fontAwesomeLibrary.add(faMinus, faPlus)

function App() {
  // Raspberry Pi touchscreen resolution is 800 x 480

  const [garrettItemsVisible, setGarrettItemsVisible] = useState(false)

  const toggleGarrettItemsVisible = () =>
    setGarrettItemsVisible(!garrettItemsVisible)

  return (
    <div className="App">
      <div className="inventoryHeader">Communal Snack Items</div>
      <Inventory itemNames={communalItemNames} />
      <div className="inventoryHeader">
        <button
          className="showButton"
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
