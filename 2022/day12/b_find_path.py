#! env python

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

    for start in [start]:
        print(find_path(maze, start, end))


def find_path(maze:dict, start, end):
    visited, q = {}, [(0, start)]

    while q:
        depth, current = heappop(q)
        if current == end:
            return depth

        if current in visited and visited[current] <= depth:
            continue

        visited[current] = depth

        r, c = current
        children = [(r+1,c),(r-1,c),(r,c+1),(r,c-1)]
        for child in children:
            if is_valid_move(maze, current, child):
                heappush(q, (depth + 1, child))

def is_valid_move(maze, current, child):
    return child in maze and maze[child] - maze[current] < 2

if __name__ == "__main__":
    main()