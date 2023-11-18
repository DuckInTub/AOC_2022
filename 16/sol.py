from collections import defaultdict, deque
from copy import copy, deepcopy
from itertools import combinations, permutations, product
import re
import numpy as np
from time import perf_counter
from functools import cache


start_time = perf_counter()

with open("./16/input.txt", "r") as file:
    lines = file.readlines()
    lines.sort(key=lambda x : x[6] + x[7])
    data = []
    nodes = {}
    values = []
    edges = np.zeros((len(lines), len(lines)), int)
    
    for line in lines:
        item = re.findall("[A-Z0-9]+", line[1:])
        name = item[0]
        value = int(item[1])
        connections = item[2:]

        data.append((name, value, connections))
        nodes[name] = value
        values.append(value)

    for name, value, connections in data:
        names = list(nodes.keys())
        r = names.index(name)
        c = [names.index(con) for con in connections]
        for col in c:
            edges[r][col] = 1
            edges[col][r] = 1

    dists = np.zeros(edges.shape, int)
    m = deepcopy(edges)
    for dist in range(1, len(values)+1):
        dists[np.logical_and(m > 0, dists == 0)] = dist
        m = np.matmul(m, edges)
        m[m > 0] = 1

@cache
def solve(at : int, opened : int, time : int) -> int:
    bits = bin(opened)[2:][::-1]
    pressure_per_minute = sum(v for v, b in zip(values, bits) if b == '1')

    # Determine what valves can be opened in time
    not_opened = []
    for valve, value in enumerate(values):
        if value > 0 and not bool(opened & (1 << valve)) and valve != at and dists[at][valve] + 2 <= time:
            not_opened.append(valve)
    
    # Get distances to closed valves
    distances = dists[at][np.array(not_opened, int)]

    # If there are no valves to open, 
    # or there are no valves we can open in time,
    # let the pressure release during the remaining time.
    if not not_opened or all(d + 2 > time for d in distances):
        return time * pressure_per_minute

    # For each valve that could be opened, calculate the maximum
    # possible preassure release after opening that valve,
    # then take the maxium of all of those.
    mx = 0
    for valve, dist in zip(not_opened, distances):
        new_opened = opened | (1 << valve)
        new_time = time - (dist + 1)
        new_released = (dist + 1) * pressure_per_minute

        assert new_time > 0
        
        mx = max(mx, new_released + solve(valve, new_opened, new_time))

    return mx

def solve2(start : int, time : int):
    # At, opened, time, released
    Q = deque([(start, 0, time, 0)])
    best = defaultdict(lambda : -1)
    while Q:
        info = Q.pop()
        at, opened, time, released = info
        best[opened] = max(best[opened], released)
        for valve, flow in enumerate(values):
            if flow <= 0 or opened & (1 << valve) != 0:
                continue
            dist = dists[at][valve]
            if time - dist - 1 > 0:
                new_released = released + flow * (time - dist - 1)
                new_opened = opened | (1 << valve)
                Q.append((valve, new_opened, time - dist - 1, new_released))

    return max(best.values())

print(solve(0, 0, 30))
print(f"Finished in {perf_counter() - start_time}s")



print(solve2(0, 30))
print(f"Finished in {perf_counter() - start_time}s")