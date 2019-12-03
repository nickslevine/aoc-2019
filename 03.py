from math import inf
from utils import read_input
import cProfile


def manhattan_distance(coord1, coord2):
    return abs(coord1[0] - coord2[0]) + abs(coord1[1] - coord2[1])


def update_loc(update, cache):
    coords = cache[-1][:]
    direction = update[0]
    magnitude = int(update[1:])
    if direction == 'R':
        for m in range(1, magnitude + 1):
            coords[0] += 1
            cache.append(coords[:])
    elif direction == 'L':
        for m in range(1, magnitude + 1):
            coords[0] -= 1
            cache.append(coords[:])
    elif direction == 'U':
        for m in range(1, magnitude + 1):
            coords[1] += 1
            cache.append(coords[:])
    elif direction == 'D':
        for m in range(1, magnitude + 1):
            coords[1] -= 1
            cache.append(coords[:])
    else:
        raise ValueError("Problem with input", update)
    return cache


def get_overlaps(str1, str2):
    updates1 = str1.split(',')
    updates2 = str2.split(',')
    loc1_cache = [[0, 0]]
    loc2_cache = [[0, 0]]
    overlaps = []
    for u in updates1:
        loc1_cache = update_loc(u, loc1_cache)
    for u in updates2:
        loc2_cache = update_loc(u, loc2_cache)
    for l in loc1_cache:
        if l in loc2_cache:
            overlaps.append(l[:])

    return [loc1_cache, loc2_cache, overlaps]


def find_min_distance(overlaps):
    min_distance = inf
    min_coord = [0, 0]
    for c in overlaps:
        dist = manhattan_distance([0, 0], c)
        if dist < min_distance:
            min_distance = dist
            min_coord = c
    return min_distance


def solve1(str1, str2):
    overlaps = get_overlaps(str1, str2)[2]
    overlaps = [x for x in overlaps if x[0] != 0 and x[1] != 0]
    return find_min_distance(overlaps)


assert solve1("R8,U5,L5,D3", "U7,R6,D4,L4") == 6
assert solve1("R75,D30,R83,U83,L12,D49,R71,U7,L72",
              "U62,R66,U55,R34,D71,R55,D58,R83") == 159
assert solve1("R98,U47,R26,D63,R33,U87,L62,D20,R33,U53,R51",
              "U98,R91,D20,R16,D67,R40,U7,R15,U6,R7") == 135

inputstrings = read_input("03.txt")
print(solve1(inputstrings[0], inputstrings[1]))


def solve2(str1, str2):
    results = get_overlaps(str1, str2)
    min_steps = inf
    for o in results[2][1:]:
        combined_steps = 0
        combined_steps += results[0].index(o)
        combined_steps += results[1].index(o)
        if combined_steps < min_steps:
            min_steps = combined_steps
    return min_steps


assert solve2("R75,D30,R83,U83,L12,D49,R71,U7,L72",
              "U62,R66,U55,R34,D71,R55,D58,R83") == 610
assert solve2("R98,U47,R26,D63,R33,U87,L62,D20,R33,U53,R51",
              "U98,R91,D20,R16,D67,R40,U7,R15,U6,R7") == 410
cProfile.run('print(solve2(inputstrings[0], inputstrings[1]))')
