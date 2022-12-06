#! env python

from itertools import *
from functools import *
from collections import *

import os 

dir_path = os.path.dirname(os.path.realpath(__file__))

def divide_chunks(l, n):
     
    # looping till length l
    for i in range(0, len(l), n):
        yield l[i:i + n]

def main():

    rucksacks = []
    with open(dir_path + "/input.txt") as f:
        for line in f.readlines():
            line = line.strip()
            half = len(line) // 2
            rucksacks += [line] #[(line[:half], line[half:])]

    sum_of_priority = 0
    for r in divide_chunks(rucksacks, 3):
        a, b, c = set(r[0]), set(r[1]), set(r[2])

        intersection = a.intersection(b)
        intersection = intersection.intersection(c)
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