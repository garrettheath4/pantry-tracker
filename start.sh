#!/usr/bin/env bash

ConsoleLogFile=/tmp/pantryserver-console.log

# Switch to this script's directory (in case it's called from a different working directory)
cd "$( dirname "${BASH_SOURCE[0]}" )" || exit

git pull

# Optional: pipenv install

# Optional: npm run build
cd webapp && npm run build && cd ..

pipenv run python3 -m pantryserver 2>&1 >> $ConsoleLogFile
