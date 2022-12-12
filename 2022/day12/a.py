#! env python

from itertools import *
from functools import *
from collections import *

import os 

dir_path = os.path.dirname(os.path.realpath(__file__))

def main():
    aaa = []

    start = None
    end = None
    maze = {}
    with open(dir_path + "/input.txt") as f:
        count = 0
        for line in f.readlines():
            line = line.strip()
            for idx, c in enumerate(line):
                maze[(count, idx)] = c
                if c == 'S':
                    start = (count, idx)
                    maze[(count, idx)] = 'a'
                elif c == 'E':
                    end = (count, idx)
                    maze[(count, idx)] = 'z'


            count += 1

    # print(maze)


    q = deque([(start, 0)])
    visited = {}
    def dfs():
        while q:
            current, depth = q.pop()
            if current == end:
                print("found", current, depth)

            if current not in visited or visited[current] > depth:
                visited[current] = depth

                r, c = current
                for child in [(r + 1, c + 0), (r - 1, c + 0), (r + 0, c + 1), (r + 0, c - 1)]:
                    if child in maze:
                        if ord(maze[child]) - ord(maze[current]) < 2:
                            q.append((child, depth + 1))


    dfs()

    print(min(possible))


if __name__ == "__main__":
    main()