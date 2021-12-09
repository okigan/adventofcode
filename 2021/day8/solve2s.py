#! /usr/bin/env python

print('hello')

import os
import sys
import re

from functools import * 
from collections import *
from itertools import *

def load():
    segments_lines = []
    with open('./input.txt', 'rt') as f:
        while True:
            line = f.readline().strip()
            if len(line) == 0:
                break
            segments = re.split(' |\|', line)
            segments = list(filter(lambda x: len(x) > 0, segments))
            segments_lines += [segments]
    return segments_lines


def main():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g']

    standard_display = {
    0 : "abcefg" , #len 6
    1 : "cf"     , #len 2
    2 : "acdeg"  , #len 5
    3 : "acdfg"  , #len 5
    4 : "bcdf"   , #len 4
    5 : "abdfg"  , #len 5
    6 : "abdefg" , #len 6
    7 : "acf"    , #len 3
    8 : "abcdefg", #len 7
    9 : "abcdfg" } #len 6


    standard_display_to_set = { k:set(list(v)) for k, v in standard_display.items()}

        
    standard_display_lookup = {frozenset(list(v)):k for k,v in standard_display.items()}
    standard_display_by_len = defaultdict(list)
    for x in standard_display.values():
        standard_display_by_len[len(x)].append(''.join(sorted(list(x))))

    for i in range(len(standard_display_to_set)):
        for j in range(len(standard_display_to_set)):
            for k in range(len(standard_display_to_set)):
                if i!= j and j != k and i != k:
                    if standard_display_to_set[i] == standard_display_to_set[j] | standard_display_to_set[k]:
                        pass

    segments_lines = load()

    total_sum = 0

    for segments_line in segments_lines:
        len_hist = defaultdict(list)
        for segment in segments_line:
            len_hist[len(segment)] += [segment]
        learned = {}
        # standard_display_to_set = { k:set(list(v)) for k, v in standard_display.items()}

        for std_len, std_values in standard_display_by_len.items():
            if len(std_values) == 1:
                key = frozenset(list(std_values[0]))
                std_value_x = standard_display_lookup[key]
                learned[std_values[0]] = frozenset(list(len_hist[std_len][0]))

        learned_numbers = {}
        for segment in segments_line:
            if segment in learned:
                learned_numbers[standard_display_lookup[frozenset(list(learned[segment]))]] = segment

        # learn 6
        for segment in segments_line:
            if set(list(segment)).union(set(list(learned_numbers[1]))) == set(list(learned_numbers[8])):
                learned_numbers[6] = segment

        # learn 0
        for segment in segments_line:
            if set(list(segment)).union(set(list(learned_numbers[4]))) == set(list(learned_numbers[8])):
                learned_numbers[0] = segment

        r = set(list(learned_numbers[7])) - set(list(learned_numbers[1])) 
        print(learned)




    return total_sum 



print(main())   