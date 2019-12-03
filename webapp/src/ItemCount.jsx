import React from "react"
import { FontAwesomeIcon } from "@fortawesome/react-fontawesome"

const ItemCount = ({ count, name }) => {
  const countDisplay = typeof count === 'undefined'
    ? <FontAwesomeIcon icon="spinner" pulse />
    : count
  return <span className="pure-u-3-4 countNumber">{countDisplay} {name}</span>
}
export default ItemCount


// vim: set ts=2 sw=2 vts=2 sta sts=2 sr et ai:
