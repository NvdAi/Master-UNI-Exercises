from typing import List
import pawn

class Player:
    def __init__(self, 
                 board_size: tuple =(8,8), 
                 player_state: dict = {}):
        self.board_size = board_size
        self.player_state = player_state 
        self.components: List = []

    def build(self):
        self.pawn_0 = pawn.Pawn(pos=self.player_state["pawn_0"])
        self.components.append(self.pawn_0)

        self.pawn_1 = pawn.Pawn(pos=self.player_state["pawn_1"])
        self.components.append(self.pawn_1)
        # TODO add all components here


    def is_check(self, competitor):
        # based on another player (competitor) check if it's in "check" state
        # check all components
        pass


    def is_mate(self, competitor):
        # check if it's in mate state
        pass


