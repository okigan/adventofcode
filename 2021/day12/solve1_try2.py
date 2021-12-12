#! /usr/bin/env python

from collections import defaultdict, deque
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
        adj[e] += [s]

    paths = []
    candidates = deque([(['start'], set(['start']))])
    while candidates:
        candidate, ss = candidates.popleft()
        head = candidate[-1]

        if head == 'end':
            paths += [candidate]
        else:
            for nnn in adj[head]:
                if nnn not in candidate or nnn.isupper():
                    candidates += [(candidate + [nnn], ss | {nnn})]

    return len(paths)


print(main())
