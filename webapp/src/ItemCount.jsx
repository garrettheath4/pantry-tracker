import React from "react"
import { FontAwesomeIcon } from "@fortawesome/react-fontawesome"

import { roundToOne } from "./numbers"

const ItemCount = ({ count, name }) => {
  return <span className="pure-u-3-4 countNumber">
    {displayCount(count)} {displayName(name, count)}
  </span>
}
export default ItemCount

const displayCount = (count) => (
  typeof count === 'undefined'
    ? <FontAwesomeIcon icon="spinner" pulse />
    : roundToOne(count)
)

const displayName = (name, count) => {
  if (count === 1 && name.endsWith("s")) {
    return name.slice(0, -1)
  }
  return name
}


// vim: set ts=2 sw=2 vts=2 sta sts=2 sr et ai:
