#! /usr/bin/env python

print('hello')

import os
import sys
import re

from functools import * 
from collections import *

def find_corrupt_char(line):
    chars = {")" : "(", "]" : "[", "}" : "{", ">": "<"} 

    s = []
    for c in line:
        if c in chars.values():
            s += c
        elif c in chars.keys():
            if s[-1] != chars[c]:
                return c
            else:
                s.pop()
    return None


def main():
    lines = []
    with open('./input.txt', 'rt') as f:
        while True:
            line = f.readline().strip()
            if len(line) == 0:
                break
            lines += [line]

    corrupt_chars  = []
    for line in lines:
        corrupt_char = find_corrupt_char(line)
        if corrupt_char is not None:
            corrupt_chars += [corrupt_char]

    point_map = {')': 3, ']': 57, '}': 1197, '>': 25137}
    points  = 0
    for cc in corrupt_chars:
        points += point_map[cc]

    return points

print(main())   