from typing import List, Tuple

class Pawn:
    def __init__(self, 
                 pos: tuple = ("a", 2), 
                 board_size: Tuple = (8,8))->None:
        self.pos = pos
        self.board_size = board_size
    
    def next_possible_position()->List[Tuple]:
        positions = []
        # return all posible positions based on current position and board size and other components in board
        return positions

