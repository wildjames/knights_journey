import numpy as np

# Define the board as having the bottom left square be [0,0], and the top right be [7,7]

knight_moves = np.array(
    [
        [+1, +2],
        [+2, +1],
        [+2, -1],
        [+1, -2],
        [-1, -2],
        [-2, -1],
        [-2, +1],
        [-1, +2],
    ]
)


def get_possible_moves(position):
    """Take a position, which is a 2-element numpy array, and 
    return the possible moves that a knight could take from that location."""
    moves = knight_moves + position
    
    # Some numpy magic. Filter out all elements that contain a negative number
    positive_moves = moves[np.all(moves >= 0, axis=1)]
    legal_moves = positive_moves[np.all(positive_moves < 8, axis=1)]
    
    # There should always be at least two possible moves, if my reasoning is correct.
    return legal_moves


def index_to_chess_notation(position):
    pass


def chess_notation_to_index(postition):
    pass


if __name__ in "__main__":
    position = np.array([0, 0])
    moves = get_possible_moves(position)
    print("Position:")
    print(position)
    print("Moves:")
    print(moves)
