# Simple Python Chess Engine - WIP

A lightweight terminal-based chess engine using `python-chess`, can play against it in the CLI.

## Version 1 `chess_engine1.py` [Functions as is]

- Uses chess library to find possible pieces
- Evaluates position based of static board scalar values called `kernel`
- Minimax with alpha beta pruning with default depth of 4

## Version 2 `chess_engine2.py` [WIP]

- Cannot increase depth of minimax function, too computationally expensive, the engines moves will take too long
- Improvements will be implemented upon the evaluation function
- Likely to use different kernels for Black and White pieces, possibly a kernel for each type of chess-piece


## Notes

- Cutechess is an attempt to make my engine UCI compatible such that i can evaluate my models performance (ELO) against Stockfish
- No significant progress has been made, the documentation is sparse for this


## Setup

```bash
pip install chess numpy
python your_script.py
