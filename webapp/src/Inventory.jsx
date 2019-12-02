import React from "react"
import classnames from "classnames";

import Item from "./Item.jsx"

const Inventory = ({ itemNames }) => {
  return (
    <div className={classnames(
      "pure-g",
      "inventoryGrid",
      { inventoryGridSmall: itemNames.length <= 2 }
    )}>
      {itemNames.map((itemName) => <Item name={itemName} key={itemName} />)}
    </div>
  )
}
export default Inventory

// vim: set ts=2 sw=2 vts=2 sta sts=2 sr et ai:
