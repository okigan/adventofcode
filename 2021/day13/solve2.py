#! /usr/bin/env python

print('hello')

import os
import sys
import re

from functools import * 
from collections import *
from itertools import * 

def main():
    dots = []
    folds = []
    with open('./input.txt', 'rt') as f:
        while True:
            line = f.readline().strip()
            if len(line) == 0:
                break
            coord = re.split(',', line)
            coord = list(map(int, coord))
            dots += [coord]

        while True:
            line = f.readline().strip()
            if len(line) == 0:
                break
            fold = re.split('=', line)
            folds += [(fold[0], int(fold[1]))]

    maxC, maxR = -float('inf'), -float('inf')

    for x,y in dots:
        maxC = max(maxC, x)
        maxR = max(maxR, y)

    m = [None] * (maxR + 1)
    for r in range(maxR + 1):
        m[r] = [0] * (maxC + 1)

    for c,r in dots:
        m[r][c] = 1

    for fold_dir, pos in folds:
        if fold_dir == 'fold along y':
            for r in range(pos, len(m)):
                offset = r - pos 
                for c in range(0, len(m[r])):
                    m[pos - offset][c] |= m[r][c]
            del m[pos:]
        x = sum(chain(*m))
        
        if fold_dir == 'fold along x':
            for r, ROW in enumerate(m):
                for c in range(pos + 1, len(ROW)):
                    offset = c - pos
                    m[r][pos - offset] |= m[r][c]
                del ROW[pos:]

    lines = []
    for r in m:
        lines.append(''.join([{0:' ', 1:'X'}[x] for x in r]))
    
    for l in lines:
        print(l)

 

main()