#! env python

from itertools import *
from functools import *
from collections import *
from operator import *

import os 

dir_path = os.path.dirname(os.path.realpath(__file__))

def main():

    trees = []
    with open(dir_path + "/input.txt") as f:
        for line in f.readlines():
            line = line.strip()
            t = []
            for c in line:
                t += [int(c)]

            trees += [t]

    visible = set()
    # left to right
    for idx_r in range(len(trees)):
        ROW = trees[idx_r]
        for idx_c in range(len(ROW)):
            h = ROW[idx_c]
            if idx_c == 0 or idx_c == len(ROW) - 1 or idx_r == 0 or idx_r == len(trees[0]) - 1:
                visible.add((idx_r, idx_c))
                m = h
            if h > m:
                visible.add((idx_r, idx_c))
                m = h

    # right to left
    for idx_r in range(len(trees) - 1, -1, -1):
        ROW = trees[idx_r]
        for idx_c in range(len(ROW) - 1, -1, -1):
            h = ROW[idx_c]
            if idx_c == 0 or idx_c == len(ROW) - 1 or idx_r == 0 or idx_r == len(trees[0]) - 1:
                visible.add((idx_r, idx_c))
                m = h
            if h > m:
                visible.add((idx_r, idx_c))
                m = h

    # top to bottom
    for idx_c in range(len(trees[0])):
        for idx_r in range(len(trees)):
            ROW = trees[idx_r]
            h = ROW[idx_c]
            if idx_c == 0 or idx_c == len(ROW) - 1 or idx_r == 0 or idx_r == len(trees[0]) - 1:
                visible.add((idx_r, idx_c))
                m = h
            if h > m:
                visible.add((idx_r, idx_c))
                m = h

    # bottom to top
    for idx_c in range(len(trees[0])):
        for idx_r in range(len(trees)-1, -1, -1):
            ROW = trees[idx_r]
            h = ROW[idx_c]
            if idx_c == 0 or idx_c == len(ROW) - 1 or idx_r == 0 or idx_r == len(trees[0]) - 1:
                visible.add((idx_r, idx_c))
                m = h
            if h > m:
                visible.add((idx_r, idx_c))
                m = h

    print(len(visible))

    def score_vis(pos_r, pos_c, inc_r, inc_c):
        h = trees[pos_r][pos_c]
        count = 0
        curr_r, curr_c = pos_r + inc_r, pos_c + inc_c
        while curr_r >= 0 and curr_r < len(trees) and curr_c >= 0 and curr_c < len(trees[0]):
            count += 1

            if h <= trees[curr_r][curr_c]:
                break
            curr_r, curr_c = curr_r + inc_r, curr_c + inc_c

        return count

    max_score = 0
    
    for pos_r, pos_c in visible:
        score = 1
        score  *= score_vis(pos_r, pos_c, -1, +0)
        score  *= score_vis(pos_r, pos_c, +0, -1)
        score  *= score_vis(pos_r, pos_c, +1, +0)
        score  *= score_vis(pos_r, pos_c, +0, +1)

        max_score = max(max_score, score)
    
    print(max_score)



if __name__ == "__main__":
    main()