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
            

    print(monkeys)

    def eval_monkey(node):
        vals = monkeys[node]
        if len(vals) == 3:
            if vals[0] == "+":
                return eval_monkey(vals[1]) + eval_monkey(vals[2])
            if vals[0] == "-":
                return eval_monkey(vals[1]) - eval_monkey(vals[2])
            if vals[0] == "*":
                return eval_monkey(vals[1]) * eval_monkey(vals[2])
            if vals[0] == "/":
                return eval_monkey(vals[1]) / eval_monkey(vals[2])
        else:
            try:
                return int(vals[0])
            except:
                return eval_monkey(vals[0])

        return None

    print(eval_monkey('root'))

if __name__ == "__main__":
    main()