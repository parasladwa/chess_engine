import chess
import numpy as np
import time


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

#test
 
def evaluate_board(board):
    total = 0

    for square in chess.SQUARES:
        piece = board.piece_at(square)
        if piece is None:
            continue

        symbol = piece.symbol()
        color = piece.color  # True for white, False for black
        base_score = abs(piece_score[symbol])  # use positive value

        file = chess.square_file(square)
        rank = chess.square_rank(square)
        kernel_row = 7 - rank if color == chess.WHITE else rank
        kernel_col = file

        positional_bonus = kernel[kernel_row, kernel_col]
        score = base_score + positional_bonus

        # Add as + for white, - for black
        total += score if color == chess.WHITE else -score

    return total



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




DEPTH = 4
def minimax(board, is_maximizing, depth=DEPTH, alpha=float('-inf'), beta=float('inf')):
    if depth == 0 or board.is_game_over():
        return evaluate_board(board)

    if is_maximizing:
        max_eval = float('-inf')
        best_move = None
        for move in board.legal_moves:
            board.push(move)
            eval = minimax(board, False, depth - 1, alpha, beta)
            board.pop()
            if eval > max_eval:
                max_eval = eval
                if depth == DEPTH:
                    best_move = move
            alpha = max(alpha, eval)
            if beta <= alpha:
                break
        return best_move if depth == DEPTH else max_eval
    else:
        min_eval = float('inf')
        best_move = None
        for move in board.legal_moves:
            board.push(move)
            eval = minimax(board, True, depth - 1, alpha, beta)
            board.pop()
            if eval < min_eval:
                min_eval = eval
                if depth == DEPTH:
                    best_move = move
            beta = min(beta, eval)
            if beta <= alpha:
                break
        return best_move if depth == DEPTH  else min_eval






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
            move = minimax(board, not user_is_white)
            board.push(move)
            print(f"Computer played: {move.uci()}, time taken: {time.time() - start:.2f} seconds")

        print_board(board, user_is_white)

    print("Game over:", board.result())


main()