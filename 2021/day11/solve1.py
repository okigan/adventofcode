#! /usr/bin/env python

print('hello')

import os
import sys
import re

from functools import * 
from collections import *

def main():
    m = []
    with open('./input.txt', 'rt') as f:
        while True:
            line = f.readline().strip()
            if len(line) == 0:
                break
            digits = re.split('', line)
            digits = filter(lambda x: len(x)>0, digits)
            numbers = [int(d) for d in digits]
            m += [numbers]

    incs = [
        (1, 0), (-1, 0), (0 , 1), ( 0,-1),
        (1, 1), (-1, 1), (-1,-1), (+1,-1)]

    flash_count = 0
    for step in range(1, 100 + 1):
        for ir, r in enumerate(m):
            for ic, c in enumerate(r):
                m[ir][ic] += 1

        flashed = set()
        had_flashed = True
        while had_flashed:
            had_flashed = False
            for ir, _ in enumerate(m):
                for ic, _ in enumerate(m[0]):
                    if m[ir][ic] > 9 and (ir, ic) not in flashed:
                        flash_count += 1
                        flashed.add((ir, ic))
                        had_flashed = True

                        for incR, incC in incs:
                            posR, posC = ir + incR, ic + incC
                            if posR >= 0 and posR < len(m):
                                if posC >= 0 and posC < len(m[0]):
                                    m[posR][posC] += 1


        while flashed:
            RR, CC = flashed.pop()
            m[RR][CC] = 0


    return flash_count




    return None

print(main())   