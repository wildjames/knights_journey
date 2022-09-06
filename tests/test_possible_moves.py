import numpy as np
import pytest
from src.knights_journey import chess_notation_to_index, get_possible_moves, index_to_chess_notation, move_between_positions

possible_moves_test_io = [
    [
        [3, 3],
        np.array(
            [
                [4, 5],
                [5, 4],
                [5, 2],
                [4, 1],
                [2, 1],
                [1, 2],
                [1, 4],
                [2, 5],
            ]
        ),
    ],
    [
        [0, 0],
        np.array([
            [1, 2],
            [2, 1],
        ]),
    ],
    [
        [7, 7],
        np.array([
            [6, 5],
            [5, 6],
        ]),
    ],
    [
        [0, 7],
        np.array([
            [2, 6],
            [1, 5],
        ]),
    ]
]


@pytest.mark.parametrize("position,expected", possible_moves_test_io)
def test_possible_moves(position, expected):
    assert np.array_equal(get_possible_moves(position), expected)


positions = [
    [
        [0,0],
        "A1"
    ],
    [
        [1,0],
        "B1"
    ],
    [
        [0,1],
        "A2"
    ],
    [
        [7,7],
        "H8"
    ]
]

@pytest.mark.parametrize("position,index", positions)
def test_index_to_chess_notation(position, index):
    assert index_to_chess_notation(position) == index


@pytest.mark.parametrize("position,index", positions)
def test_chess_notation_to_index(position, index):
    assert np.array_equal(chess_notation_to_index(index), position)


test_pathfinding = [
    [
        # One move gets you there
        [[0,0],[1, 2]],
        [[0,0],[1, 2]]
    ],
    [
        # Two moves gets you there
        [[0,0],[2, 4]],
        [[0,0],[1, 2],[2, 4]]
    ],
    [
        # Two moves gets you there
        [[0,0],[7, 7]],
        [[0,0],[1, 2],[2, 4]]
    ],   
]

@pytest.mark.parametrize("input,output", test_pathfinding)
def test_pathfinding(input, output):
    start = input[0]
    stop = input[1]

    moves = output
    assert np.array_equal(move_between_positions(start, stop), moves)