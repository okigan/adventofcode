#! env python

from itertools import *
from functools import *
from collections import *

import os 
import re
dir_path = os.path.dirname(os.path.realpath(__file__))

def main():
    assignments = []
    with open(dir_path + "/input.txt") as f:
        for line in f.readlines():
            # line = line.strip()
            x = re.match("(.+)-(.+),(.+)-(.+)", line)
            assignments += [((int(x[1]), int(x[2])), (int(x[3]), int(x[4])))]

    count = 0
    for a,b in assignments:
        set_a = set(range(a[0], a[1]+1))
        set_b = set(range(b[0], b[1]+1))
        if set_a.issubset(set_b) or set_b.issubset(set_a):
            count += 1

    print(count)

if __name__ == "__main__":
    main()