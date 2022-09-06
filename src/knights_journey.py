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
    """Take a position, which is a 2-element list, and 
    return the possible moves that a knight could take from that location.
    Leverages numpy logic"""
    moves = knight_moves + np.array(position)
    
    # Some numpy magic. Filter out all elements that contain a negative number
    positive_moves = moves[np.all(moves >= 0, axis=1)]
    legal_moves = positive_moves[np.all(positive_moves < 8, axis=1)]
    
    # There should always be at least two possible moves, if my reasoning is correct.
    return legal_moves.tolist()


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

    index = [file, rank]
    return index


def move_between_positions(start, stop, history=None):
    """Get the shortest path between two positions, recursively. 
    Note that this version checks depth-first, so will absolutely not return the fastest solutions.
    
    TODO: rewrite this so it's breadth-first."""
    if history is None:
        history = [start]

    possible_moves = get_possible_moves(start)
    # Dont allow retreading steps
    possible_moves = [move for move in possible_moves if move not in history]
    
    if stop in possible_moves:
        history.append(stop)
        return history
    
    else:
        for move in possible_moves:
            history.append(move)
            return move_between_positions(move, stop, history)


if __name__ in "__main__":
    position = "A1"
    target = "H8"

    print("Final answer:")
    position = chess_notation_to_index(position)
    target = chess_notation_to_index(target)
    moves = move_between_positions(position, target)
    print(moves)
    print("This is {} moves".format(len(moves)))
