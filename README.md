# Simple Python Chess Engine - WIP

A lightweight terminal-based chess engine using `python-chess`, can play against it in the CLI.

## Version 1 `chess_engine1.py` [Functions as is]

- Uses chess library to find possible pieces
- Evaluates position based of static board scalar values called `kernel`
- Minimax with alpha beta pruning with default depth of 4

## Version 2 `chess_engine2.py` [Functions as is]

- Runs of opensource local chess engine, stockfish

## Version 3 `chess_engine3.py` [WIP]

- Going to be built off Version 1
- Improvements in Kernels, different for each side

## Notes

- Cutechess is an attempt to make my engine UCI compatible such that I can evaluate my models performance (ELO) against Stockfish
- No significant progress has been made, the documentation is sparse for this


## Setup

```bash
pip install chess numpy
python your_script.py
