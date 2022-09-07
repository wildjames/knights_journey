#!python3

import sys

from src.knights_workers import print_path

if __name__ in "__main__":
    for line in sys.stdin:
        start, stop = line.strip().split(" ")
        print_path(start, stop)
