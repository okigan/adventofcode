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
            parts = line.strip().split()
            for idx, p in enumerate(parts):
                if idx > 0:
                    parts[idx] = int(parts[idx])

            commands += [parts]

    instructions = []
    for command in commands:
        if command[0] == "noop":
            instructions += [0]
        elif command[0] == "addx":
            instructions += [0]
            instructions += [command[1]]

    X = 1
    total = 0
    screen = ''
    for idx, i in enumerate(instructions):
        cycle = idx + 1
        if cycle in [20, 60, 100, 140, 180,  220]:
            total += cycle * X
        print(f'cycle {cycle}  X {X}')
        screen += '\u2588' if abs((cycle-1)%40 - X) <=1 else ' '
        X += i

    print(total)
    for i in range(0, 240, 40):
        print(screen[i:i+40])

if __name__ == "__main__":
    main()