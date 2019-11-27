import React, { useState, useEffect } from "react"
import ItemCount from "./ItemCount"

let apiFetchInvalidWarned = false

const Item = ({ name }) => {
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
            if (!apiFetchInvalidWarned) {
              console.log("Invalid response when fetching inventory from API.",
                "Are we in DEV mode?")
              apiFetchInvalidWarned = true
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
            const resStr = String(res)
            if (resStr.includes("</html>")) {
              console.log("Warning: Received HTML response from API instead of",
                "expected response of", nonNegCount)
            } else {
              console.log("Warning: Did not receive expected response of",
                nonNegCount, "from API")
            }
          }
        })
        .catch(err => console.log("Unable to set item count through API", err))
    }
  )

  return (
    <div className="pure-u-2-5">
      <button
        className="pure-button"
        onClick={setCount(count - 1)}
      >
        <i className="fas fa-minus" />
      </button>
      <ItemCount count={count} name={name} />
      <button
        className="pure-button"
        onClick={setCount(count + 1)}
      >
        <i className="fas fa-plus" />
      </button>
    </div>
  )
}
export default Item


// vim: set ts=2 sw=2 vts=2 sta sts=2 sr et ai:
