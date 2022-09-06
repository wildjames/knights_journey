# Define the board as having the bottom left square be [0,0], and the top right be [7,7]

knight_moves = [
    [+1, +2],
    [+2, +1],
    [+2, -1],
    [+1, -2],
    [-1, -2],
    [-2, -1],
    [-2, +1],
    [-1, +2],
]


def get_possible_moves(position):
    pass


def index_to_chess_notation(position):
    pass


def chess_notation_to_index(postition):
    pass


if __name__ in "__main__":
    position = [3, 3]
    moves = get_possible_moves(position)
    print(position)
    print(moves)
