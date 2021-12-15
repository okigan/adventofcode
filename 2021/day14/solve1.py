#! /usr/bin/env python

print('hello')

import os
import sys
import re

from functools import * 
from collections import *
from itertools import * 

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

    for step in range(40):
        print(step)
        new_polymer = ''

        for i in range(len(polymer) - 1):
            l = polymer[i:i+2] 
            new_polymer += l[0] + rules[l]

        polymer = new_polymer + polymer[-1]


    hist = Counter(list(polymer))

    sorted_hist = sorted(hist.values())


    print(sorted_hist[-1] - sorted_hist[0])


 

print(main())   