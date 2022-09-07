Knight's path
=============

Implement a program that finds the shortest path a knight can take between two points on a standard 8x8 chessboard.

In chess, knights move in an L-shape: 2 squares along one dimension, 1 square along the other. See the [Wikipedia illustration](https://en.wikipedia.org/wiki/Knight_(chess)#Placement_and_movement):

![knight moves](img/knight-moves.png)

Functional Requirements
-----------------------

  - Write a command-line executable that reads instructions from standard input (stdin).
  - Instructions are lines (separated by newlines) in the following format:
```
D4 G7
D4 D5
```

  - The first of the space-separated values is the knight's starting position, the second is the knight's target position.
  - For each line in the input, your program should print (to standard out) the shortest path it found. So for the example above, it should print e.g.:
```
D4 F5 G7
D4 E2 F4 D5
```

Notes
-----

  - Use language you are most comfortable in.
  - Apply development practices you use to write **production code**.
  - Feel free to use supporting libraries (but write the algorithm yourself).
  - Provide complete instructions for running your code and installing dependencies.
  - Document assumptions and decisions in readme file.
  - It should be possible to run your program on Linux or macOS.
  - Please provide us with access to your git repo with code when you’re done (don't push to this repo).

-----

# James Wild 

This is my attempt at filling the above brief. Note that any minor changes should be made on the `development` branch, and new features or refactoring should be done on their own branches. Committing directly to master should be disabled. Pull requests *must* pass automated checks, and new functions should be covered with new tests!

## Running the code

I use conda environments, since I'm on Apple silicon and python is generally a pain here. To replicate my environment, 
```
conda create -n knights_journey python==3.10 
conda activate knights_journey
pip install -r requirements.txt
```

I have two running scripts. First, and mostly for debugging, is `./knights_journey.py` which takes two arguments: `[start]` and `[stop]`, and prints a path between them. This has a shebang, so doesn't need to have python specified: `$ ./knights_journey.py [start] [stop]`.

There is also `endless_knight.py` which just streams in the `stdin` and prints paths as we go, with output that looks like this:
```
$ ./endless_knight.py 
A1 B3
A1 B3
A1 H8
A1 B3 C5 D7 F8 G6 H8
D3 E8
D3 E5 F7 D6 E8
```
This can be escaped by entering an invalid position, killing the script, or entering a string containing `q`. Note that positions can also be fed input from a file, like `./endless_knight.py < input_list.txt`


## Testing

I should have `pytest` tests for my code (if I've kept up with it), which should be runnable simply with
```
pytest --cov=src tests/
```

Pytest should also run automatically in Github on pushes and pull requests. 

-----

## Initial thoughts. 

From here on are my stream-of-conciousness notes on the task. I prefer to keep more casual notes when doing something like this, since it's a better insight into my thought processes; actual, real projects get more "official" documentation. Depending on how verbose this gets, I may convert this section into a jupyter notebook, but we shall see.

  - Since this is chess on a standard board, there's a temptation to use `stockfish` to generate legal moves. This would let me change what piece we're considering, e.g. to a rook, or let me impose restrictions like there being other pieces on the board, but still feels like overkill for the description as-is.
    - It's not worth the import, I don't think. Were the task to expand, the logic from a vanilla python implementation would port over pretty easily anyway, so a v2 would be pretty doable.
  - Knights can move both forward and back, making closed loops irrelevant. Keep a list of visited tiles, and disallow revisting places we've been.
  - Possible use-case for recursion - I'll have a think once I've got basics down.
    - My quick-and-dirty recursive implementation turned out depth-first, duh. Rewrite that so it's breadth-first!
  - It occurs to me while writing the breadth-first version that since this is just a graph, I could leverage a graph package to handle this?
    - Probably more optimised
    - It's been a few years since I've done anything with networkX, but I think that would do the job here... But I'd need to essentially re-learn its use

-----

So there didn't wind up being much to talk about. Besides initially using a depth-first search (caught by my tests) and having to re-jig the logic for the moving function, this proceeded fairly straightforwardly. I'll leave my initial thoughts below unedited, for posterity, but this was fun to do around dinner and while watching Charlotte (my wife) play some games in the background.

