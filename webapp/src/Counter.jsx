import React, { useState, useEffect } from "react"

let invalidApiWarned = false

const Counter = ({ name }) => {
  const [count, setCountState] = useState(0)

  useEffect(() => {
    async function fetchData() {
      const res = await fetch(`/api?name=${name.toLowerCase()}`)
      res
        .text()
        .then(res => {
          const num = Number(res)
          if (!Number.isNaN(num)) {
            setCountState(Number(res))
          } else {
            if (!invalidApiWarned) {
              console.log("Invalid response from API. Are we in DEV mode?")
              invalidApiWarned = true
            }
          }
        })
        .catch(err => console.log("Unable to fetch count for", name, ".", err))
    }

    // noinspection JSIgnoredPromiseFromCall
    fetchData();
  })

  const setCount = (newCount) => (
    () => {
      const nonNegCount = Math.max(newCount, 0)
      setCountState(nonNegCount)
      fetch(`/api?name=${name.toLowerCase()}&count=${nonNegCount}`)
        .then(res => res.text())
        .then(res => {
          if (nonNegCount !== Number(res)) {
            console.log("Warning: Got", res.text(), "from API but expected",
              nonNegCount)
          }
        })
        .catch(err => console.log("Unable to set item count through API", err))
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
