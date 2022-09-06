#!python3

from src.knights_workers import *
import click


@click.command()
@click.argument("start", type=str)
@click.argument("stop", type=str)
def execute(start, stop):
    """Take two positions, in chess co-ordinates (i.e. A1 - H8), and print the 
    positions that a knight could move through to take the shortest path between them.
    """

    initial_history = [[chess_notation_to_index(start)]]
    target = chess_notation_to_index(stop)
    moves = move_between_positions(target, initial_history)
    moves = [index_to_chess_notation(m) for m in moves]
    moves = " ".join(moves)

    print(moves)

if __name__ in "__main__":
    execute()