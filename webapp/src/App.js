import React from 'react'
import Inventory from './Inventory.jsx'
import './App.css'

function App() {
  const communalItemNames = [
    "Apples",
    "Bananas",
  ]
  const garrettItemNames = [
    "Tuna salad",
    "Bread",
    "Cheese",
    "Lettuce",
    "Mayonnaise",
    "Tuna cans",
    "Chopped veggies",
    "Relish (backup)",
    "Soylent Mocha drink",
    "Soylent Mint Choc drink",
    "Soylent Mocha powder",
    "Soy milk",
    "Chocolate syrup",
    "Cereal",
    "Coke (big)",
    "Coke (small)",
    "Coke Zero (small)",
    "Steamable meals",
    "Noodle bowls",
    "Protein bars",
    "Chip bags",
    "Dairy milk",
    "Peanut butter",
  ]
  return (
    <div className="App">
      <div className="greeting">
        What food do we have? We'll order more if we get low.
      </div>
      <div>Communal Items</div>
      <Inventory itemNames={communalItemNames} />
      <div>Show Garrett's items</div>
      <Inventory itemNames={garrettItemNames} />
    </div>
  )
}

export default App
