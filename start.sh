#!/usr/bin/env bash

# Switch to this script's directory (in case it's called from a different working directory)
cd "$( dirname "${BASH_SOURCE[0]}" )" || exit

# Optional: pipenv install

pipenv run python3 -m pantryserver
