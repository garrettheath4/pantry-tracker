# pantry-tracker

A web app that helps you track what groceries you have in your pantry and fridge
so you know what you might be low on when you go to the store.


## Installation

You'll need Node.js to build the React UI and Python 3 to run the server.
Installing Python 3 is easy:

```bash
sudo apt install python3
pip3 install pipenv
git clone https://github.com/garrettheath4/pantry-tracker.git
cd pantry-tracker
sudo ln -s "$PWD/init.d" /etc/init.d/pantry-tracker && sudo update-rc.d pantry-tracker defaults
pipenv install
```

***Note:*** You might need to follow the instructions in the _Install Node.js
on Raspberry Pi_ section below if you can't install it with _apt_.

```bash
sudo apt install nodejs npm
npm install npm@latest -g
cd webapp/
npm install
npm run build
```


## Configuration

In order to run the server, you'll first need to create a `credentials.json`
file that can access the Google Sheets API. You can do this the quick way or the
advanced way.

The _quick_ way to do this is to go to [this quickstart guide][QuickCreds] and
click _Enable the Google Sheets API_ and then _Download Client Configuration_ to
download the `credentials.json` file.

The _advanced_ way to do this is to first go to the [Google APIs Developer
Console][AdvancedCreds]. From there, click on _Configure Consent Screen_ and go
through the process to set up the consent screen with the _auth/spreadsheets_
scope. After configuring the consent screen, click _Create Credentials > OAuth
client ID_ and follow that process to get a client ID and a client secret.


## Usage

To start the web server as a service, run:

```bash
service pantry-tracker start
```

To run the web server directly, just run:

```bash
./start.sh
```

from this repository's top level. Or you can directly run:

```bash
pipenv run python3 -m pantryserver
```


## Development

* From top-level folder of repo:
    * `pipenv run python3 -m test` - Run Python unit tests only (no React tests)
* From `webapp/` folder of repo:
    * `npm test` - Run React unit tests only (no Python tests)
    * `npm start` - Compile and launch the React UI in dev mode (no Python API)


## Dependencies

* React - webapp UI
* Python 3 - server for React UI and API
* Node.js and NPM - dependency management and build tool


## Install Node.js on Raspberry Pi

1. Download Linux binaries for ARM processors

    ```bash
    ARCH=$(arch)
    NODEVER=v12.13.1
    DISTRO=linux-$ARCH

    wget "https://nodejs.org/dist/$NODEVER/node-$NODEVER-$DISTRO.tar.xz"
    ```

2. Extract Node.js to the installation directory (`/usr/local/packages/` in
   this case)

    ```bash
    sudo mkdir -p /usr/local/packages
    sudo tar -xJvf "node-$NODEVER-$DISTRO.tar.xz" -C /usr/local/packages
    sudo chown -R root:staff /usr/local/packages
    sudo chmod -R ug+w /usr/local/packages
    ```

3. Create a symbolic link to point to the "current" version of Node.js (this
   makes it easier to update to a newer version by simply updating this link)

    ```bash
    cd /usr/local/packages
    sudo ln -s "node-$NODEVER-$DISTRO" nodejs
    ```

4. Add Node.js to your path by adding this line to your `~/.profile` or
   `~/.bashrc` (using `nano ~/.profile` or `vim ~/.profile`)

   ```bash
   export PATH=$PATH:/usr/local/packages/nodejs/bin
   ```


## Troubleshooting

### Google Refresh Error

If the Python console has the following error after you try to start the server
process:

```
google.auth.exceptions.RefreshError: ('deleted_client: The OAuth client was
deleted.', '{\n  "error": "deleted_client",\n  "error_description": "The OAuth
client was deleted."\n}')
```

then simply delete the `token.pickle` file and restart the Python server. The
server will then launch a web browser with a google.com page to allow you to
authenticate to your Google account.


### Lots of 404's

If you see the error `code 404, message File Not Found` in the Python console
multiple times then it probably means the React webapp's URL prefix is set
incorrectly. Check the value of the `"homepage"` key in `webapp/package.json`.
You should probably delete the `"homepage"` configuration line unless you're
hosting the web app on GitHub.io (for example:
`"homepage": "http://garrettheath4.github.io/pantry-tracker",`).


<!-- Links -->
[QuickCreds]: https://developers.google.com/sheets/api/quickstart/python
[AdvancedCreds]: https://console.developers.google.com/apis/credentials?authuser=0&project=quickstart-1580509776614


<!-- vim: set ts=4 sw=4 sta sts=4 sr et: -->
