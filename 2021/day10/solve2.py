#! /usr/bin/env python

print('hello')

import os
import sys
import re

from functools import * 
from collections import *

chars = {")" : "(", "]" : "[", "}" : "{", ">": "<"} 
ichars = {"(" : ")", "[" : "]", "{" : "}", "<": ">"} 

def find_corrupt_char(line):

    s = []
    for c in line:
        if c in chars.values():
            s += c
        elif c in chars.keys():
            if s[-1] != chars[c]:
                return c, len(s)
            else:
                s.pop()
    return None, s


def main():
    lines = []
    with open('./input.txt', 'rt') as f:
        while True:
            line = f.readline().strip()
            if len(line) == 0:
                break
            lines += [line]


    corrupt_chars  = []
    incomplete_lines = []
    for line in lines:
        corrupt_char, stack  = find_corrupt_char(line)
        if corrupt_char is not None:
            corrupt_chars += [corrupt_char]
        else:
            if len(stack) > 0:
                incomplete_lines += [(line, stack)]

    completers = []
    for (c, stack) in incomplete_lines:
        completer = []
        for cc in stack[::-1]:
            completer += ichars[cc]
        completers += [completer]

        


    point_map = {')': 1, ']': 2, '}': 3, '>': 4}
    points  = []
    for cc in completers:
        curr_points = 0
        for c in cc:
            curr_points = curr_points * 5 + point_map[c]
        points += [curr_points]

    sss = sorted(points)
    return sss[len(sss) // 2]

print(main())   