import React, { useState } from "react"

const Counter = () => {
  const [count, setCountState] = useState(5)

  const setCount = (newCount) => (
    () => {
      const nonNegCount = Math.max(newCount, 0)
      setCountState(nonNegCount)
      fetch(`/api?name=apples&count=${nonNegCount}`)
    }
  )

  return <>
    <button onClick={setCount(count - 1)}>-</button>
    <span>{count}</span>
    <button onClick={setCount(count + 1)}>+</button>
  </>
}
export default Counter


// vim: set ts=2 sw=2 vts=2 sta sts=2 sr et ai:
