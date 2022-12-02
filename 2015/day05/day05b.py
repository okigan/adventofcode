#! env python

from itertools import *
from functools import *
from collections import *

import os 

dir_path = os.path.dirname(os.path.realpath(__file__))

def has_pair_twice_without_overlap(s):
    i = 1
    while i < len(s):
        xy = s[i-1] + s[i]
        if xy in s[i+1:]:
            return True
        i += 1
    return False

def has_repeating_letter_with_one_skip(string):
    for i in range(len(string) - 2):
        if string[i] == string[i+2]:
            return True

    return False

def main():
    strings = []
    with open(dir_path + "/input.txt") as f:
        for line in f.readlines():
            line = line.strip()
            strings += [line]

    print(len(strings))

    good_strings_counter = 0

    for string in strings:
        if not has_pair_twice_without_overlap(string):
            continue
        if not has_repeating_letter_with_one_skip(string):
            continue
        
        good_strings_counter += 1

    print(good_strings_counter)

if __name__ == "__main__":
    main()