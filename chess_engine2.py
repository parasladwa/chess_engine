import chess
import numpy as np
import time
from stockfish import Stockfish

stockfish = Stockfish(path=r"C:\Users\paras\Desktop\Personal\stockfish\stockfish-windows-x86-64-avx2.exe", depth=15)
stockfish.update_engine_parameters({"Hash": 2048, "Threads": 4})


kernel = np.array([[0, 5, 5, 5, 5, 5, 5, 0,],
                  [5, 10, 10, 10, 10, 10, 10, 5],
                  [5, 10, 20, 20, 20, 20, 10, 5],
                  [5, 10, 20, 30, 30, 20, 10, 5],
                  [5, 10, 20, 30, 30, 20, 10, 5],
                  [5, 10, 20, 20, 20, 20, 10, 5],
                  [5, 10, 10, 10, 10, 10, 10, 5],
                  [0, 5, 5, 5, 5, 5, 5, 0]], dtype=int)



piece_score = {
    'p': 100,  # Pawn
    'n': 300,  # Knight
    'b': 350,  # Bishop
    'r': 500,  # Rook
    'q': 900,  # Queen
    'k': 100000,  # King
    'P': -100,  # Pawn
    'N': -300,  # Knight
    'B': -350,  # Bishop
    'R': -500,  # Rook
    'Q': -900,  # Queen
    'K': -100000  # King
}


 




def print_board(board, user_is_white=True):
    ranks = range(8, 0, -1) if user_is_white else range(1, 9)
    files = "abcdefgh" if user_is_white else "hgfedcba"

    for rank in ranks:
        line = str(rank) + "| "
        for file in files:
            square = chess.parse_square(file + str(rank))
            piece = board.piece_at(square)
            if piece:
                line += piece.symbol() + " "
            else:
                line += ". "
        print(line)
    print("   ---------------")
    print("   " + " ".join(files))







def main():
    board = chess.Board()
    user = input("Playing as black or white? (b/w): ").strip().lower()
    user_is_white = user == 'w'

    print_board(board, user_is_white)

    while not board.is_game_over():
        if board.turn == user_is_white:
            # User's turn
            while True:
                move_input = input("Enter your move (e.g., e2e4): ").strip()
                try:
                    move = chess.Move.from_uci(move_input)
                    if move in board.legal_moves:
                        board.push(move)
                        break
                    else:
                        print("Illegal move. Try again.")
                except:
                    print("Invalid move format. Try again.")
        else:
            # Computer's turn
            print("Computer thinking...")
            start = time.time()

            
            
            
            stockfish.set_fen_position(board.fen())

            move = stockfish.get_best_move()
            #convert move to chess.Move object
            move = chess.Move.from_uci(move)
            
            print(move, type(move))
            board.push(move)
            print(f"Computer played: {move.uci()}, time taken: {time.time() - start:.2f} seconds")

        print_board(board, user_is_white)

    print("Game over:", board.result())


main()