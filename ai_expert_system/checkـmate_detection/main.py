
def main(state):
    pass


if __name__ == "__main__":
    # location of components
    palyer_white = {}
    palyer_white["pawn_0"] = ('a',2)
    palyer_white["pawn_1"] = ('b',2)
    palyer_white["pawn_2"] = ('c',2)
    palyer_white["pawn_3"] = ('d',2)
    palyer_white["pawn_4"] = ('e',2)
    palyer_white["pawn_5"] = ('f',2)
    palyer_white["pawn_6"] = ('g',2)
    palyer_white["pawn_7"] = ('h',2)
    palyer_white["rook_0"] = ('a',1)
    palyer_white["rook_1"] = ('h',1)
    palyer_white["knight_0"] = ('b',1)
    palyer_white["knight_1"] = ('g',1)
    palyer_white["bishop_0"] = ('c',1)
    palyer_white["bishop_1"] = ('f',1)
    palyer_white["queen"] = ('e',1)
    palyer_white["king"] = ('d',1)

    palyer_black = {}
    palyer_black["pawn_0"] = ('a',2)
    palyer_black["pawn_1"] = ('b',2)
    palyer_black["pawn_2"] = ('c',2)
    palyer_black["pawn_3"] = ('d',2)
    palyer_black["pawn_4"] = ('e',2)
    palyer_black["pawn_5"] = ('f',2)
    palyer_black["pawn_6"] = ('g',2)
    palyer_black["pawn_7"] = ('h',2)
    palyer_black["rook_0"] = ('a',1)
    palyer_black["rook_1"] = ('h',1)
    palyer_black["knight_0"] = ('b',1)
    palyer_black["knight_1"] = ('g',1)
    palyer_black["bishop_0"] = ('c',1)
    palyer_black["bishop_1"] = ('f',1)
    palyer_black["queen"] = ('e',1)
    palyer_black["king"] = ('d',1)

    state = {}
    state["palyer_white"] = palyer_white
    state["palyer_black"] = palyer_black
    state["board_size"] = (8,8)

    main(state)