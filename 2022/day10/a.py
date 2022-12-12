#! env python

from itertools import *
from functools import *
from collections import *

import os 

dir_path = os.path.dirname(os.path.realpath(__file__))

def main():
    commands = []
    with open(dir_path + "/input.txt") as f:
        for line in f.readlines():
            line = line.strip()
            parts = line.split()
            for idx, p in enumerate(parts):
                if idx > 0:
                    parts[idx] = int(parts[idx])

            commands += [parts]

    cq = deque(commands)
    cycle = 0
    steps = 1;
    X = 0
    add = 1

    total = 0
    while steps > 0:
        cycle += 1
        steps -= 1

        if steps == 0:
            X += add

            if cq:
                command = cq.popleft()
                if command[0] == 'noop':
                    steps = 1
                    add = 0
                elif command[0] == 'addx':
                    steps = 2
                    add = command[1]

        if cycle in [20, 60, 100, 140, 180,  220]:
            total += cycle * X



    print(X)
    print(total)

if __name__ == "__main__":
    main()