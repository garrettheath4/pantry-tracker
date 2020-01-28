import React, { useState } from 'react'
import { library as fontAwesomeLibrary } from '@fortawesome/fontawesome-svg-core'
import {
  faMinus,
  faPlus,
  faSpinner,
} from '@fortawesome/free-solid-svg-icons'

import { apiAppUpdate, apiSystemRestart } from './system'
import Inventory from './Inventory.jsx'
import { communalItems, garrettItems } from './ItemLists'
import './App.css'

fontAwesomeLibrary.add(faMinus, faPlus, faSpinner)

function App() {
  // Raspberry Pi touchscreen resolution is 800 x 480

  const [garrettItemsVisible, setGarrettItemsVisible] = useState(false)

  const toggleGarrettItemsVisible = () =>
    setGarrettItemsVisible(!garrettItemsVisible)

  return (
    <div className="App">
      <h2 className="inventoryHeader">Snack Item Tracker</h2>
      <h5 className="inventorySubheader">
        Help us keep track of what snack items we have so we can know when to
        get more if we run low.
      </h5>
      <Inventory items={communalItems} />
      <div className="inventoryHeader">
        <button className="subtleButton" onClick={apiAppUpdate}>
          Pull, Build, & Refresh App
        </button>
        <button className="subtleButton bold" onClick={toggleGarrettItemsVisible}>
          {garrettItemsVisible
            ? "Hide Garrett's items"
            : "Show Garrett's items"}
        </button>
        <button className="subtleButton" onClick={apiSystemRestart}>
          Reboot this device
        </button>
      </div>
      {garrettItemsVisible && <Inventory items={garrettItems} />}
    </div>
  )
}

export default App
