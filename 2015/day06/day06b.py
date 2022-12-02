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


    d = defaultdict(int)
    for c in commands:
        cm, fx,fy,tx,ty = c[0], c[1], c[2], c[3], c[4]
        current_set = set()
        for i in range(fx, tx + 1):
            for j in range(fy, ty + 1):
                current_set.add((i, j))
        if cm == "turn on":
            # increase the brightness of those lights by 1.
            for i in current_set:
                d[i] += 1
        elif cm == "turn off":
            # decrease the brightness of those lights by 1
            for i in current_set:
                if d[i] <= 1:
                    del d[i]
                else:
                    d[i] -= 1
        elif cm == "toggle":
            # increase the brightness of those lights by 2.
            for i in current_set:
                d[i] += 2000

    total = 0
    for v in d.values():
        total += v
    print(v)

if __name__ == "__main__":
    main()