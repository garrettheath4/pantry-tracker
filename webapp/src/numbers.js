// Source: https://stackoverflow.com/a/18358056/1360295

const numOrDefault = altNum => num => num || altNum
const numOrZero = numOrDefault(0)

export const nonNegNum = num => Math.max(numOrZero(num), 0)
export const roundToOne = num =>
  Math.round((Number(num) + Number.EPSILON) * 10) / 10
