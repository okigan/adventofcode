#! /usr/bin/env python

print('hello')

import os
import sys
import re

from functools import * 
from collections import *

def main():
    heigh_map = []
    with open('./input1.txt', 'rt') as f:
        while True:
            line = f.readline().strip()
            if len(line) == 0:
                break
            digits = re.split('', line)
            digits = filter(lambda x: len(x)>0, digits)
            numbers = [int(d) for d in digits]
            heigh_map += [numbers]

    mins = {}
    for r in range(len(heigh_map)):
        for c in range(len(heigh_map[0])):
            coords = [(r + 1, c + 0), (r - 1, c + 0),(r + 0, c + 1), (r + 0, c - 1)]

            surround_min = +float('inf')
            for rr, cc in coords:
                if rr >= 0 and rr < len(heigh_map):
                    if cc >= 0 and cc < len(heigh_map[0]):
                        surround_min = min(surround_min, heigh_map[rr][cc])
            if heigh_map[r][c] < surround_min:
                mins[(r,c,)] = heigh_map[r][c]

    risk_level = sum(mins.values()) + len(mins.values())

    basin_sizes = []
    for (mr,mc), value in mins.items():
        counted = 0
        q = deque([(mr,mc)])
        visited = set()
        while q:
            (r, c) = q.popleft()
            if (r,c) not in visited:
                counted += 1
                visited.add((r,c))
                for rr, cc in [(r + 1, c + 0), (r - 1, c + 0),(r + 0, c + 1), (r + 0, c - 1)]:
                    if rr >= 0 and rr < len(heigh_map):
                        if cc >= 0 and cc < len(heigh_map[0]):
                            if heigh_map[rr][cc] != 9:
                                q += [(rr, cc)]
        basin_sizes += [counted]
    basin_sizes = sorted(basin_sizes)
    prod = reduce(lambda x,y: x*y, basin_sizes[-3:])

    return prod
print(main())   