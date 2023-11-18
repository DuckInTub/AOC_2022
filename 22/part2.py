from math import sqrt
from collections import deque
from itertools import combinations, groupby
import numpy as np
from typing import Set, Tuple

# Constants
UP = (-1, 0)
DOWN = (1, 0)
LEFT = (0, -1)
RIGHT = (0, 1)
DIRS = [UP, RIGHT, DOWN, LEFT]

def turn(direction : str, facing : tuple):
    facing = DIRS.index(facing)
    direction = -1 if direction == 'L' else 1
    return DIRS[(facing + direction) % len(DIRS)]

def add_points(p1, p2):
    r1, c1 = p1
    r2, c2 = p2
    return r1 + r2, c1 + c2

def move_cube(facing, start, steps, dimensions):
    pass

def parse_cube(points : Set[Tuple[int, int]]):
    # len = 6*A = 6*x ** 2
    side_length = sqrt(len(points) / 6)
    assert int(side_length) == side_length
    side_length = int(side_length)
    # Determine top_left point
    for c in range(6*side_length):
        if (0, c) in points:
            top_left = (0, c)
            break
    
    # Get only points that are on the circumference
    perimiter = set()
    perimiter.add(top_left)
    facing = RIGHT
    at = add_points(top_left, facing)
    while at != top_left:
        perimiter.add(at)
        # Prioritize walking: Left, Straight, Right
        left = turn('L', facing)
        right = turn('R', facing)
        l = add_points(at, left)
        s = add_points(at, facing)
        r = add_points(at, right)
        if l in points:
            facing = left
            at = l
        elif s in points:
            at = s
        elif r in points:
            facing = right
            at = r
        else:
            assert False
    
    # Get inner corners
    inners = set()
    for p in perimiter:
        u = add_points(p, UP)
        d = add_points(p, DOWN)
        l = add_points(p, LEFT)
        r = add_points(p, RIGHT)
        if all(poi in points for poi in [u, d, l, r]):
            inners.add(p)
    
    # Walk edges from inner corners
    edge_map = {}
    for inner_corner in inners:
        p_cw = inner_corner
        p_ccw = inner_corner
        for d in DIRS:
            f_ccw = add_points(inner_corner, d)
            f_cw = add_points(inner_corner, turn('R', d))
            if f_ccw in perimiter and f_cw in perimiter:
                f_ccw, f_cw = d, turn('R', d)
                break
         
        while True:
            for _ in range(side_length):
                p_cw = add_points(p_cw, f_cw)
                p_ccw = add_points(p_ccw, f_ccw)
                edge_map[p_cw, turn('L', f_cw)] = (p_ccw, turn('L', f_ccw))
                edge_map[p_ccw, turn('R', f_ccw)] = (p_cw, turn('R', f_cw))
            
            if not (add_points(p_cw, f_cw) in perimiter or add_points(p_ccw, f_ccw) in perimiter):
                break

            if add_points(p_cw, f_cw) not in perimiter:
                f_cw = turn('R', f_cw)
            if add_points(p_ccw, f_ccw) not in perimiter:
                f_ccw = turn('L', f_ccw)


    return edge_map


POSITIONS = set()
WALLS = set()
with open('test.txt', 'r') as file:
    data = file.readlines()
    path = [''.join(v) for k, v in groupby(data[-1], str.isdigit)]
    path = [int(v) if str.isdigit(v) else v for v in path]

    assert turn('R', UP) == RIGHT
    assert turn('R', LEFT) == UP
    assert turn('R', DOWN) == LEFT
    assert turn('R', RIGHT) == DOWN

    assert turn('L', UP) == LEFT
    assert turn('L', LEFT) == DOWN
    assert turn('L', DOWN) == RIGHT
    assert turn('L', RIGHT) == UP

    MAP = [[c for c in line[:-1]] for line in data[:-2]]
    for r, line in enumerate(MAP):
        for c, char in enumerate(line):
            if char == '#':
                WALLS.add((r, c))
            elif char == '.':
                POSITIONS.add((r, c))

    points = WALLS.union(POSITIONS)
    print(len(points))
    perimiter = parse_cube(points)
    print(perimiter)