import React from "react"
import { FontAwesomeIcon } from "@fortawesome/react-fontawesome"

const ItemButton = ({ onClickHandler, increments }) => {
  return (
    <div className="pure-u-1-8">
      <button
        className="pure-button countButton"
        onClick={onClickHandler}
      >
        {increments
          ? <FontAwesomeIcon size="2x" icon="plus" />
          : <FontAwesomeIcon size="2x" icon="minus" />}
      </button>
    </div>
  )
}

export default ItemButton