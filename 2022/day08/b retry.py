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

    def score_vis(pos_r, pos_c, inc_r, inc_c):
        h = trees[(pos_r,pos_c)]
        count = 0
        curr_r, curr_c = pos_r + inc_r, pos_c + inc_c
        while curr_r in range(H) and curr_c in range(W):
            count += 1

            if h <= trees[(curr_r,curr_c)]:
                break
            curr_r, curr_c = curr_r + inc_r, curr_c + inc_c

        return count

    max_score = 0
    for pos_r, pos_c in visible:
        score = 1
        score *= score_vis(pos_r, pos_c, +1, +0)
        score *= score_vis(pos_r, pos_c, -1, +0)
        score *= score_vis(pos_r, pos_c, +0, +1)
        score *= score_vis(pos_r, pos_c, +0, -1)
        max_score = max(max_score, score)

    print(max_score)

if __name__ == "__main__":
    main()