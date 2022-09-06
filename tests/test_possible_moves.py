import numpy as np
import pytest
from src.knights_journey import get_possible_moves

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
    ]
]


@pytest.mark.parametrize("position,expected", possible_moves_test_io)
def test_possible_moves(position, expected):
    assert np.array_equal(get_possible_moves(position), expected)
