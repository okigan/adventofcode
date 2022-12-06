#! env python

from itertools import *
from functools import *
from collections import *

import os 

dir_path = os.path.dirname(os.path.realpath(__file__))

def main():

    rucksacks = []
    with open(dir_path + "/input.txt") as f:
        for line in f.readlines():
            line = line.strip()
            half = len(line) // 2
            rucksacks += [(line[:half], line[half:])]

    sum_of_priority = 0
    for r in rucksacks:
        a, b = set(r[0]), set(r[1])

        intersection = a.intersection(b)
        letter = list(intersection)[0]
        priority = 0
        if ord('a') <= ord(letter) and ord(letter) <=ord('z'):
            priority = ord(letter) - ord('a') + 1
        if ord('A') <= ord(letter) and ord(letter) <=ord('Z'):
            priority = ord(letter) - ord('A') + 27

        sum_of_priority += priority

    print(sum_of_priority)

if __name__ == "__main__":
    main()