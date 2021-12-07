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

    # rasterize lines
    for c0, r0, c1, r1 in lines:
        c, c_sign = c0,  c1 - c0
        r, r_sign = r0,  r1 - r0
        while True:
            flag1, flag2 = False, False
            m[r][c] += 1
            if c0 != c1 and math.copysign(1, c_sign)*(c1 - c) > 0:
                c += int(math.copysign(1, c_sign))
            else:
                flag1 = True
            if r0 != r1 and math.copysign(1, r_sign) * (r1 - r) > 0:
                r += int(math.copysign(1, r_sign))
            else:
                flag2 = True
            if flag1 and flag2:
                break


    # count overlap
    count_overlaps = 0
    for r in range(len(m)):
        for c in range(len(m[r])):
            if m[r][c] >= 2:
                count_overlaps += 1

    print(m)
    return count_overlaps


print(main())