import React, { useState } from "react"

const Counter = () => {
  const [count, setCount] = useState(5)
  return <>
    <button onClick={() => setCount(Math.max(count - 1, 0))}>-</button>
    <span>{count}</span>
    <button onClick={() => setCount(Math.max(count + 1, 0))}>+</button>
  </>
}
export default Counter


// vim: set ts=2 sw=2 vts=2 sta sts=2 sr et ai:
