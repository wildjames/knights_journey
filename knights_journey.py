#!python3

from src.knights_workers import print_path
import click


@click.command()
@click.argument("start", type=str)
@click.argument("stop", type=str)
def execute(start, stop):
    """Take two positions, in chess co-ordinates (i.e. A1 - H8), and print the 
    positions that a knight could move through to take the shortest path between them.
    """
    print_path(start, stop)

if __name__ in "__main__":
    execute()