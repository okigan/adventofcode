#! env python

from itertools import *
from functools import *
from collections import *

import os 

dir_path = os.path.dirname(os.path.realpath(__file__))

def main():
    directions = ''
    with open(dir_path + "/input.txt") as f:
        for line in f.readlines():
            directions = line
            break

    santa_pos = (0,0)
    robo_pos = (0,0)

    d = defaultdict(int)

    d[santa_pos] += 1
    d[robo_pos] += 1

    for idx,c in enumerate(directions):
        if idx % 2 == 0:
            santa_pos = next_pos(santa_pos, c)
            d[santa_pos] += 1
        else:
            robo_pos = next_pos(robo_pos, c)
            d[robo_pos] += 1

    count = 0
    for k,v in d.items():
        if v >= 1:
            count += 1
    
    print(count)

def next_pos(pos, c):
    if c == "^":
        pos = pos[0], pos[1] - 1
    elif c == "v":
        pos = pos[0], pos[1] + 1
    elif c == ">":
        pos = pos[0] + 1, pos[1]
    elif c == "<":
        pos = pos[0] - 1, pos[1]
    else:
        print( "should not be here")
    return pos


if __name__ == "__main__":
    main()