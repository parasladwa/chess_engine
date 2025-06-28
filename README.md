# Simple Python Chess Engine - WIP

A lightweight terminal-based chess engine using `python-chess`, can play against it in the CLI.

## Version 1 `chess_engine1.py` [Functions as is]

- Uses chess library to find possible moves
- Evaluates position based of static board scalar values called `kernel`
- Minimax algorithm with alpha beta pruning, default depth of 4

## Version 2 `chess_engine2.py` [Functions as is]

- Runs off open source local chess engine, Stockfish

## Version 3 `chess_engine3.py` [WIP]

- Going to be built off Version 1
- Improvements in Kernels, different for each side, black/white


## Setup

```bash
pip install chess numpy
python your_script.py
