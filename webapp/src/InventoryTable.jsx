import React from "react"
import ItemRow from "./ItemRow.jsx"

const InventoryTable = () => {
  return (
    <table className="pure-table">
      <thead>
        <tr>
          <th>Item</th>
          <th>Qty</th>
        </tr>
      </thead>
      <tbody>
        <ItemRow name="Apples" />
        <ItemRow name="Bananas" />
      </tbody>
    </table>
  )
}
export default InventoryTable

// vim: set ts=2 sw=2 vts=2 sta sts=2 sr et ai:
