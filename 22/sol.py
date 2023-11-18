from itertools import groupby
import re

POSITIONS = set()
WALLS = set()
with open('input.txt', 'r') as file:
    data = file.readlines()
    path = [''.join(v) for k, v in groupby(data[-1], str.isdigit)]
    path = [int(v) if str.isdigit(v) else v for v in path]
    MAP = [[c for c in line[:-1]] for line in data[:-2]]
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