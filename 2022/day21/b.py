#! env python

from itertools import *
from functools import *
from collections import *

import os 

dir_path = os.path.dirname(os.path.realpath(__file__))

def main():

    monkeys = {}
    with open(dir_path + "/input.txt") as f:
        for line in f.readlines():
            line = line.strip()
            a, b = line.split(": ")
            bparts = b.split(" ")
            pass
            if len(bparts) == 3:
                monkeys[a] = [bparts[1], bparts[0], bparts[2]]
            else:
                monkeys[a] = bparts

            if a == 'root':
                monkeys[a] = ['-', bparts[0], bparts[2]]

    # print(monkeys)

    def eval_monkey(node, humn_override):

        if node == 'humn':
            return humn_override

        vals = monkeys[node]
        if len(vals) == 3:
            if vals[0] == "+":
                return eval_monkey(vals[1], humn_override) + eval_monkey(vals[2], humn_override)
            if vals[0] == "-":
                return eval_monkey(vals[1], humn_override) - eval_monkey(vals[2], humn_override)
            if vals[0] == "*":
                return eval_monkey(vals[1], humn_override) * eval_monkey(vals[2], humn_override)
            if vals[0] == "/":
                return eval_monkey(vals[1], humn_override) / eval_monkey(vals[2], humn_override)
        else:
            try:
                return int(vals[0])
            except:
                return eval_monkey(vals[0], humn_override)

        return None

    # hi, lo = float('100000000000000000000000000000000'), float('-100000000000000000000000000000000')

    # while lo + 1 < hi:
    #     mid = (hi + lo) / 2
    #     result = eval_monkey('root', mid)
    #     if result < 0:
    #         hi = mid
    #     else:
    #         lo = mid
        
    # print(lo, hi)

    print(eval_monkey('root', 3330805295850))

if __name__ == "__main__":
    main()