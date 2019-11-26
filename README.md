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
pipenv install
```

You might need to follow the instructions in the _Install Node.js on Raspberry
Pi_ section below if you can't install it with _apt_.

```bash
# Install Node.js and npm before this
cd webapp/
npm install
npm run build
```

## Usage

To start the web server, just run:

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


<!-- vim: set ts=4 sw=4 sta sts=4 sr et: -->
