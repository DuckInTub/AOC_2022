from collections import namedtuple
from itertools import groupby
from math import sqrt
from turtle import position
from typing import NamedTuple, Set, Tuple, override

class Point(NamedTuple):
    r: int
    c: int

    def __add__(self, other):
        return Point(self.r+other.r, self.c+other.c)

    def __sub__(self, other):
        return Point(other.r-self.r, other.c-self.c)

# Constants
UP = Point(-1, 0)
DOWN = Point(1, 0)
LEFT = Point(0, -1)
RIGHT = Point(0, 1)
DIRS = [RIGHT, DOWN, LEFT, UP]

def turn(direction : str, facing : Point):
    assert direction in "LR", "Can only turn L or R"
    facing = DIRS.index(facing)
    direction = -1 if direction == 'L' else 1
    return DIRS[(facing + direction) % len(DIRS)]

def get_top_left(points : Set[Point]):
    max_c = max(p.c for p in points)
    for c in range(max_c):
        if Point(1, c) in points:
            return Point(1, c)

def move(start, facing, instructions, positions, walls):
    points = positions|walls
    at = start
    # edge_mapping = get_edge_mapping(perimiter)
    for inst in instructions:
        if isinstance(inst, str):
            facing = turn(inst, facing)
            continue
        
        for _ in range(inst):
            old = at
            at = at + facing
            if at not in points:
                if facing == RIGHT:
                    at = Point(at.r, min(p.c for p in points if p.r == at.r))
                if facing == DOWN:
                    at = Point(min(p.r for p in points if p.c == at.c), at.c)
                if facing == LEFT:
                    at = Point(at.r, max(p.c for p in points if p.r == at.r))
                if facing == UP:
                    at = Point(max(p.r for p in points if p.c == at.c), at.c)

            if at in walls:
                at = old
                break

    return at, facing

POSITIONS : Set[Point] = set()
WALLS : Set[Point] = set()
with open('input.txt', 'r') as file:
    data = file.readlines()
    path = [''.join(v) for k, v in groupby(data[-1], str.isdigit)]
    path = [int(v) if str.isdigit(v) else v for v in path]

    MAP = [[c for c in line[:-1]] for line in data[:-2]]
    for r, line in enumerate(MAP):
        for c, char in enumerate(line):
            if char == '#':
                WALLS.add(Point(r+1, c+1))
            elif char == '.':
                POSITIONS.add(Point(r+1, c+1))

at, facing = move(get_top_left(POSITIONS|WALLS), RIGHT, path, POSITIONS, WALLS)
print(at, facing)
score = 1000*at.r + 4*at.c + DIRS.index(facing)
print(score)