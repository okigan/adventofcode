#! /usr/bin/env python

from collections import defaultdict, deque
from itertools import product
import re


def main():
    edges = []
    with open('./input.txt', 'rt') as f:
        while True:
            line = f.readline().strip()
            if len(line) == 0:
                break
            edge = re.split('-', line)
            edges += [edge]

    adj = defaultdict(list)

    for s, e in edges:
        adj[s] += [e]
        if s != 'start':
            adj[e] += [s]

    paths = []
    candidates = deque([(['start'], False)])
    while candidates:
        candidate, small_cave_twice = candidates.popleft()
        head = candidate[-1]

        if head == 'end':
            paths += [candidate]
        else:
            for nnn in adj[head]:
                if nnn.isupper():
                    candidates += [(candidate + [nnn], small_cave_twice)]
                else:
                    if small_cave_twice:
                        if candidate.count(nnn) < 1:
                            candidates += [(candidate + [nnn], small_cave_twice)]
                    else:
                        if candidate.count(nnn) < 2:
                            candidates += [(candidate + [nnn], True if candidate.count(nnn) == 1 else False)]

    return len(paths)


print(main())
