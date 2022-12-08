#! env python

from itertools import *
from functools import *
from collections import *

import os 

dir_path = os.path.dirname(os.path.realpath(__file__))

def main():
    field = []    
    with open(dir_path + "/input.txt") as f:
        for line in f.readlines():
            line = line.strip()
            field += [list(map(lambda x: int(x), list(line)))]

    trees = {}
    W = len(field[0])
    H = len(field)

    for r in range(H):
        for c in range(W):
            trees[(r, c)] = field[r][c]

    visible = {}
    # left to right
    for r in range(H):
        m = -9999
        for c in range(W):
            if trees[(r,c)] > m:
                visible[(r,c)] = True
                m = trees[(r,c)]


    # right to left
    for r in range(H):
        m = -9999
        for c in range(W-1, -1, -1):
            if trees[(r,c)] > m:
                visible[(r,c)] = True
                m = trees[(r,c)]

    # top to bottom
    for c in range(W):
        m = -9999
        for r in range(H):
            if trees[(r,c)] > m:
                visible[(r,c)] = True
                m = trees[(r,c)]

    # bottom to top
    for c in range(W):
        m = -9999
        for r in range(H-1, -1, -1):
            if trees[(r,c)] > m:
                visible[(r,c)] = True
                m = trees[(r,c)]

    print(len(visible))

if __name__ == "__main__":
    main()