#! env python

from itertools import *
from functools import *
from collections import *

import os 

dir_path = os.path.dirname(os.path.realpath(__file__))

def main():
    lines = []

    with open(dir_path + "/input.txt") as f:
        for line in f.readlines():
            line = line.strip()
            point_descs = line.split(" -> ")
            points = []
            for point_desc in point_descs:
                strs = point_desc.split(",")
                coords = list(map(lambda x: int(x), strs))
                points += [(coords[0], coords[1])]
            lines += [points]

    print(lines)

    minx = float('inf')
    miny = float('inf')

    maxx = -float('inf')
    maxy = -float('inf')

    for line in lines:
        for point in line:
            minx, miny = min(minx, point[0]), min(miny, point[1])
            maxx, maxy = max(maxx, point[0]), max(maxy, point[1])

    start = (500, 0)
    minx = min(start[0], int(minx))
    maxx = max(start[0], int(maxx))
    miny = min(start[1], int(miny))
    maxy = max(start[1], int(maxy))

    print(minx, miny, maxx, maxy)

    space = defaultdict(lambda: '.')
    for line in lines:
        for idx in range(len(line) - 1):
            a = line[idx]
            b = line[idx + 1]
            for r in range(min(b[1], a[1]), max(b[1], a[1])+1):
                for c in range(min(b[0], a[0]), max(b[0], a[0])+1):
                    space[(c, r)] = '#'

    print_space(space)

    counter = 0
    while drop_sand(start, space, minx, miny, maxx, maxy):
        print(Counter(space.values()))
        counter += 1
        if counter % 10000 == 0: 
            print_space(space)


def drop_sand(start, space, minx, miny, maxx, maxy):
    sand = start
    moved = True

    increments = [(0, 1), (-1, 1), (1, 1)]

    while moved and sand[1] < maxy + 1:
        moved = False

        for incx, incy in increments:
            next_sand_pos = (sand[0] + incx, sand[1] + incy)
            if space[next_sand_pos] == ".":
                sand = next_sand_pos
                moved = True
                break
            else:
                pass

    space[sand] = 'o'
    return True

 
def print_space(space):
    minx = min(k[0] for k in space.keys())
    maxx = max(k[0] for k in space.keys())
    miny = min(k[1] for k in space.keys())
    maxy = max(k[1] for k in space.keys())

    for y in range(miny, maxy + 1):
        for x in range(minx, maxx + 1):
            print(space[(x, y)], end="")
        print()



if __name__ == "__main__":
    main()