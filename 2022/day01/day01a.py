#! env python

from itertools import *
from functools import *
from collections import *

import os 

dir_path = os.path.dirname(os.path.realpath(__file__))

def main():
    elves = [[]]
    with open(dir_path + "/input.txt") as f:
        for line in f.readlines():
            line = line.strip()
            if line == "":
                elves += [[]]
            else:
                elves[-1] += [int(line)]

    d = {}
    for i, e in enumerate(elves):
        d[i] = sum(e)

    i = -1
    m = 0
    for k,v in d.items():
        if v > m:
            m = v
            i = k

    print(i, m)

if __name__ == "__main__":
    main()