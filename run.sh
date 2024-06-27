#/bin/zsh

cd "$(dirname "$0")"

source .venv/bin/activate
python serve.py --reload