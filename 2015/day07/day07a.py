#! env python

from itertools import *
from functools import *
from collections import *

import os
import re

dir_path = os.path.dirname(os.path.realpath(__file__))

def to_int_if_possible(x):
    try:
        return int(x)
    except ValueError:
        return x

def is_number(n):
    if isinstance(n, int):
        return True
    if isinstance(n, float):
        return True

def main():
    d = {}

    with open(dir_path + "/input.txt") as f:
        for line in f.readlines():
            line = line.strip()
            m = re.match("(.+) (.+) (.+) -> (.+)", line)
            if m is not None:
                d[m[4]] = (m[2], m[1], m[3])
                continue
            
            m = re.match("(.+) (.+) -> (.+)", line)
            if m is not None:
                d[m[3]] = (m[1], m[2], m[3])
                continue

            m = re.match("(.+) -> (.+)", line)
            if m is not None:
                d[m[2]] = ("ASSIGN", m[1])
                continue

            print("unknown line", line)

    cache = {}
    def eval(x):
        if x in cache:
            return cache[x]

        if x not in d:
            cache[x] = to_int_if_possible(x)
            return cache[x]

        z = d[x]

        if z[0] == "ASSIGN":
            cache[x] = eval(z[1])
            return cache[x]

        if z[0] == "OR":
            cache[x] = eval(z[1]) | eval(z[2])
            return cache[x]

        if z[0] == "AND":
            cache[x] = eval(z[1]) & eval(z[2])
            return cache[x]

        if z[0] == "LSHIFT":
            cache[x] =  eval(z[1]) << eval(z[2])
            return cache[x]

        if z[0] == "RSHIFT":
            cache[x] =  eval(z[1]) >> eval(z[2])
            return cache[x]

        if z[0] == "NOT":
            cache[x] = ~eval(z[1])
            return cache[x]

        print("should not be here", z)

    result = eval('a')

    print(result)

if __name__ == "__main__":
    main()