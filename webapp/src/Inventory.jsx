import React from "react"
import Item from "./ItemRow.jsx"

const Inventory = () => {
  return (
    <table className="pure-table">
      <thead>
        <tr>
          <th>Item</th>
          <th>Qty</th>
        </tr>
      </thead>
      <tbody>
        <Item name="Apples" />
        <Item name="Bananas" />
      </tbody>
    </table>
  )
}
export default Inventory

// vim: set ts=2 sw=2 vts=2 sta sts=2 sr et ai:
