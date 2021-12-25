#! /usr/bin/env python

print('hello')

import os
import sys
import re

from functools import * 
from collections import *
from itertools import * 

from queue import PriorityQueue


def main():
    terrain = []
    with open('./input.txt', 'rt') as f:
        while True:
            line = f.readline().strip()
            if len(line) == 0:
                break
            digits = list(map(int, list(line)))
            terrain += [digits]


    q = deque()
    q.append((0, (0, 0)))

    incs = [(+1, 0), (-1, 0),(0, +1), (0, -1)]

    visited = {}
    while q:
        cost, (r, c) = q.popleft()

        if r == len(terrain) - 1 and c == len(terrain[0]):
            print(cost)

        if (r, c) not in visited or visited[(r,c)] > cost:
            visited[(r, c)] = cost

            for inc in incs:
                RR, CC = r + inc[0], c + inc[1]


                if RR >= 0 and RR < len(terrain):
                    if CC >= 0 and CC < len(terrain[RR]):
                        q.append((terrain[RR][CC] + cost, (RR, CC)))

    print('end')
    return visited[(len(terrain)-1, len(terrain[0]) -1)]







 

print(main())   