
from collections import Counter, defaultdict
from copy import copy, deepcopy


with open('input.txt', 'r') as file:
    points = set()
    data = file.readlines()
    for r, row in enumerate(data):
        for c, char in enumerate(row):
            if char == '#':
                points.add((r, c))


start_len = len(points)

DIRS = {
    (-1, -1), (-1, 0), (-1, 1),
    (0, -1), (0, 1),
    (1, -1), (1, 0), (1, 1)
}

NORTHS = ((-1, -1), (-1, 0), (-1, 1))
SOUTHS = ((1, -1), (1, 0), (1, 1))
WESTS = ((-1, -1), (0, -1), (1, -1))
EASTS = ((-1, 1), (0, 1), (1, 1))
considerations = [NORTHS, SOUTHS, WESTS, EASTS]

def add_points(p1, p2):
    r1, c1 = p1
    r2, c2 = p2
    return r1+r2, c1+c2

def get_bounds(points):
    rs = {p[0] for p in points}
    cs = {p[1] for p in points}

    min_c = min(cs) 
    max_c = max(cs)
    min_r = min(rs)
    max_r = max(rs)
    return min_c, min_r, max_c, max_r
        
def print_elves(points):
    min_c, max_c, min_r, max_r = get_bounds(points)
    for r in range(min_r, max_r):
        for c in range(min_c, max_c):
            if (r, c) in points:
                print('#', end='')
            else:
                print(' ', end='')

def solve(part, points, considerations):
    considerations = deepcopy(considerations)
    points = deepcopy(points)
    range_limit = 10 if part == 1 else 10 ** 6
    for _ in range(range_limit):
        # Stage 1
        count = defaultdict(lambda : 0)
        D = {}
        for elf in points:
            if not any(add_points(elf, d) in points for d in DIRS):
                continue

            for cons in considerations:
                if not any(add_points(elf, d) in points for d in cons):
                    a = add_points(elf, cons[1])
                    D[elf] = a
                    count[a] += 1
                    break

        # Stage 2
        if part == 2 and len(D) == 0:
            return _+1
        for elf in D:
            if count[D[elf]] < 2:
                points.remove(elf)
                points.add(D[elf])

        assert len(points) == start_len
        considerations = considerations[1:] + [considerations[0]]

    return points

ans2 = solve(2, points, considerations)
points = solve(1, points, considerations)
min_c, min_r, max_c, max_r = get_bounds(points)
empty = 0
for c in range(min_c, max_c+1):
    for r in range(min_r, max_r+1):
        if (r, c) not in points:
            empty += 1
        

print(empty)
print(ans2)