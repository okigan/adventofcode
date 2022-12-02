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

    pos = (0,0)

    d = defaultdict(int)

    d[pos] += 1

    for c in directions:
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

        d[pos] += 1

    count = 0
    for k,v in d.items():
        if v >= 1:
            count += 1
    
    print(count)


if __name__ == "__main__":
    main()