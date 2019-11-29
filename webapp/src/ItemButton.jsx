import React from "react"

const ItemButton = ({ onClickHandler, increments }) => {
  return (
    <button
      className="pure-u-1-4 pure-button"
      onClick={onClickHandler}
    >
      {increments
        ? <i className="fas fa-minus" />
        : <i className="fas fa-minus" />}
    </button>
  )
}

export default ItemButton