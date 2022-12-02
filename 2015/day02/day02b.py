#! env python

import itertools
import functools
import os 

dir_path = os.path.dirname(os.path.realpath(__file__))

def main():
    needed = 0
    with open(dir_path + "/input.txt") as f:
        for line in f.readlines():
            l,w,h = line.split('x')
            l,w,h = int(l), int(w), int(h)
            smallest_perimiter = 2 * min(l+w, l+h, w+h)
            bow = l*w*h
            needed += smallest_perimiter + bow

    print(needed)

if __name__ == "__main__":
    main()