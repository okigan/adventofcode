#! env python

from itertools import *
from functools import *
from collections import *
from heapq import *
import math

import os
import random 

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
                maze[(count, idx)] = ord(c) - ord('a')
                if c == 'S':
                    start = (count, idx)
                    maze[(count, idx)] = ord('a') - ord('a')
                    starts += [((count, idx))]
                elif c == 'E':
                    end = (count, idx)
                    maze[(count, idx)] = ord('z') - ord('a')
                elif c == 'a':
                    starts += [((count, idx))]
            count += 1

    print(find_path(maze, start, end))
    # distances = []
    # for start in starts:
    #     distances += [find_path(maze, start, end)]
    
    # print(min(filter(lambda x: x is not None, distances)))

def find_path(maze:dict, start, end):
    visited, q = {}, deque([(0, start)])

    while q:
        depth, current = q.popleft()
        if current == end:
            return depth

        if current in visited and visited[current] <= depth:
            continue

        visited[current] = depth

        r, c = current
        for child in [(r+1,c),(r-1,c),(r,c+1),(r,c-1)]:
            if child in visited and visited[child] <= depth:
                continue
            if is_valid_move(maze, current, child):
                q += [(depth + 1, child)]

def new_func(visited, depth, current):
    return current in visited and visited[current] <= depth
    
    # print('not found for', start, end)

def is_valid_move(maze, current, child):
    return child in maze and maze[child] - maze[current] <= 1

def distance(a, b):
    # return 0
    return (a[0] - b[0])**2 + abs(a[1] - b[1])**2

if __name__ == "__main__":
    main()