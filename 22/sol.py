from itertools import groupby
import re

POSITIONS = set()
WALLS = set()
with open('input.txt', 'r') as file:
    data = file.readlines()
    path = [''.join(v) for k, v in groupby(data[-1], str.isdigit)]
    path = [int(v) if str.isdigit(v) else v for v in path]
    MAP = [[c for c in line[:-1]] for line in data[:-2]]
    maxY = len(MAP)
    for y, line in enumerate(MAP):
        for x, c in enumerate(line):
            if c == '#':
                WALLS.add((x, y))
            elif c == '.':
                POSITIONS.add((x, y))
    
UP = (0, -1)
DOWN = (0, 1)
LEFT = (-1, 0)
RIGHT = (1, 0)
DIRS = [UP, DOWN, LEFT, RIGHT]
def turn(direction : str, facing : tuple):
    facing = DIRS.index(facing)
    direction = -1 if direction == 'L' else 1
    return DIRS[(facing + direction) % len(DIRS)]

NEIGHBORS = {
    1 : {
        UP : (4, UP),
        DOWN: (3, DOWN),
        LEFT : (5, UP),
        RIGHT : (2, RIGHT),
    },
    2 : {
        UP : (4, RIGHT),
        DOWN: (3, LEFT),
        LEFT : (1, LEFT),
        RIGHT : (6, LEFT),
    },
    3 : {
        UP : (1, UP),
        DOWN: (6, DOWN),
        LEFT : (5, RIGHT),
        RIGHT : (2, UP),
    },
    4 : {
        UP : (6, UP),
        DOWN: (1, DOWN),
        LEFT : (5, LEFT),
        RIGHT : (2, DOWN),
    },
    5 : {
        UP : (6, RIGHT), 
        DOWN: (1, RIGHT),
        LEFT : (3, RIGHT),
        RIGHT : (4, RIGHT),
    },
    6 : {
        UP : (3, UP),
        DOWN: (4, DOWN),
        LEFT : (5, DOWN),
        RIGHT : (2, LEFT),
    },
}
def move_cube(facing, start, steps, dimensions):
    cmax, rmax = dimensions
    at = start
    for _ in range(steps):
        oldC, oldR, oldF = at
        oldFacing = facing
        c, r, f = at
        dc, dr = facing
        c, r = c+dc, r+dr

        if c < 0 or r < 0 or c > cmax or r > rmax:
            f, facing = NEIGHBORS[f][facing]
        
        if facing == UP:
            c, r = c, rmax
        if facing == DOWN:
            c, r = c, 0
        if facing == LEFT:
            c, r = 0, r
        if facing == RIGHT:
            c, r = cmax, r

        at = (c, r, f)
        if (c, r) in walls[f]:
            return (oldC, oldR, oldF), facing
    
    return at, facing


for x, c in enumerate(line):
    if c == '.':
        start = (x, 0)
        break

at = start
facing = (1, 0)
for inst in path:
    dir_s = '>V<^'[DIRS.index(facing)]
    if isinstance(inst, str):
        facing = turn(inst, facing)
    
    if isinstance(inst, int):
        MAP[at[1]][at[0]] = dir_s
        for i in range(inst):
            old = at
            at = (at[0]+facing[0], at[1]+facing[1])
            if at not in POSITIONS and at not in WALLS:
                if facing == (1, 0):
                    newX = min(map(lambda x : x[0], filter(lambda x : x[1] == at[1], POSITIONS|WALLS)))
                    at = (newX, at[1])
                elif facing == (-1, 0):
                    newX = max(map(lambda x : x[0], filter(lambda x : x[1] == at[1], POSITIONS|WALLS)))
                    at = (newX, at[1])
                elif facing == (0, -1):
                    newY = max(map(lambda x : x[1], filter(lambda x : x[0] == at[0], POSITIONS|WALLS)))
                    at = (at[0], newY)
                elif facing == (0, 1):
                    newY = min(map(lambda x : x[1], filter(lambda x : x[0] == at[0], POSITIONS|WALLS)))
                    at = (at[0], newY)

            if at in WALLS:
                at = old
                break

            MAP[at[1]][at[0]] = dir_s

print(at)
score = 1000*(at[1]+1) + 4*(at[0]+1) + DIRS.index(facing)
print(score)