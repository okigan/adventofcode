#! env python

from itertools import *
from functools import *
from collections import *

import os 

dir_path = os.path.dirname(os.path.realpath(__file__))

def main():

    data = ""
    with open(dir_path + "/input.txt") as f:
        for line in f.readlines():
            line = line.strip()
            data = line
            print(line)

    d = deque()
    for idx,c in enumerate(data):
        d.append(c)

        if len(d) > 14:
            d.popleft()

        if len(set(d)) == 14:
            print(idx + 1)
            break


if __name__ == "__main__":
    main()