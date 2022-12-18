#! env python

from itertools import *
from functools import *
from collections import *

import os 

dir_path = os.path.dirname(os.path.realpath(__file__))

def main():
    coords = set()

    with open(dir_path + "/input.txt") as f:
        for line in f.readlines():
            line = line.strip()
            coord = tuple(list(map(lambda x: int(x), line.split(","))))
            coords.add(coord)

    print(coords)
    incs = [
        (+1, 0, 0), 
        (-1, 0, 0), 
        (+1,+1, 0), 
        (-1,-1, 0), 
    ]

    incs = []
    for z in [-1, 0, +1]:
        for y in [-1, 0, +1]:
            for x in [-1, 0, +1]:
                if x == 0 and y == 0 and z == 0:
                    continue
                if x != 0 and y != 0 and z != 0:
                    continue
                if abs(x) + abs(y) + abs(z) >= 2:
                    continue
                
                incs += [(x, y, z)]

    touching = 0
    for coord in coords:
        for inc in incs:
            pos = [0, 0, 0]
            for i in range(3):
                pos[i] = coord[i] + inc[i]
            
            if tuple(pos) in coords:
                touching += 1

    print(len(coords) * 6)
    print(touching)
    print(len(coords) * 6 - touching)

if __name__ == "__main__":
    main()