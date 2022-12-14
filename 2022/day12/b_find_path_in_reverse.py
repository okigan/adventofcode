#! env python

from ast import Dict, Tuple
from itertools import *
from functools import *
from collections import *
from heapq import *

import os

dir_path = os.path.dirname(os.path.realpath(__file__))

def main():
    starts = []
    start = None
    end = None
    maze = {}
    with open(dir_path + "/input.txt") as f:
        count = 0
        for line in f.readlines():
            line = line.strip()
            for idx, c in enumerate(line):
                maze[(count, idx)] = ord(c)
                if c == 'S':
                    start = (count, idx)
                    maze[(count, idx)] = ord('a')
                    starts += [((count, idx))]
                elif c == 'E':
                    end = (count, idx)
                    maze[(count, idx)] = ord('z')
                elif c == 'a':
                    starts += [((count, idx))]
            count += 1

    for s in [end]:
        print(find_path(maze, s, set(starts)))

def find_path(maze:Dict, start, ends):
    visited: dict = {}
    q: list  = [(0, [], start)]

    while q:
        depth, prior, current = heappop(q)
        if current in ends:
            return depth

        if current in visited and visited[current] <= depth:
            continue

        visited[current] = depth

        r, c = current
        for child in [(r+1,c),(r-1,c),(r,c+1),(r,c-1)]:
            if child in visited and visited[child] <= depth:
                continue
            if is_valid_move(maze, current, child):
                heappush(q, (depth + 1, prior + [current], child))

def is_valid_move(maze, current, child):
    return child in maze and maze[current] - maze[child] < 2

def distance(a, b):
    # return 0
    return (a[0] - b[0])**2 + abs(a[1] - b[1])**2

if __name__ == "__main__":
    main()