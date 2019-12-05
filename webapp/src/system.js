export function apiAppUpdate() {
  console.log("Sending API request to update app")
  const url = "/api/app/update?blocking=true"
  fetch(url)
    .then(res => {
      console.log(res)
      return res.text()
    })
    .then(res => {
      if (res.includes("</html>")) {
        console.log("Warning:", url, "-> HTML response (expected OK).",
          "Is the API not running?")
      }
      window.location.reload(true);
    })
    .catch(err => console.log("Error: API request to update app failed.", err))
}

export function apiSystemRestart() {
  console.log("Sending API request to restart system")
  const url = "/api/system/restart"
  fetch(url)
    .then(res => {
      console.log(res)
      return res.text()
    })
    .then(res => {
      if (res.includes("</html>")) {
        console.log("Warning:", url, "-> HTML response (expected OK).",
          "Is the API not running?")
      }
    })
    .catch(err => console.log("Error: API request to restart system failed.", err))
}
