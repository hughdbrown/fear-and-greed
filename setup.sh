#!/bin/sh

set -euo pipefail

pyenv install 3.12.0
pyenv virtualenv fear_greed-3.12.0
pyenv activate fear_greed-3.12.0
pyenv local fear_greed-3.12.0

pip install -r requirements.txt

