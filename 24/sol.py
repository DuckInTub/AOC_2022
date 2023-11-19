from collections import deque

# Constants
UP = (-1, 0)
DOWN = (1, 0)
LEFT = (0, -1)
RIGHT = (0, 1)
DIRS = [UP, RIGHT, DOWN, LEFT]

def add_points(p1, p2):
    r1, c1 = p1
    r2, c2 = p2
    return r1+r2, c1+c2

BLIZZARDS = set()
WALLS = set()
with open('test.txt', 'r') as file:
    start = (0, 1)
    WALLS.add(add_points(start, UP))
    data = [line[:-1] for line in file.readlines()]
    finish = (len(data)-1, len(data[0])-2)

    for r, row in enumerate(data):
        for c, char in enumerate(row):
            if char == '#':
                WALLS.add((r, c))
            if char in '^>v<':
                d = DIRS['^>v<'.index(char)]
                BLIZZARDS.add(((r, c), d))

    rs = list(map(lambda x : x[0], WALLS))
    cs = list(map(lambda x : x[1], WALLS))
    max_r = max(rs)
    min_r = min(rs)
    max_c = max(cs)
    min_c = min(cs)


def move_blizzard(b_points):
    ret = set()
    for b in b_points:
        at, facing = b
        new_at = add_points(at, facing)
        if new_at in WALLS:
            if facing == UP:
                new_at = (max_r-1, at[1])
            if facing == DOWN:
                new_at = (min_r+1, at[1])
            if facing == LEFT:
                new_at = (at[0], max_c-1)
            if facing == RIGHT:
                new_at = (at[0], min_c+1)
        ret.add((new_at, facing))
    return ret

def get_nex_blizzard_state():
    curr = BLIZZARDS
    while True:
        curr = move_blizzard(curr)
        bliz_steps = [set(map(lambda x : x[0], b)) for b in bliz_steps]
        yield bliz_steps

def solve():
    I = 1000
    bliz_steps = [0]*(I+1)
    bliz_steps[0] = BLIZZARDS
    for _ in range(I):
        bliz_steps[_+1] = move_blizzard(bliz_steps[_])

    bliz_steps = [set(map(lambda x : x[0], b)) for b in bliz_steps]

    at = start
    # steps, at
    Q = deque()
    Q.append((0, at))
    SEEN = set()

    while Q:
        steps, at = Q.popleft()
        if at == finish:
            break

        if (steps, at) in SEEN:
            continue
        SEEN.add((steps, at))

        bliz = bliz_steps[steps+1]
        for d in [DOWN, RIGHT, UP, LEFT]:
            new_at = add_points(at, d)
            if new_at not in bliz and new_at not in WALLS:
                Q.append((steps+1, new_at))

        if at not in bliz:
            Q.append((steps+1, at))

    assert at == finish 
    return steps
         
print(solve())