#/bin/zsh

cd "$(dirname "$0")"

source .venv/bin/activate
python main.py --serve=true --reload=true --prefix=kent-map/kent