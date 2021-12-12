#! /usr/bin/env python

from functools import *
from collections import *
import re
import sys
import os
print('hello')


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
        adj[e] += [s]

    q = deque([('start', ['start'])])

    paths = []
    while q:
        node, path = q.popleft()

        if node == 'end':
            paths += [path]
        else:
            for n in adj[node]:
                if check_path(path + [n]):
                    q.append((n, path + [n]))

    # for p in paths:
    #     print(p)
    return len(paths)


def check_path(path):
    hist = Counter(path)
    if hist['start'] > 1:
        return False

    vals = [v for k, v in hist.items() if k.islower()]
    vals = sorted(vals, reverse=True)
    if (len(vals) >= 2 and vals[0] <= 2 and vals[1] <= 1) or (len(vals) < 2 and vals[0] <= 2):
        return True
    return False


print(main())
