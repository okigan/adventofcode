from itertools import *
from functools import *
from collections import *

import os 

dir_path = os.path.dirname(os.path.realpath(__file__))

def manhattan_distance(ax, ay, bx, by):
    return abs(ax - bx) + abs(ay - by)

def adjust(hx, hy, tx, ty):
    dx, dy = 0, 0
    if hx == tx and abs(hy - ty) == 2:
        dy = (hy - ty)
    elif hy == ty and abs(hx - tx) == 2:
        dx = (hx - tx)
    elif abs(hy - ty) + abs(hx - tx) > 2:
        dy = (hy - ty)
        dx = (hx - tx)

    return tx + dx/max(1, abs(dx)), ty + dy/max(1, abs(dy))

def main():
    moves = []
    with open(dir_path + "/input.txt") as f:
        for line in f.readlines():
            line = line.strip()
            d, count = line.split()
            count = int(count)
            moves += [(d, count)]

    tx, ty = 0, 0
    hx, hy = 0, 0

    tpositions = set()
    tpositions.add((tx,ty))
    hpositions = set()
    hpositions.add((hx,hy))

    for move in moves:
        d, count = move
        print("== ", d, " ", count, " ==")
        ix, iy = 0, 0
        if d == 'U':
            ix, iy = 0, 1
        elif d == 'D':
            ix, iy = 0, -1
        elif d == 'L':
            ix, iy = -1, 0
        elif d == 'R':
            ix, iy = 1, 0
        else:
            print("should not be here")

        for _ in range(count):
            hx, hy = hx + ix, hy + iy
            tx, ty = adjust(hx, hy, tx, ty)
            hpositions.add((hx, hy))
            tpositions.add((tx, ty))
            print_state(hx, hy, tx, ty, hpositions, tpositions)
            print("")


    print(len(tpositions))

def print_state(hx, hy, tx, ty, hpositions, tpositions):
    field = []
    for r in range(5):
        row = ['.'] * 6
        for c in range(6):
            # if (c, r) in tpositions:
            #     row[c] = '#'
            if (c, r) == (tx, ty):
                row[c] = 'T'
            if (c, r) == (hx, hy):
                row[c] = 'H'

        field.append(''.join(row))
    
    for r in reversed(field):
        print(r)

if __name__ == "__main__":
    ax, ay = adjust(1, 2, 0, 0)
    main()