#! env python

import itertools
import functools
import os 

dir_path = os.path.dirname(os.path.realpath(__file__))

def main():
    floor = 0

    with open(dir_path + "/input.txt") as f:
        for line in f.readlines():
            for c in line:
                if c == "(":
                    floor += 1
                elif c == ")":
                    floor -= 1
    print(floor)

if __name__ == "__main__":
    main()