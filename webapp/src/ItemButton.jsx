import React from "react"

const ItemButton = ({ onClickHandler, increments }) => {
  return (
    <div className="pure-u-1-8">
      <button
        className="pure-button"
        onClick={onClickHandler}
      >
        {increments
          ? <i className="fas fa-minus" />
          : <i className="fas fa-minus" />}
      </button>
    </div>
  )
}

export default ItemButton