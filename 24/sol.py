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

BLIZZARDS = set()
WALLS = set()
with open('input.txt', 'r') as file:
    start = (0, 1)
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
    WALLS.add((-1, 1))
    WALLS.add(add_points(finish, DOWN))
    WALLS.add(add_points(finish, RIGHT))

    I = 1000
    bliz_steps = [0]*(I+1)
    bliz_steps[0] = BLIZZARDS
    for _ in range(I):
        bliz_steps[_+1] = move_blizzard(bliz_steps[_])

    bliz_steps = [set(p[0] for p in b) for b in bliz_steps]

def visualize_blizzard(points, walls):
    m = [['.']*(max_c+1) for _ in range(max_r+1)]
    for blizz in points:
        at, facing = blizz
        r, c = at
        char = '^>v<'[DIRS.index(facing)]
        if m[r][c] not in '^>v<':
            m[r][c] = char
        elif m[r][c] in '^>v<':
            m[r][c] = str(2)
        elif m[r][c] in '123456789':
            m[r][c] = str(int(m[r][c])+1)
    
    for wall in walls:
        r, c = wall
        m[r][c] = '#'

    for row in m:
        print("".join(row))
    print()

def get_next_blizzard_state():
    curr = BLIZZARDS
    while True:
        curr = move_blizzard(curr)
        bliz_steps = [set(map(lambda x : x[0], b)) for b in bliz_steps]
        yield bliz_steps

def solve(st, fi, init_time, dirs):
    # steps, at
    Q = deque()
    Q.append((0, st))
    SEEN = set()

    while Q:
        steps, at = Q.popleft()
        if at == fi:
            break

        if (steps, at) in SEEN:
            continue
        SEEN.add((steps, at))

        # Get the next blizzard
        bliz = bliz_steps[init_time+steps+1]

        # Check all directions, if there isn't a blizzard there
        # then we can try moving there.
        for d in dirs:
            nr, nc = add_points(at, d)
            if (nr, nc) not in bliz and (nr, nc) not in WALLS:
                Q.append((steps+1, (nr, nc)))

        # We can always stay on the starting square
        if at not in bliz or at == st:
            Q.append((steps+1, at))

    assert at == fi 
    return steps
         
start_finish = solve(start, finish, 0, (DOWN, RIGHT, UP, LEFT))
print(start_finish)

finish_start = solve(finish, start, start_finish, (UP, LEFT, DOWN, RIGHT))
start_finish_2 = solve(start, finish, finish_start+start_finish, (DOWN, RIGHT, UP, LEFT))
print(start_finish,finish_start,start_finish_2)
print(start_finish+finish_start+start_finish_2)