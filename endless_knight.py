#!python3

from src.knights_workers import print_path


if __name__ in "__main__":
    while True:
        try:
            inp = input("")
        except EOFError:
            exit()
        
        if "q" in inp.lower():
            exit()
        if not " " in inp:
            exit()
        
        start, stop = inp.split(" ")

        print_path(start, stop)
