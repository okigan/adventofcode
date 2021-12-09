#! /usr/bin/env python

print('hello')

import os
import sys
import re

from functools import * 
from collections import *
from itertools import *


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

    standard_display_lookup = {frozenset(list(v)):k for k,v in standard_display.items()}

    segments_lines = load()

    total_sum = 0

    for segments_line in segments_lines:
        segment_to_index = [(x, i) for i, x in enumerate(segments_line)]
        test_sorted_segments = sorted(segment_to_index, key=lambda x: len(x[0]))

        for ip, p  in enumerate(permutations(letters)):
            # if ip % 1000 == 0:
            #     print(ip)

            lookup = dict(zip(letters, p))
            
            decoded = [None] * len(segments_line)
            for segment, index in test_sorted_segments:
                decoded_segment = ''.join(lookup[c] for c in list(segment))
                if frozenset(list(decoded_segment)) not in standard_display_lookup:
                    break
                decoded[index] = decoded_segment

            if any(x is None for x in decoded):
                continue

            if all(frozenset(list(x)) in standard_display_lookup for x in decoded):
                # print('found')
                this_sum = 0
                for dd in decoded[-4:]:
                    this_sum = 10*this_sum + standard_display_lookup[frozenset(list(dd))]  
                total_sum += this_sum
    return total_sum 

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


print(main())   