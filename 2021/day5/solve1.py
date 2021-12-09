#! /usr/bin/env python

print('hello')

import os
import sys
import re
import math


def main():
    lines = []
    with open('./input1.txt') as f:
        while True:
            line = f.readline()
            if len(line) == 0:
                break;
            split = re.split(',|->| ', line)
            sub = split[0:2] + split[4:6]
            coords = list(map(int, sub))
            lines += [coords]

    minx, miny, maxx, maxy = float('inf'), float('inf'), -float('inf'), -float('inf')
    # find min max of coords to get range
    for x0, y0, x1, y1 in lines:
        minx = min(minx, x0, x1)
        miny = min(miny, y0, y1)
        maxx = max(maxx, x0, x1)
        maxy = max(maxy, y0, y1)

    m = [None] * (maxy + 1)
    for r in range(len(m)):
        m[r] = [0] * (maxx + 1)

    for c0, r0, c1, r1 in lines:
        if r0 == r1:
            c, sign = c0,  c1 - c0
            while c != c1 + math.copysign(1, sign):
                m[r0][c] += 1
                c += int(math.copysign(1, sign))
        if c0 == c1:
            r, sign = r0, r1 - r0
            while r != r1 + math.copysign(1, sign):
                m[r][c0] += 1
                r += int(math.copysign(1, sign))

    count_overlaps = 0
    for r in range(len(m)):
        for c in range(len(m[r])):
            if m[r][c] >= 2:
                count_overlaps += 1

    print(m)
    print(count_overlaps)


    # rasterize lines
    # count overlap
 


print(main())