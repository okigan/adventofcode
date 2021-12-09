#! /usr/bin/env python

print('hello')

import os
import sys
import re

from functools import * 
from collections import *

def decode(to_decode:list, decoded:list,  find : set, replace: set):
    find = find.copy()
    replace = replace.copy()
    replace = replace.pop()

    for f in find:
        if set(list(f)).issubset(set(to_decode)):
            for c in f:
                to_decode.remove(c)
            
            for c in replace:
                decoded += [c]


def replace_chars(s:str, f : set, replace: set):
    f = f.copy()
    replace = replace.copy()
    f = f.pop()
    replace = replace.pop()

    if set(list(f)).issubset(set(list(s))):
        s_as_set = list(s)
        for c in f:
            s = s.replace(c, '')
        s += replace
        return s
    return s

def main():
    standard_display = {}
    standard_display[0] = ("abcefg" )#len 6
    standard_display[1] = ("cf"     )#len 2
    standard_display[2] = ("acdeg"  )#len 5
    standard_display[3] = ("acdfg"  )#len 5
    standard_display[4] = ("bcdf"   )#len 4
    standard_display[5] = ("abdfg"  )#len 5
    standard_display[6] = ("abdefg" )#len 6
    standard_display[7] = ("acf"    )#len 3
    standard_display[8] = ("abcdefg")#len 7
    standard_display[9] = ("abcdfg" )#len 6

    standard_display_len_to_char = defaultdict(list)
    for v, segment in standard_display.items():
        standard_display_len_to_char[len(segment)] += [segment]

    standard_display_len_to_value = { v: k for k,v in standard_display.items()}

    segments_lines = []
    with open('./input.txt', 'rt') as f:
        while True:
            line = f.readline().strip()
            if len(line) == 0:
                break
            segments = re.split(' |\|', line)
            segments = list(filter(lambda x: len(x) > 0, segments))
            segments_lines += [segments]

    for segments_line in segments_lines:
        len_to_display_map = defaultdict(set)
        for segment in segments_line:
            len_to_display_map[len(segment)].add(segment)
        len_to_display_map = {k: list(v) for k,v in len_to_display_map.items()}

        learned  = {}
        for std_len, std_list in standard_display_len_to_char.items():
            if len(std_list) == 1:
                for i in len_to_display_map[std_len]:
                    learned[i] = std_list[0]

        for segment in segments_line:
            if len(segment) == 3:
                print(segment)
            to_decode = list(segment)
            decoded = []

            if len(to_decode) == 0:
                learned[segment] = ''.join(decoded)


print(main())   