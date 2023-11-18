from time import perf_counter


with open('input.txt', 'r') as file:
    line = file.readlines()[0]
    data = [1 if dir == '>' else -1 for dir in line]

"""
####

.#.
###
.#.

..#
..#
###

#
#
#
#

##
##
"""
def get_piece(iterations, y):
    pieceI = iterations % 5
    pieces = {
        0 : [(2, y+0), (3, y+0), (4, y+0), (5, y+0)],
        1 : [(3, y+0), (2, y+1), (3, y+1), (4, y+1), (3, y+2)],
        2 : [(4, y+2), (4, y+1), (4, y+0), (3, y+0), (2, y+0)],
        3 : [(2, y+0), (2, y+1), (2, y+2), (2, y+3)],
        4 : [(2, y+0), (3, y+0), (3, y+1), (2, y+1)]
    }
    return pieces[pieceI]

def move_piece_x(piece : set[tuple[int]], dir) -> set[tuple[int]]:
    if min(x for x, _ in piece) == 0 and dir == -1 or max(x for x, _ in piece) == 6 and dir == 1:
        return piece
    return set(map(lambda x : (x[0]+dir, x[1]), piece))

def move_piece_y(piece : set[tuple[int]], dir) -> set[tuple[int]]:
    return set(map(lambda x : (x[0], x[1]+dir), piece))

def signature(tower : set[int], pieceI, dataI):
    maxY = max(y for _, y in tower)
    towerTop = filter(lambda x : x[1] > maxY - 20, tower)
    towerTop_moved = map(lambda x : (x[0], x[1] - maxY), towerTop)
    sign = (pieceI, dataI, frozenset(towerTop_moved))
    return sign

def visualize(tower : set[(int, int)]) -> str:
    maxY = max(y for _, y in tower)
    grid = []
    
    for y in range(1, maxY + 1):
        row = []
        for x in range(7):
            if (x, y) in tower:
                row.append('#')
            else:
                row.append('.')
        
        grid.append(row)

    return "\n".join("".join(row) for row in reversed(grid))

def solve(total_iterations : int):
    seen = set()
    when_height = {}
    tower = set((x, 0) for x in range(7))
    dataI = 0
    iterations = 0
    repeated = False
    added_height = 0

    while iterations < total_iterations:
        maxY = max(y for _, y in tower)
        curr = get_piece(iterations, maxY+4)

        sign = signature(tower, iterations % 5, dataI)
        if sign in seen and not repeated:
            old_iterations, old_height = when_height[sign]
            repeat = (total_iterations - iterations) // (iterations - old_iterations)
            added_height = repeat * (maxY - old_height)
            iterations += (iterations - old_iterations) * repeat
            repeated = True
        
        seen.add(sign)
        when_height[sign] = (iterations, maxY)
        
        # While curr hasn't hit previously stopped blocks
        while not any(c in tower for c in curr):
            # Push
            newCurr = move_piece_x(curr, data[dataI])

            # Pushed into fallen blocks
            if any(c in tower for c in newCurr):
                newCurr = curr

            # Fall
            curr = move_piece_y(newCurr, -1)

            dataI = (dataI + 1) % len(data)

        curr = move_piece_y(curr, 1)
        tower |= curr
        iterations += 1

    maxY = max(y for _, y in tower)
    return maxY + added_height

start = perf_counter()
print(solve(2022))
print(solve(1000000000000))
print(f"Finished in : {perf_counter() - start}s")