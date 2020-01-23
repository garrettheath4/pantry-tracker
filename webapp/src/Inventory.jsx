import React from 'react'
import classnames from 'classnames'

import Item from './Item.jsx'

const Inventory = ({ items }) => {
  return (
    <div
      className={classnames('pure-g', 'inventoryGrid', {
        inventoryGridSmall2: items.length < 3,
        inventoryGridSmall3: items.length === 3,
      })}
    >
      {items.map(item => (
        <Item item={item} key={item.name} />
      ))}
    </div>
  )
}
export default Inventory

// vim: set ts=2 sw=2 sta sts=2 sr et ai:
