import numpy as np
import pytest
from src.knights_workers import *

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
        np.array(
            [
                [1, 2],
                [2, 1],
            ]
        ),
    ],
    [
        [7, 7],
        np.array(
            [
                [6, 5],
                [5, 6],
            ]
        ),
    ],
    [
        [0, 7],
        np.array(
            [
                [2, 6],
                [1, 5],
            ]
        ),
    ],
]


@pytest.mark.parametrize("position,expected", possible_moves_test_io)
def test_possible_moves(position, expected):
    assert np.array_equal(get_possible_moves(position), expected)


positions = [[[0, 0], "A1"], [[1, 0], "B1"], [[0, 1], "A2"], [[7, 7], "H8"]]


@pytest.mark.parametrize("position,index", positions)
def test_index_to_chess_notation(position, index):
    assert index_to_chess_notation(position) == index


@pytest.mark.parametrize("position,index", positions)
def test_chess_notation_to_index(position, index):
    assert np.array_equal(chess_notation_to_index(index), position)


test_pathfinding = [
    [
        # One move gets you there
        [[0, 0], [1, 2]],
        2,
    ],
    [
        # Two moves gets you there
        [[0, 0], [2, 4]],
        3,
    ],
    [
        # Cross the board
        [[0, 0], [7, 7]],
        7,
    ],
    [
        # And back again
        [[7, 7], [0, 0]],
        7,
    ],
    [
        # From near the middle
        [[5, 3], [7, 7]],
        4,
    ],
    [
        # Traverse in a straight line
        [[4, 0], [4, 7]],
        6,
    ],
]


@pytest.mark.parametrize("input,output", test_pathfinding)
def test_pathfinding(input, output):
    start = input[0]
    stop = input[1]

    n_moves = len(move_between_positions(stop, [[start]]))
    assert output >= n_moves


print_path_tests = [
    [
        # One move gets you there
        ["A1", "B3"],
        2,
    ],
    [
        # Two moves gets you there
        ["A1", "C5"],
        3,
    ],
    [
        # Cross the board
        ["A1", "H8"],
        7,
    ],
    [
        # And back again
        ["H8", "A1"],
        7,
    ],
    [
        # From near the middle
        ["E4", "H8"],
        4,
    ],
    [
        # Traverse in a straight line
        ["D1", "D8"],
        6,
    ],
]


@pytest.mark.parametrize("input,output", print_path_tests)
def test_pathfinding(input, output):
    start = input[0]
    stop = input[1]

    n_moves = len(print_path(start, stop))
    assert output == n_moves