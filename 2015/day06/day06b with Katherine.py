#! env python

from itertools import *
from functools import *
from collections import *

import os 
import re

dir_path = os.path.dirname(os.path.realpath(__file__))

def main():

    commands = []
    with open(dir_path + "/input.txt") as f:
        for line in f.readlines():
            line = line.strip()
            m = re.match("(.*) (\d+),(\d+) .* (\d+),(\d+)", line)
            commands += [(m.group(1), int(m.group(2)), int(m.group(3)), int(m.group(4)), int(m.group(5)))]

    lights = defaultdict(int)
    for c in commands:
        cm,fx,fy,tx,ty = c[0], c[1], c[2], c[3], c[4]

        if cm == "turn on":
            for i in range(fx, tx + 1):
                for j in range(fy, ty + 1):
                    lights[(i,j)] += 1
        elif cm == "turn off":
            for i in range(fx, tx + 1):
                for j in range(fy, ty + 1):
                    lights[(i,j)] -= 1
                    if lights[(i,j)] < 0:
                        lights[(i,j)] = 0
        elif cm == "toggle":
            for i in range(fx, tx + 1):
                for j in range(fy, ty + 1):
                    lights[(i,j)] += 2

    total = 0
    for v in lights.values():
        if v:
            total += v
    print(total)

    # for c in commands:
    #     cm,fx,fy,tx,ty = c[0], c[1], c[2], c[3], c[4]
    #     current_set = set()
    #     for i in range(fx, tx + 1):
    #         for j in range(fy, ty + 1):
    #             current_set.add((i, j))
    #     if cm == "turn on":
    #         s = s.union(current_set)
    #     elif cm == "turn off":
    #         s = s - current_set
    #     elif cm == "toggle":
    #         to_turn_off = s.intersection(current_set)
    #         to_turn_on = current_set - s
    #         s = s - to_turn_off
    #         s = s.union(to_turn_on)


if __name__ == "__main__":
    main()