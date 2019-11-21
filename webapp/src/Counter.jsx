import React, { useState } from "react"

const Counter = ({ name }) => {
  const [count, setCountState] = useState(5)

  const setCount = (newCount) => (
    () => {
      const nonNegCount = Math.max(newCount, 0)
      setCountState(nonNegCount)
      fetch(`/api?name=${name.toLowerCase()}&count=${nonNegCount}`)
    }
  )

  return <>
    <button
      className="countButton"
      onClick={setCount(count - 1)}
    >
      &minus;
    </button>
    <span className="countNumber">{count}</span>
    <button
      className="countButton"
      onClick={setCount(count + 1)}
    >
      &#43;
    </button>
  </>
}
export default Counter


// vim: set ts=2 sw=2 vts=2 sta sts=2 sr et ai:
