#! /usr/bin/env python

from itertools import *
from functools import *
from queue import PriorityQueue
from collections import *
import re
import sys
import os
print('hello')

def wrappp(x):
    if x < 10:
        return x
    else:
        return wrappp(x // 10 + (x % 10))

def main():
    terrain = []
    with open('./input.txt', 'rt') as f:
        while True:
            line = f.readline().strip()
            if len(line) == 0:
                break
            digits = list(map(int, list(line)))
            terrain += [digits]

    new_terrain = []
    for IR in range(len(terrain)*5):
        new_terrain += [[None] * len(terrain[0])*5]
        for IC in range(len(terrain[0])*5):
            v = terrain[IR % len(terrain)][IC % len(
                terrain[0])] + IR // len(terrain) + IC // len(terrain[0])

            new_terrain[IR][IC] = wrappp(v)

    # for step in range(5):
    #     for IR, r in terrain:
    #         new_row = r * 5
    #         for i in range(len(new_row)):
    #             new_row[i] =terrain[IR,]

    #         new_terrain += [new_row]
    #         # print(new_row)
    #         # break

    terrain = new_terrain

    q = PriorityQueue()
    q.put((0, (0, 0)))

    incs = [(+1, 0), (-1, 0), (0, +1), (0, -1)]

    visited = {}
    while q:
        cost, (r, c) = q.get()

        if r == len(terrain) - 1 and c == len(terrain[0])-1:
            print(cost)
            break

        if (r, c) not in visited or visited[(r, c)] > cost:
            visited[(r, c)] = cost

            for inc in incs:
                RR, CC = r + inc[0], c + inc[1]

                if RR >= 0 and RR < len(terrain):
                    if CC >= 0 and CC < len(terrain[RR]):
                        q.put((terrain[RR][CC] + cost, (RR, CC)))

    print('end')
    # return visited[(len(terrain)-1, len(terrain[0]) - 1)]


print(main())
