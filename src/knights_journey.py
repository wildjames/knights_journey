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
    """Take a position, like (2, 4), and return the chess notation string, like B5."""
    file = "ABCDEFGH"[position[0]]
    rank = str(position[1]+1)

    chess_notation = file + rank

    return chess_notation


def chess_notation_to_index(chess_notation):
    """Take a position, like B5, and return the chess notation string, like (2, 4)."""

    file = "ABCDEFGH".index(chess_notation[0])
    rank = int(chess_notation[1]) - 1

    index = np.array([file, rank])
    return index


if __name__ in "__main__":
    position = np.array([1, 2])
    moves = get_possible_moves(position)
    print("Position:")
    print(index_to_chess_notation(position))
    print("Moves:")
    print(moves)
