
# Constants
from collections import deque


UP = (-1, 0)
DOWN = (1, 0)
LEFT = (0, -1)
RIGHT = (0, 1)
DIRS = [UP, RIGHT, DOWN, LEFT]


BLIZZARDS = set()
WALLS = set()
with open('test.txt', 'r') as file:
    start = (1, 2)
    data = file.readlines()
    finish = (len(data), len(data[0]-1))

    for r, row in enumerate(data):
        for c, char in enumerate(row):
            if char == '#':
                WALLS.add((r, c))
            if char in '^>v<':
                d = DIRS['^>v<'.index(char)]
                BLIZZARDS.add(((r, c), d))

def add_points(p1, p2):
    r1, c1 = p1
    r2, c2 = p2
    return r1+r2, c1+r2

def move_blizzard(b_points):
    for b in b_points:
        at, facing = b
        new_at = add_points(at, facing)
        if new_at in WALLS:
            
        

at = start
# steps, at
Q = deque()
Q.append((0, at))
SEEN = set()

while Q:
    steps, at = Q.pop()
    r, c = at

    if at in SEEN:
        continue
    SEEN.add((steps, at))



