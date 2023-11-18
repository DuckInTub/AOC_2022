from collections import deque

with open("input.txt", "r") as file:
    cords = set(map(eval, file.readlines()))
    maxX = max(x for x, _, _ in cords)
    maxY = max(y for _, y, _ in cords)
    maxZ = max(z for _, _, z in cords)

def sides(x, y, z):
    yield x+1,y,z
    yield x-1,y,z
    yield x,y+1,z
    yield x,y-1,z
    yield x,y,z+1
    yield x,y,z-1

OUT = set()
IN = set()
def reaches_outside(sX, sY, sZ):
    global OUT
    global IN
    start = (sX, sY, sZ)
    if start in OUT:
        return True
    if start in IN:
        return False
    SEEN = set()
    Q = deque([start])
    iterations = 0
    while Q:
        assert iterations < 30 ** 3
        x, y, z = Q.popleft()
        
        if (x, y, z) in cords or (x, y, z) in SEEN:
            continue

        SEEN.add((x, y, z))

        if (x, y, z) in OUT or x > 2 + maxX or y > 2 + maxY or z > 2 + maxZ or x < -2 or y < -2 or z < -2:
            OUT |= SEEN
            return True
        
        for x, y, z in sides(x, y, z):
            Q.append((x, y, z))

        iterations += 1

    IN |= SEEN
    return False


ans1 = 0
ans2 = 0
for cord in cords:
    for x, y, z in sides(*cord):
        if (x, y, z) not in cords:
            ans1 += 1
        if reaches_outside(x, y, z) and (x, y, z) not in cords:
            ans2 += 1


print(ans1)
print(ans2)
