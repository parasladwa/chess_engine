import chess
import numpy as np







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





board = chess.Board()


def evaluate_board(board):
    evals = np.zeros((8, 8), dtype=int)
    
    for i in range(8):
        for j in range(8):
            if board.piece_at(chess.square(j, i)) == None:
                continue
            piece = board.piece_at(chess.square(j, i)).symbol()
            print(piece)
            evals[i, j] = piece_score[piece] * kernel[i, j]
            

    return np.sum(evals)

        


 
def evaluate_board(board):
    total = 0

    for square in chess.SQUARES:
        piece = board.piece_at(square)
        if piece is None:
            continue

        symbol = piece.symbol()
        score = piece_score[symbol]

        file = chess.square_file(square)  # 0 to 7
        rank = chess.square_rank(square)  # 0 to 7

        kernel_row = 7 - rank  # flip for correct top-down alignment
        kernel_col = file

        total += score * kernel[kernel_row, kernel_col]

    return total       


        
        
        

def print_board(board):
    for rank in range(8, 0, -1):
        line = str(rank) + "| "
        for file in "abcdefgh":
            square = chess.parse_square(file + str(rank))
            piece = board.piece_at(square)
            if piece:
                line += piece.symbol() + " "
            else:
                line += ". "
        print(line)
    print("   ---------------")
    print("  a b c d e f g h")














def main():
    
    
    board = chess.Board()
    
    
    user = input("playing as black or white? (b/w): ").strip().lower()
    user_is_white = user == 'w'

    
    
    
    print_board(board)
    
    
    while not board.is_game_over():
        
        
        if board.turn == user_is_white:

        
            
            while True:
                move_input = input("Enter your move (e.g., e2e4): ").strip()
                try:
                    move = chess.Move.from_uci(move_input)
                    if move in board.legal_moves:
                        board.push(move)
                        break  # valid move, exit loop
                    else:
                        print("Illegal move. Try again.")
                except:
                    print("Invalid move format. Try again.")
            print(board)
    
        
        
        
        
    
main()












#print(list(board.legal_moves))