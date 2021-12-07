#! /usr/bin/env python

print('hello')

from collections import defaultdict
import os
import sys
import re
import math
from functools import *
from typing import Counter 


def main():
    fishes = []
    with open('./input1.txt') as f:
        while True:
            line = f.readline()
            if len(line) == 0:
                break;
            split = re.split(',', line)
            fishes = list(map(int, split))

    fishes_hist = Counter(fishes)
    days = 256
    for d in range(days):
        new_fish_hist = defaultdict(int)
        for fish_age, fish_count in fishes_hist.items():
            if fish_age == 0:
                new_fish_hist[6] += fish_count
                new_fish_hist[8] += fish_count
            else:
                new_fish_hist[fish_age - 1] += fish_count

        fishes_hist = new_fish_hist

    return sum(fishes_hist.values())



 


print(main())