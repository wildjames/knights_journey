import numpy as np

# Define the board as having the bottom left square be [0,0], and the top right be [7,7]

# Possible knight movement vectors
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
    Leverages numpy logic
    """
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


def move_between_positions(stop, histories):
    """Histories must be initialised with at least one history, with at least one position. 
    e.g.
    histories = [
        [ # first history
            [0,0]
        ]
    ]

    Recursive. Returns a list of positions that terminate at the `stop` position

    Inputs:
    -------
    stop: list
        - A two-element list that constitutes the target vector. e.g. [0, 1]
    histories: list
        - A list-of-lists-of-positions, which forms the traversed tree. Each element of the top-level list is a list of unique positions 
    
    Returns:
    --------
    path: list
        - A list of positions that terminate at the `stop` vector.
    """
    # Get the shortest history. This will be checked next.
    shortest_history = histories[0]
    for history in histories:
        if len(history) < len(shortest_history):
            shortest_history = history

    position = shortest_history[-1]
    moves = get_possible_moves(position)
    for move in moves:
        # If we've been here before, skip this move
        if move in shortest_history:
            continue

        # Create a new history with this move on the end, and 
        # if its new then add it to the list of histories
        proposed_history = shortest_history + [move]

        # If we've arrived, return the path
        if move == stop:
            return proposed_history

        # If we are still searching, add a branch to the tree
        if not proposed_history in histories:
            histories.append(proposed_history)
    
    # Prune the old branch
    histories.remove(shortest_history)

    return move_between_positions(stop, histories)


if __name__ in "__main__":
    position = "E1"
    target = "E8"

    position = chess_notation_to_index(position)
    target = chess_notation_to_index(target)
    moves = move_between_positions(target, [[position]])

    print("Final answer:")
    print([index_to_chess_notation(m) for m in moves])
    print("This is {} positions".format(len(moves)))
