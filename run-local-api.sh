#/bin/zsh

cd "$(dirname "$0")"

source .venv/bin/activate
python main.py --wc http://localhost:5173/src/main.ts --api http://localhost:8000