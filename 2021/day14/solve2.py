#! /usr/bin/env python

import enum
from itertools import *
from functools import *
from collections import *
import re
import sys
import os
print('hello')


def main():
    polymer = ''
    rules = {}
    with open('./input.txt', 'rt') as f:
        while True:
            line = f.readline().strip()
            if len(line) == 0:
                break
            polymer = line

        while True:
            line = f.readline().strip()
            if len(line) == 0:
                break
            rule = re.split(' -> ', line)
            rules[rule[0]] = rule[1]

    pairs = defaultdict(int)
    for i in range(len(polymer) - 1):
        pairs[polymer[i:i+2]] += 1

    subtract = defaultdict(int)

    for ic, c in enumerate(polymer):
        if ic == 0 or ic == len(polymer) -1:
            continue
        subtract[c] += 1

    for step in range(40):
        new_pairs = defaultdict(int)
        
        for k, v in list(pairs.items()):
            insert = rules[k]

            new_pairs[k[0] + insert] += v
            new_pairs[insert + k[1]] += v
            subtract[insert] += v
            del pairs[k]
        if len(pairs)>0:
            print("residiual")
        pairs = new_pairs

    hist = defaultdict(int)
    for k, v in pairs.items():
        hist[k[0]] += v
        hist[k[1]] += v

    for k in subtract:
        hist[k] -= subtract[k]

    print(max(hist.values()) - min(hist.values()))


print(main())

                   # NNCB

# NNCB         NN     NC      CB
# NCNBCHB     NC CN  NC BC   CH HB