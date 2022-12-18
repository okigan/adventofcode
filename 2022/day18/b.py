#! env python

from itertools import *
from functools import *
from collections import *

import os 

dir_path = os.path.dirname(os.path.realpath(__file__))

def get_bounds(coords):
    m =[+1*float('inf')]*3
    x =[-1*float('inf')]*3

    for coord in coords:
        m[0] = min(m[0], coord[0])
        m[1] = min(m[1], coord[1])
        m[2] = min(m[2], coord[2])

        x[0] = max(x[0], coord[0])        
        x[1] = max(x[1], coord[1])        
        x[2] = max(x[2], coord[2])

    return (m[0] - 2, m[1] - 2, m[2] - 2, ), (x[0] + 2, x[1] + 2, x[2] + 2)        

def floodfill(start, coords, mins, maxs):
    q = [start]
    visited = {}

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


    while q:
        current = q.pop()

        visited[current] = 'a'

        for inc in incs:
            pos = [0, 0, 0]
            for i in range(3):
                pos[i] = current[i] + inc[i]
            
            pos_tuple = tuple(pos)

            oob = False
            for i in range(3):
                if pos[i] < mins[i] or pos[i]> maxs[i]:
                    oob = True
                    break

            if oob:
                continue

            if pos_tuple not in coords:
                if pos_tuple not in visited:
                    q += [pos_tuple]

    return visited.keys()



def main():
    coords = set()

    with open(dir_path + "/input.txt") as f:
        for line in f.readlines():
            line = line.strip()
            coord = tuple(list(map(lambda x: int(x), line.split(","))))
            coords.add(coord)

    print(coords)


    mins, maxs = get_bounds(coords)


    result = floodfill(tuple(mins), coords, mins, maxs)

    print_touching(coords, result)

def print_touching(coords, outer):
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
            
            if tuple(pos) in outer:
                touching += 1

    print(len(coords) * 6)
    print(touching)
    print(len(coords) * 6 - touching)

if __name__ == "__main__":
    main()