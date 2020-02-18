export const initialState = { items: {} }

export const INCREMENT = 'INCREMENT'
export const DECREMENT = 'DECREMENT'
export const UPDATE_COUNT = 'UPDATE_COUNT'

export function reducer(state, action) {
  switch (action.type) {
    case INCREMENT:
      const incrementedState = {
        ...state,
        items: {...state.items}
      }
      if (incrementedState.items[action.payload]) {
        if (incrementedState.items[action.payload].count) {
          incrementedState.items[action.payload].count =
            incrementedState.items[action.payload].count + 1
        } else {
          incrementedState.items[action.payload].count = 1
        }
      } else {
        incrementedState.items[action.payload] = { count: 1 }
      }
      return incrementedState
    case DECREMENT:
      const decrementedState = {
        ...state,
        items: {...state.items}
      }
      if (decrementedState.items[action.payload]) {
        if (decrementedState.items[action.payload].count) {
          decrementedState.items[action.payload].count = Math.max(
            decrementedState.items[action.payload].count - 1, 0)
        } else {
          decrementedState.items[action.payload].count = 0
        }
      } else {
        decrementedState.items[action.payload] = { count: 0 }
      }
      return decrementedState
    case UPDATE_COUNT:
      const updatedState = {
        ...state,
        items: {...state.items}
      }
      if (updatedState.items[action.payload.name]) {
        updatedState.items[action.payload.name].count = action.payload.count
      } else {
        updatedState.items[action.payload.name] = { count: action.payload.count }
      }
      return updatedState
    default:
      throw new Error("Unexpected action in reducer: " + action.type)
  }
}
