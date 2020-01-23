import React from 'react'
import { FontAwesomeIcon } from '@fortawesome/react-fontawesome'

import { roundToOne } from './numbers'

const ItemCount = ({ count, name }) => {
  return (
    <span className="pure-u-3-4 countNumber">
      {displayCount(count)} {displayName(name, count)}
    </span>
  )
}
export default ItemCount

const displayCount = function(count) {
  if (typeof count === 'undefined') {
    return <FontAwesomeIcon icon="spinner" pulse />
  } else if (count === null) {
    return '??'
  } else {
    return roundToOne(count)
  }
}

const displayName = (name, count) => {
  if (count === 1 && name.endsWith('s')) {
    return name.slice(0, -1)
  }
  return name
}

// vim: set ts=2 sw=2 sta sts=2 sr et ai:
