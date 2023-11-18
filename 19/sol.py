from collections import deque
from itertools import product
from math import prod
import re

with open("input.txt", "r") as file:
    data = [tuple(map(int, re.findall("[0-9]+", line)[1:])) for line in file.readlines()]


# Tuple have field:
# Ore: ore cost, Clay: ore cost, Obsidian: ore cost, Obsidian: clay cost, Geode: ore cost, Geode: obsidian cost
# Data tuples are (orC, cC, obOC, obCC, gOC, gOBC)

def max_geodes(blueprint : tuple[int], time : int):
    # Items in queue are (time, ore, clay, obsidian, geode, r1, r2, r3, r4)
    Q = deque([(time, 0, 0, 0, 0, 1, 0, 0, 0)])
    SEEN = set()
    best = 0
    max_ore_cost = max(cost for i, cost in enumerate(blueprint) if i not in [3, 5])
    while Q:
        P = Q.popleft()
        time, ore, clay, obsidian, geode, r1, r2, r3, r4 = P 
        best = max(best, geode)

        if time <= 0:
            continue

        if ore >= (mx_ore := time*max_ore_cost - r1*(time - 1)):
            ore = mx_ore
        
        if clay >= (mx_clay := time*blueprint[3] - r2*(time - 1)):
            clay = mx_clay

        if obsidian >= (mx_obsidian := time*blueprint[5] - r3*(time - 1)):
            obsidian = mx_obsidian

        P = (time, ore, clay, obsidian, geode, r1, r2, r3, r4) 

        if P in SEEN:
            continue
        SEEN.add(P)

        if ore >= blueprint[0] and r1 < max_ore_cost + 1: # Craft ore robot
            Q.append((time-1, ore+r1-blueprint[0], clay+r2, obsidian+r3, geode+r4, r1+1, r2, r3, r4))

        if ore >= blueprint[1] and r2 < blueprint[3] + 1: # Craft clay robot
            Q.append((time-1, ore+r1-blueprint[1], clay+r2, obsidian+r3, geode+r4, r1, r2+1, r3, r4))

        if ore >= blueprint[2] and clay >= blueprint[3] and r3 < blueprint[5] + 1: # Craft obsidian robot
            Q.append((time-1, ore+r1-blueprint[2], clay+r2-blueprint[3], obsidian+r3, geode+r4, r1, r2, r3+1, r4))

        if ore >= blueprint[4] and obsidian >= blueprint[5]: # Craft geode robot
            Q.append((time-1, ore+r1-blueprint[4], clay+r2, obsidian+r3-blueprint[5], geode+r4, r1, r2, r3, r4+1))

        Q.append((time-1, ore+r1, clay+r2, obsidian+r3, geode+r4, r1, r2, r3, r4))
    return best

print(data[0])

print(sum(max_geodes(blueprint, 24)*(i+1) for i, blueprint in enumerate(data)))
print(prod(max_geodes(blueprint, 32) for blueprint in data[:3]))