import pytest
from src.knights_journey import get_possible_moves


possible_moves_test_io = [
    [
        [0, 0],
        [
            [1, 2],
            [2, 1],
        ],
    ]
]


@pytest.mark.parametrize("position,expected", possible_moves_test_io)
def test_possible_moves(position, expected):
    assert get_possible_moves(position) == expected
