import React, { useState, useEffect } from "react"

import ItemCount from "./ItemCount"
import ItemButton from "./ItemButton"
import useDebounce from "./useDebounce"
import { minusDeltaGenerator, nonNegNum, plusDeltaGenerator } from "./numbers"

let warnedAboutHtmlRespFromFetch = false

const Item = ({ item }) => {
  const { name } = item
  const plusDelta = plusDeltaGenerator(item.increment)
  const minusDelta = minusDeltaGenerator(item.decrement)

  const [isInitialized, setIsInitialized] = useState(false)
  const [count, setCountState] = useState(undefined)

  const debouncedCount = useDebounce(count, 1500)

  async function fetchData() {
    const url = `/api?name=${name.toLowerCase()}`
    const res = await fetch(url)
    const resText = await res.text()
    const resNum = Number(resText)
    if (!Number.isNaN(resNum)) {
      setCountState(resNum)
    } else {
      if (!warnedAboutHtmlRespFromFetch) {
        warnedAboutHtmlRespFromFetch = true
        if (resText.includes("</html>")) {
          console.log("Warning:", url, "-> HTML response (expected a number).",
            "Is the API not running?")
        } else {
          console.log("Warning: received very unexpected response from",
            ` API while fetching ${name.toLowerCase()}:`, resText)
        }
      }
    }
  }

  useEffect(() => {
    // noinspection JSIgnoredPromiseFromCall
    fetchData()
  }, [])

  useEffect(
    () => {
      if (typeof debouncedCount !== "undefined") {
        if (isInitialized) {
          // noinspection JSIgnoredPromiseFromCall
          apiCommitCount(name, debouncedCount)
        } else {
          setIsInitialized(true)
        }
      }
    },
    [debouncedCount]
  )

  const countHandlerFactory = (deltaFn) => () => setCountState(deltaFn(count))

  return (
    <div className="pure-u-1-2 item">
      <ItemButton
        increments={true}
        onClickHandler={countHandlerFactory(plusDelta)}
      />
      <ItemCount count={count} name={name} />
      <ItemButton
        increments={false}
        onClickHandler={countHandlerFactory(minusDelta)}
      />
    </div>
  )
}
export default Item

function apiCommitCount(name, newCount) {
  const nonNegCount = nonNegNum(newCount)
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
