#!python3

from src.knights_workers import print_path
import sys


if __name__ in "__main__":
    for line in sys.stdin.readlines():
        start, stop = line.strip().split(" ")
        print_path(start, stop)
