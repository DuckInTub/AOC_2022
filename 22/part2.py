from collections import Counter
from json import dump
from math import sqrt
from string import ascii_uppercase
from turtle import pos
from typing import Set, Tuple
from itertools import groupby

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

def move_cube(start, facing, insts, positions, walls):
    at = start
    edge_map = parse_cube(positions.union(walls))
    points = [(at, facing)]
    
    for inst in insts:
        if isinstance(inst, str):
            facing = turn(inst, facing)
            points.append((at, facing))
            continue

        for _ in range(inst):
            old = at
            old_facing = facing
            at = add_points(at, facing)
            if at not in positions.union(walls):
                at, facing = edge_map[old, facing]
            
            if at in walls:
                at = old
                facing = old_facing
                points.append((at, facing))
                break
            points.append((at, facing))

    return points, facing


def trace_perimiter(points : Set[Tuple[int, int]]):
    # len = 6*A = 6*x ** 2
    side_length = sqrt(len(points) / 6)
    assert int(side_length) == side_length
    side_length = int(side_length)
    # Determine top_left point
    for c in range(6*side_length):
        if (1, c) in points:
            top_left = (1, c)
            break
    
    # Get only points that are on the circumference
    perimiter = set()
    perimiter.add(top_left)
    facing = RIGHT
    at = add_points(top_left, facing)
    while at != top_left:
        perimiter.add(at)
        # Prioritize walking: left, straight or right,
        # since we are walking clockwise around the circumference.
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
    
    return perimiter

def get_inner_corners(points):
    perimiter = trace_perimiter(points)
    inners = set()
    for p in perimiter:
        u = add_points(p, UP)
        d = add_points(p, DOWN)
        l = add_points(p, LEFT)
        r = add_points(p, RIGHT)
        if all(poi in points for poi in [u, d, l, r]):
            inners.add(p)
    
    return inners

def visualize_edges(points : Set[Tuple[int, int]]):
    # len = 6*A = 6*x ** 2
    side_length = sqrt(len(points) / 6)
    assert int(side_length) == side_length
    side_length = int(side_length)

    perimiter = trace_perimiter(points)

    # Get inner corners
    inners = get_inner_corners(points)

    i = 0
    alfa = ascii_uppercase
    max_r = max(map(lambda x : x[0], points)) + 1 
    max_c = max(map(lambda x : x[1], points)) + 1 
    m = [[' ']*max_c for _ in range(max_r)]
    # Walk edges out from inner corners
    for inner_corner in inners:
        # Determine counter- and clockwise pointers and facing vectors
        p_cw = inner_corner
        p_ccw = inner_corner
        for d in DIRS:
            f_ccw = add_points(inner_corner, d)
            f_cw = add_points(inner_corner, turn('R', d))
            if f_ccw in perimiter and f_cw in perimiter:
                f_ccw, f_cw = d, turn('R', d)
                break

        # Add the edges connected to the inner corner
        for _ in range(side_length):
            p_cw = add_points(p_cw, f_cw)
            p_ccw = add_points(p_ccw, f_ccw)
            r, c = p_cw
            m[r][c] = alfa[i] if _ >= side_length // 2 else alfa[i].lower()
            r, c = p_ccw
            m[r][c] = alfa[i] if _ >= side_length // 2 else alfa[i].lower()
        i += 1

        # If both facing vectors don't have to turn,
        # we can keep adding the edges until they do.
        while add_points(p_cw, f_cw) in perimiter or add_points(p_ccw, f_ccw) in perimiter:
            if add_points(p_cw, f_cw) not in perimiter:
                f_cw = turn('R', f_cw)
            if add_points(p_ccw, f_ccw) not in perimiter:
                f_ccw = turn('L', f_ccw)

            for _ in range(side_length):
                r, c = p_cw
                m[r][c] = alfa[i] if _ >= side_length // 2 else alfa[i].lower()
                r, c = p_ccw
                m[r][c] = alfa[i] if _ >= side_length // 2 else alfa[i].lower()
                p_cw = add_points(p_cw, f_cw)
                p_ccw = add_points(p_ccw, f_ccw)
            i += 1

    return m

def parse_cube(points : Set[Tuple[int, int]]):
    # len = 6*A = 6*x ** 2
    side_length = sqrt(len(points) / 6)
    assert int(side_length) == side_length
    side_length = int(side_length)

    perimiter = trace_perimiter(points)
    inners = get_inner_corners(points) 

    # Walk edges out from inner corners
    edge_map = {}
    for inner_corner in inners:
        # Determine counter- and clockwise pointers and facing vectors
        p_cw = inner_corner
        p_ccw = inner_corner
        for d in DIRS:
            f_ccw = add_points(inner_corner, d)
            f_cw = add_points(inner_corner, turn('R', d))
            if f_ccw in perimiter and f_cw in perimiter:
                f_ccw, f_cw = d, turn('R', d)
                break

        # Add the edges connected to the inner corner
        for _ in range(side_length):
            p_cw = add_points(p_cw, f_cw)
            p_ccw = add_points(p_ccw, f_ccw)
            edge_map[p_cw, turn('L', f_cw)] = (p_ccw, turn('L', f_ccw))
            edge_map[p_ccw, turn('R', f_ccw)] = (p_cw, turn('R', f_cw))

        # If both facing vectors don't have to turn,
        # we can keep adding the edges until they do.
        while add_points(p_cw, f_cw) in perimiter or add_points(p_ccw, f_ccw) in perimiter:
            if add_points(p_cw, f_cw) not in perimiter:
                f_cw = turn('R', f_cw)
                p_ccw = add_points(p_ccw, f_ccw)
            if add_points(p_ccw, f_ccw) not in perimiter:
                f_ccw = turn('L', f_ccw)
                p_cw = add_points(p_cw, f_cw)

            for _ in range(side_length):
                edge_map[p_cw, turn('L', f_cw)] = (p_ccw, turn('L', f_ccw))
                edge_map[p_ccw, turn('R', f_ccw)] = (p_cw, turn('R', f_cw))
                if _ >= side_length - 1:
                    break
                p_cw = add_points(p_cw, f_cw)
                p_ccw = add_points(p_ccw, f_ccw)

    return edge_map

def draw_points(points, char):
    max_r = max(map(lambda x : x[0], points)) + 1
    max_c = max(map(lambda x : x[1], points)) + 1
    m = [[' ']*max_c for _ in range(max_r)]
    
    for point in points:
        r, c = point
        m[r][c] = char

    m = list(''.join(row) for row in m)
    for row in m:
        print(row)
    print()

def visualize_walk(points, walk):
    max_r = max(map(lambda x : x[0], points)) + 1
    max_c = max(map(lambda x : x[1], points)) + 1
    m = [[' ']*max_c for _ in range(max_r)]

    for point in points:
        r, c = point
        m[r][c] = '#'
    
    for point, facing in walk:
        char = '↑→↓←'[DIRS.index(facing)]
        r, c = point
        m[r][c] = char

    m = list(''.join(row) for row in m)
    for row in m:
        print(row)
    print()

POSITIONS = set()
WALLS = set()
with open('input.txt', 'r') as file:
    data = file.readlines()
    path = [''.join(v) for k, v in groupby(data[-1], str.isdigit)]
    path = [int(v) if str.isdigit(v) else v for v in path]

    MAP = [[c for c in line[:-1]] for line in data[:-2]]
    for r, line in enumerate(MAP):
        for c, char in enumerate(line):
            if char == '#':
                WALLS.add((r+1, c+1))
            elif char == '.':
                POSITIONS.add((r+1, c+1))


# Determine top_left point
# len = 6*A = 6*x ** 2
points = POSITIONS.union(WALLS)
side_length = sqrt(len(points) / 6)
assert int(side_length) == side_length
side_length = int(side_length)
# Determine top_left point
for c in range(6*side_length):
    if (1, c) in points:
        top_left = (1, c)
        break

perimiter = trace_perimiter(points)
inners = get_inner_corners(points)
# draw_points(perimiter, '#')

edges = parse_cube(points)

for point in perimiter:
    if not any((point, d) in edges for d in DIRS) and not point in inners:
        print(point)

# print(Counter(map(lambda x : x[0], edges)))
print()
# print(edges)
edges = set(edge[0] for edge in edges)
draw_points(edges, '#')

# edge_drawing = visualize_edges(points)
# for row in edge_drawing:
#     print(''.join(row))
# print()

end, facing = move_cube(top_left, RIGHT, path, POSITIONS, WALLS)
visualize_walk(points, end)
r, c = end[-1][0]
print(r, c, facing)
score = 1000*r + 4*c + [RIGHT, DOWN, LEFT, UP].index(facing)
print(score)