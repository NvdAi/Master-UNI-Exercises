
class Board:
    def __init__(self, 
                 state: dict = {}):
        self.state = state
        self.player_white_state = self.state["player_white"]
        self.player_black_state = self.state["player_black"]
        self.board_size = state["board_size"]
    


