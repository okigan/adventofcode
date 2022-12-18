#! env python

from itertools import *
from functools import *
from collections import *

import os 
import re

dir_path = os.path.dirname(os.path.realpath(__file__))

def draw_diamond(space, s, distance, special_row):
    for dd in range(distance+1):
        for d in range(dd+1):
            px = s[0] + d
            py = s[1] + dd - d
            space[(px, py)] = '#'

            px = s[0] - d
            py = s[1] + dd - d
            space[(px, py)] = '#'

            px = s[0] + d
            py = s[1] - (dd - d)
            space[(px, py)] = '#'

            px = s[0] - d
            py = s[1] - (dd - d)
            space[(px, py)] = '#'


        
    # for r in range(distance):
    
    #     for i in [dy]:
    #         px = s[0] + i
    #         py = s[1] + (r - i)
    #         if py == special_row:
    #             space[(px, py)] = '#'

    #         px = s[0] - i
    #         py = s[1] + (r - i)
    #         if py == special_row:
    #             space[(px, py)] = '#'

    #         px = s[0] + i
    #         py = s[1] - (r - i)
    #         if py == special_row:
    #             space[(px, py)] = '#'

    #         px = s[0] - i
    #         py = s[1] - (r - i)
    #         if py == special_row:
    #             space[(px, py)] = '#'

def calc_distance(s, b):
    return abs(s[0] - b[0]) + abs(s[1] - b[1])

def print_space(space):
    if len(space.keys()) == 0:
        return 

    minx = min(k[0] for k in space.keys())
    maxx = max(k[0] for k in space.keys())
    miny = min(k[1] for k in space.keys())
    maxy = max(k[1] for k in space.keys())

    print(minx, maxx)
    for y in range(miny, maxy + 1):
        chars = ''.join(space[(x, y)] for x in range(minx, maxx + 1))
        print(f"{y:02}  {chars}")
    print()

def draw_marker(space, p, m):
    space[p] = m


def main():
    data = []
    with open(dir_path + "/input.txt") as f:
        for line in f.readlines():
            line = line.strip()
            numbers = re.findall(r"Sensor at x=([-+]?[0-9]+), y=([-+]?[0-9]+): closest beacon is at x=([-+]?[0-9]+), y=([-+]?[0-9]+)", line)
            numbers = list(numbers[0])
            numbers = list(map(lambda x: int(x), numbers))
            data += [[(numbers[0], numbers[1]), (numbers[2], numbers[3])]]
            # print(line)

    print(len(data))
    for s, b in data:
        print(s, b)


    special_row = 10
    space = defaultdict(lambda: ' ')
    for s, b in data:
        distance = calc_distance(s, b)
        draw_diamond(space, s, distance, special_row)
        draw_marker(space, s, "S")
        draw_marker(space, b, "B")
    print_space(space)

    picked_values = []
    
    for k, v in space.items():
        if k[1] == special_row:
            picked_values += [v]
            
    print(Counter(picked_values))


if __name__ == "__main__":
    main()