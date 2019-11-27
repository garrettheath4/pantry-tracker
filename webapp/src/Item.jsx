import React from "react"
import Counter from "./Counter"

const ItemRow = ({ name }) => {
  return (
    <tr>
      <td>{name}</td>
      <td>
        <Counter name={name} />
      </td>
    </tr>
  )
}
export default ItemRow


// vim: set ts=2 sw=2 vts=2 sta sts=2 sr et ai:
