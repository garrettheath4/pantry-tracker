// Source: https://stackoverflow.com/a/18358056/1360295

const numOrDefault = (altNum) => (num) => num || altNum
const numOrZero = numOrDefault(0)
const numOrOne = numOrDefault(1)

export const nonNegNum = (num) => Math.max(numOrZero(num), 0)
export const roundToOne = (num) =>
  Math.round((Number(num) + Number.EPSILON) * 10) / 10
const nonNegRoundedNum = (num) => roundToOne(nonNegNum(num))

const plus = (x, y) => x + y
const minus = (x, y) => x - y

// const plusFn = (x) => Math.max((x || 0) + (item.increment || 1), 0)
// const minusFn = (x) => Math.max((x || 0) - (item.decrement || 1), 0)
const deltaGenerator = (twoNums) =>
  (delta) => (x) => nonNegRoundedNum(twoNums(numOrZero(x), numOrOne(delta)))

export const plusDeltaGenerator = deltaGenerator(plus)
export const minusDeltaGenerator = deltaGenerator(minus)

