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

    digit_letters = {
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


    standard_display_to_set = { k:set(list(v)) for k, v in digit_letters.items()}


    by_len = defaultdict(dict)
    for val, letters in digit_letters.items():
        by_len[len(letters)].update({val:frozenset(list(letters))})

    segments_lines = load()

    for segments_line in segments_lines:
        segment_by_len = defaultdict(set)
        for segment in segments_line:
            segment_by_len[len(segment)].add(frozenset(list(segment)))

        learned = {}
        for letters_len, value_and_letters_set_list in by_len.items():
            if len(value_and_letters_set_list) == 1:
                for (value, letters_set_list) in value_and_letters_set_list.items():
                    learned[value] = segment_by_len[letters_len]

        for i in standard_display_to_set:
            for j in standard_display_to_set:
                for k in standard_display_to_set:
                    if i!= j and j != k and i != k:
                        if standard_display_to_set[i] == standard_display_to_set[j] | standard_display_to_set[k]:
                            if i in learned and k in learned:
                                for segment in segments_line:
                                    if learned[i] == frozenset(list(segment)) | learned[k]:
                                        learned[j] = frozenset(list(segment)) 
 
                        if standard_display_to_set[i] == standard_display_to_set[j] - standard_display_to_set[k]:
                            if j in learned and k in learned:
                                print('')




 

    total_sum = 0





    return total_sum 



print(main())   