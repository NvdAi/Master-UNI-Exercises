import numpy as np

#  board king  queen  rook  bishop   knight  pawn 

class Board:

    def __init__(self, shape):
        self.shape_board = shape

    def make_board(self):
        board = np.zeros(self.shape_board)
        return board

# chess_board = Board((8,8))
# print(chess_board.make_board())

class King:
    def __init__(self):
        pass

    def make_king(self, board, data):
        board[data[1]][data[2]] = data[0]
        return board


