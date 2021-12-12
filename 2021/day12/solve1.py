#! /usr/bin/env python

print('hello')

import os
import sys
import re

from functools import * 
from collections import *

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

    for s,e in edges:
        adj[s] += [e]
        adj[e] += [s]

    q = deque([('start', ['start'])])

    paths = []
    while q:
        node, path = q.popleft()

        if node == 'end':
            paths += [path]
        else:
            check_path = list(filter(lambda x: x.islower() and x != 'end', path))
            for n in adj[node]:
                if n not in check_path:
                    q.append((n, path + [n]))


    for p in paths:
        print(p)
    return len(paths)

print(main())   