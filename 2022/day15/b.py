#! env python

from itertools import *
from functools import *
from collections import *

import os 
import re

dir_path = os.path.dirname(os.path.realpath(__file__))

def range_intersection(ra_start, ra_end, rb_start, rb_end):
    return max(ra_start, rb_start), min(ra_end -1, rb_end-1)+1



def draw_diamond(space, s, distance, special_row, special_ranges:list):

    d = abs(s[1] - special_row)

    if d < distance:
        px = s[0] + (distance - d)
        nx = s[0] - (distance - d)
        special_ranges += [[nx, px]]

    return
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

    max_val = 4000000
    y = 0
    while y < max_val:
        x = 0
        while x < max_val:
            found_sensor = False
            for idx, (s, b) in enumerate(data):
                distance = calc_distance(s, b)
                if calc_distance(s, (x, y)) < distance: 
                    x = s[0] + distance - abs(s[1] - y) + 1
                    found_sensor = True
                if x >= max_val:
                    break
            if not found_sensor:
                print(x * 4000000 + y)
        y += 1



    special_row = 2000000
    special_ranges = []
    space = defaultdict(lambda: ' ')
    sub = 0
    for s, b in data:
        print(f"processing {s} {b}")
        distance = calc_distance(s, b)
        draw_diamond(space, s, distance, special_row, special_ranges)
        draw_marker(space, s, "S")
        draw_marker(space, b, "B")

        if s[1] == special_row:
            sub += 1
        if b[1] == special_row:
            sub += 1
    # print_space(space)

    special_row_as_set = set()
    for s in special_ranges:
        special_row_as_set.update(range(min(s[0], s[1]), max(s[0], s[1])))

    print("result: ", len(special_row_as_set))
    m = min(special_row_as_set)

    count = 0
    for i in range(len(special_ranges)):
        ra = special_ranges[i]
        count += abs(ra[0] - ra[1])

    for i in range(len(special_ranges)):
        ra = special_ranges[i]
        for j in range(i+1, len(special_ranges)):
            rb = special_ranges[j]

            istart, iend = range_intersection(ra[0], ra[1], rb[0], rb[1])
            count -= 2* abs(istart - iend)

    picked_values = []
    
    for k, v in space.items():
        if k[1] == special_row:
            picked_values += [v]
            
    print(Counter(picked_values))


if __name__ == "__main__":
    main()