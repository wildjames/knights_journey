import numpy as np
import pytest
from src.knights_journey import chess_notation_to_index, get_possible_moves, index_to_chess_notation

possible_moves_test_io = [
    [
        np.array([3, 3]),
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
        np.array([0, 0]),
        np.array([
            [1, 2],
            [2, 1],
        ]),
    ],
    [
        np.array([7, 7]),
        np.array([
            [6, 5],
            [5, 6],
        ]),
    ],
    [
        np.array([0, 7]),
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
        np.array([0,0]),
        "A1"
    ],
    [
        np.array([1,0]),
        "B1"
    ],
    [
        np.array([0,1]),
        "A2"
    ],
    [
        np.array([7,7]),
        "H8"
    ]
]

@pytest.mark.parametrize("position,index", positions)
def test_index_to_chess_notation(position, index):
    assert index_to_chess_notation(position) == index


@pytest.mark.parametrize("position,index", positions)
def test_chess_notation_to_index(position, index):
    assert np.array_equal(chess_notation_to_index(index), position)