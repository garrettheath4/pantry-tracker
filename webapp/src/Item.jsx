import React, { useState, useEffect } from 'react'

import ItemCount from './ItemCount'
import ItemButton from './ItemButton'
import useDebounce from './useDebounce'
import { minusDeltaGenerator, nonNegNum, plusDeltaGenerator } from './numbers'

let warnedAboutHtmlRespFromFetch = false

const Item = ({ item }) => {
  const { name: itemName } = item
  const plusDelta = plusDeltaGenerator(item.increment)
  const minusDelta = minusDeltaGenerator(item.decrement)

  const [count, setCountState] = useState(undefined)

  const debouncedCount = useDebounce(count, 1500)

  useEffect(() => {
    async function fetchData() {
      const url = `/api/item?name=${itemName.toLowerCase()}`
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
              if (res.includes('</html>')) {
                console.log(
                  'Warning:',
                  url,
                  '-> HTML response (expected a number).',
                  'Is the API not running?'
                )
              } else {
                console.log(
                  'Warning: received very unexpected response from',
                  ` API while fetching ${itemName.toLowerCase()}:`,
                  res
                )
              }
            }
          }
        })
        .catch(err =>
          console.log('Unable to fetch count for', itemName, '.', err)
        )
    }

    // noinspection JSIgnoredPromiseFromCall
    fetchData()
  }, [itemName])

  useEffect(() => {
    if (typeof debouncedCount !== 'undefined') {
      // noinspection JSIgnoredPromiseFromCall
      apiCommitCount(itemName, debouncedCount)
    }
  }, [debouncedCount, itemName])

  const countHandlerFactory = deltaFn => () => setCountState(deltaFn(count))

  return (
    <div className="pure-u-1-2 item">
      <ItemButton
        increments={true}
        onClickHandler={countHandlerFactory(plusDelta)}
      />
      <ItemCount count={count} name={itemName} />
      <ItemButton
        increments={false}
        onClickHandler={countHandlerFactory(minusDelta)}
      />
    </div>
  )
}
export default Item

function apiCommitCount(itemName, newCount) {
  const nonNegCount = nonNegNum(newCount)
  const url = `/api/item?name=${itemName.toLowerCase()}&count=${nonNegCount}`
  return fetch(url)
    .then(res => res.text())
    .then(res => {
      if (nonNegCount !== Number(res)) {
        const resStr = String(res)
        if (resStr.includes('</html>')) {
          console.log(
            'Warning:',
            url,
            `-> HTML response (expected ${nonNegCount})`
          )
        } else {
          console.log(
            'Warning: Did not receive expected response of',
            nonNegCount,
            'from API'
          )
          console.log('Received:', resStr)
        }
      }
    })
    .catch(err => console.log('Unable to set item count through API', err))
}

// vim: set ts=2 sw=2 vts=2 sta sts=2 sr et ai:
