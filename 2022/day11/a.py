#! env python

from itertools import *
from functools import *
from collections import *

import os 
import re

dir_path = os.path.dirname(os.path.realpath(__file__))

def main():
    monkeys = []
    idx = -1
    items = []
    operation = ""
    div = -1
    target1 = None
    target2 = None
    with open(dir_path + "/input.txt") as f:
        for line in f.readlines():
            line = line.strip()
            if line == "":
                monkeys += [[items, operation, div, target1, target2]]
            elif line.startswith("Monkey "):
                pass
            elif line.startswith("Starting items: "):
                items = list(map(lambda x: int(x), line[len("Starting items: "):].split(", ")))
            elif line.startswith("Operation: new = "):
                operation = line[len("Operation: new = "):]
            elif line.startswith("Test: divisible by "):
                div = line[len("Test: divisible by "):]
                div = int(div)
            elif line.startswith("If true: throw to monkey "):
                target1 = line[len("If true: throw to monkey "):]
                target1 = int(target1)
            elif line.startswith("If false: throw to monkey "):
                target2 = line[len("If false: throw to monkey "):]
                target2 = int(target2)
        monkeys += [[items, operation, div, target1, target2]]


    counter = defaultdict(int)
    for iteration in range(20):
        for idx_monkey, m in enumerate(monkeys):
            for idx, item in enumerate(m[0]):
                counter[idx_monkey] += 1
                # print(m[1])
                if type(item) != type(10):
                    pass
                new = eval(m[1], {"old": item})
                new_var = new // 3
                if new_var % m[2] == 0: 
                    monkeys[m[3]][0].append(new_var)
                else:
                    monkeys[m[4]][0].append(new_var)
            
            m[0] = []


            

    print(monkeys)
    print(counter)
    new_var1 = sorted(counter.values())
    print(new_var1[-1]*new_var1[-2])

if __name__ == "__main__":
    main()