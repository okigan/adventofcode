#! env python

from itertools import *
from functools import *
from collections import *

import os 

dir_path = os.path.dirname(os.path.realpath(__file__))

def has_3_vowels(string):
    vowels_counter = 0
    for character in string:
        if character in 'aeiou':
            vowels_counter += 1

    if vowels_counter >= 3:
        return True
    
    return False

def has_letter_appearing_twice_together(string):

    for i in range(len(string) - 1):
        if string[i] == string[i + 1]:
            return True
    
    return False

def has_forbeeden_substring(string):
    bad_strings = ['ab', 'cd', 'pq', 'xy']

    for bad_string in bad_strings:
        if string.find(bad_string) != -1:
            return True

    return False

def main():
    strings = []
    with open(dir_path + "/input.txt") as f:
        for line in f.readlines():
            line = line.strip()
            strings += [line]

    good_strings_counter = 0

    for string in strings:
        if not has_3_vowels(string):
            continue
        if not has_letter_appearing_twice_together(string):
            continue
        if has_forbeeden_substring(string):
            continue
        
        good_strings_counter += 1

    print(good_strings_counter)

if __name__ == "__main__":
    main()