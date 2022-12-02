#! env python

import itertools
import functools
import os 

dir_path = os.path.dirname(os.path.realpath(__file__))

def main():
    floor = 0
    first_basement = 0

    with open(dir_path + "/input.txt") as f:
        for line in f.readlines():
            for index, c in enumerate(line):
                if c == "(":
                    floor += 1
                elif c == ")":
                    floor -= 1
                if floor < 0:
                    first_basement = index + 1
                    break
    print(first_basement)

if __name__ == "__main__":
    main()