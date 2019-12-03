import React, { useState, useEffect } from "react"
import ItemCount from "./ItemCount"
import ItemButton from "./ItemButton"
import useDebounce from "./useDebounce"

let warnedAboutHtmlRespFromFetch = false

const Item = ({ item }) => {
  const { name } = item
  const plusFn = (x) => Math.max((x || 0) + (item.increment || 1), 0)
  const minusFn = (x) => Math.max((x || 0) - (item.decrement || 1), 0)

  const [count, setCountState] = useState(undefined)

  const debouncedCount = useDebounce(count, 1500)

  useEffect(() => {
    async function fetchData() {
      const url = `/api?name=${name.toLowerCase()}`
      const res = await fetch(url)
      res
        .text()
        .then(res => {
          const num = Number(res)
          if (!Number.isNaN(num)) {
            setCountState(num)
          } else {
            if (!warnedAboutHtmlRespFromFetch) {
              warnedAboutHtmlRespFromFetch = true
              if (res.includes("</html>")) {
                console.log("Warning:", url, "-> HTML response (expected a number).",
                  "Is the API not running?")
              } else {
                console.log("Warning: received very unexpected response from",
                  ` API while fetching ${name.toLowerCase()}:`, res)
              }
            }
          }
        })
        .catch(err => console.log("Unable to fetch count for", name, ".", err))
    }

    // noinspection JSIgnoredPromiseFromCall
    fetchData()
  }, [name])

  useEffect(
    () => {
      if (typeof debouncedCount !== "undefined") {
        // noinspection JSIgnoredPromiseFromCall
        apiCommitCount(name, debouncedCount)
      }
    },
    [debouncedCount, name]
  )

  const countHandlerFactory = (deltaFn) => () => setCountState(deltaFn(count))

  return (
    <div className="pure-u-1-2 item">
      <ItemButton
        increments={true}
        onClickHandler={countHandlerFactory(plusFn)}
      />
      <ItemCount count={count} name={name} />
      <ItemButton
        increments={false}
        onClickHandler={countHandlerFactory(minusFn)}
      />
    </div>
  )
}
export default Item

function apiCommitCount(name, newCount) {
  const nonNegCount = Math.max(newCount || 0, 0)
  const url = `/api?name=${name.toLowerCase()}&count=${nonNegCount}`
  return fetch(url)
    .then(res => res.text())
    .then(res => {
      if (nonNegCount !== Number(res)) {
        const resStr = String(res)
        if (resStr.includes("</html>")) {
          console.log("Warning:", url, `-> HTML response (expected ${nonNegCount})`)
        } else {
          console.log("Warning: Did not receive expected response of",
            nonNegCount, "from API")
          console.log("Received:", resStr)
        }
      }
    })
    .catch(err => console.log("Unable to set item count through API", err))
}


// vim: set ts=2 sw=2 vts=2 sta sts=2 sr et ai:
