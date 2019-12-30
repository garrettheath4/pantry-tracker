import React, { useState } from 'react'
import { library as fontAwesomeLibrary } from '@fortawesome/fontawesome-svg-core'
import {
  faMinus,
  faPlus,
  faSpinner,
  faSync,
  faPowerOff,
} from '@fortawesome/free-solid-svg-icons'
import { FontAwesomeIcon } from '@fortawesome/react-fontawesome'

import { apiAppUpdate, apiSystemRestart } from './system'
import Inventory from './Inventory.jsx'
import { communalItems, garrettItems } from './ItemLists'
import './App.css'

fontAwesomeLibrary.add(faMinus, faPlus, faSpinner, faSync, faPowerOff)

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
          <FontAwesomeIcon icon="sync" />
        </button>
        <button className="subtleButton" onClick={toggleGarrettItemsVisible}>
          {garrettItemsVisible
            ? "Hide Garrett's items"
            : "Show Garrett's items"}
        </button>
        <button className="subtleButton" onClick={apiSystemRestart}>
          <FontAwesomeIcon icon="power-off" />
        </button>
      </div>
      {garrettItemsVisible && <Inventory items={garrettItems} />}
    </div>
  )
}

export default App
