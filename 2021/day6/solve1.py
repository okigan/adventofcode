#! /usr/bin/env python

print('hello')

import os
import sys
import re
import math


def main():
    fishes = []
    with open('./input1.txt') as f:
        while True:
            line = f.readline()
            if len(line) == 0:
                break;
            split = re.split(',', line)
            fishes = list(map(int, split))

    days = 80
    for d in range(days):
        new_fishes = []
        for ifish, fish in enumerate(fishes):
            if fish == 0:
                fishes[ifish] = 6
                new_fishes += [8]
            else:
                fishes[ifish] -= 1

        fishes += new_fishes

    return len(fishes)



 


print(main())