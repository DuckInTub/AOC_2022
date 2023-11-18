from collections import deque
from itertools import groupby
from turtle import up
import numpy as np

# Constants
UP = (-1, 0)
DOWN = (1, 0)
LEFT = (0, -1)
RIGHT = (0, 1)
DIRS = [UP, DOWN, LEFT, RIGHT]

# Rotation around the x-axis by 90 degrees (counterclockwise)
Rx_ccw = np.array([
    [1, 0, 0],
    [0, 0, -1],
    [0, 1, 0]
], dtype=float)

# Rotation around the y-axis by 90 degrees (counterclockwise)
Ry_ccw = np.array([
    [0, 0, 1],
    [0, 1, 0],
    [-1, 0, 0]
], dtype=float)

# Rotation around the z-axis by 90 degrees (counterclockwise)
Rz_ccw = np.array([
    [0, -1, 0],
    [1, 0, 0],
    [0, 0, 1]
], dtype=float)

# Rotation around the x-axis by 90 degrees (clockwise)
Rx_cw = np.array([
    [1, 0, 0],
    [0, 0, 1],
    [0, -1, 0]
], dtype=float)

# Rotation around the y-axis by 90 degrees (clockwise)
Ry_cw = np.array([
    [0, 0, -1],
    [0, 1, 0],
    [1, 0, 0]
], dtype=float)

# Rotation around the z-axis by 90 degrees (clockwise)
Rz_cw = np.array([
    [0, 1, 0],
    [-1, 0, 0],
    [0, 0, 1]
], dtype=float)

# RIGHT, DOWN, LEFT, UP 
rot_map = {
    (1, 0, 0) : [Rz_ccw, Ry_cw, Rz_cw, Ry_ccw],
    (-1, 0, 0): [Rx_ccw, Ry_ccw, Rx_cw, Ry_cw],

}

def turn(direction : str, facing : tuple):
    facing = DIRS.index(facing)
    direction = -1 if direction == 'L' else 1
    return DIRS[(facing + direction) % len(DIRS)]

def move_cube(facing, start, steps, dimensions):
    pass

def parse_cube(face_size : int, lines : list[str]):
    lines = [line[:-1] for line in lines]
    nr_cols = max(map(len, lines)) // face_size
    nr_rows = len(lines) // face_size
    tiles = []
    
    for r in range(nr_rows):
        line_grp = lines[r*face_size:(r+1)*face_size]
        assert len(set(map(len, line_grp))) == 1
        tile_row = []
        for c in range(nr_cols):
            tile = [line[c*face_size:(c+1)*face_size] for line in line_grp]
            tile_row.append(tile)
        tiles.append(tile_row)

    # Find top left face
    for c in range(nr_cols):
        tile = tiles[0][c]
        if not tile[0]:
            continue
        fc = tile[0][0]
        if fc == '.' or fc == '#':
            start = 0, c
            break

    faces = []
    Q = deque()
    Q.append((start, np.array([0, -1, 0]), np.array([0, 0, -1])))
    seen = set()
    while Q:
        at, face_vec, up_vec = Q.popleft()
        r, c = at

        if at in seen or c < 0 or r < 0 or r >= nr_rows or c >= nr_cols:
            continue
        seen.add(at)

        tile = tiles[r][c]
        if not tile[0]:
            continue
        fc = tile[0][0]
        if fc not in '.#':
            continue

        face = np.array(tile)
        face.resize((50, 50))
        faces.append((np.array(face), face_vec, up_vec))

        for direction in [RIGHT, DOWN, LEFT, UP]:
            dr, dc = direction
            if direction == RIGHT:
                new_face_vec = 
            new_face_vec = rot_mat @ face_vec
            new_up_vec = rot_mat @ up_vec
            Q.append(((r+dr, c+dc), new_face_vec, new_up_vec))
        
    return faces
    

# Face_vec in order found
# [0, -1, 0]
# [1, 0, 0]
# [0, 0, 1]
# [0, 1, 0]
# [1, 0, 0]

POSITIONS = set()
WALLS = set()
with open('input.txt', 'r') as file:
    data = file.readlines()
    path = [''.join(v) for k, v in groupby(data[-1], str.isdigit)]
    path = [int(v) if str.isdigit(v) else v for v in path]
    fSize = 50
    # print(Rz_ccw @ np.array([0, -1, 0]))
    # vec = np.array([0, -1, 0])
    # rot_map = dict(zip([RIGHT, DOWN, LEFT, UP], [Rz_cw, Rx_ccw, Rz_ccw, Rx_cw]))
    # for direction in [DOWN, DOWN, LEFT]:
    #     rot_mat = rot_map[direction]
    #     vec = rot_mat @ vec
    # print(vec)
    dir_map = dict(zip([RIGHT, DOWN, LEFT, UP], [Rz_ccw, Rx_cw, Rz_cw, Rx_ccw]))
    faces = parse_cube(fSize, data[:-2])
    for face, face_vec, up_vec in faces:
        print(face_vec)