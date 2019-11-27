import React from "react"

const ItemButton = ({ onClickHandler, increments }) => {
  return (
    <button
      className="pure-button"
      onClick={onClickHandler}
    >
      {increments
        ? <i className="fas fa-minus" />
        : <i className="fas fa-minus" />}
    </button>
  )
}

export default ItemButton