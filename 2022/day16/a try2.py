#! env python

from itertools import *
from functools import *
from collections import *

import os
import re

dir_path = os.path.dirname(os.path.realpath(__file__))

def main():

    graph = defaultdict(list)
    rates = defaultdict(lambda: 0)
    costs = {}

    starts = []
    with open(dir_path + "/input.txt") as f:
        for line in f.readlines():
            m = re.match(f"Valve (..) has flow rate=(\d+); tunnels* leads* to valves*(.*)", line)
            items = list(m.groups())
            flow = int(items[1])
            starts += [items[0]]
            graph[items[0]] = items[2].strip().split(", ")
            open_valve_node = items[0]+"open"
            rates[open_valve_node] = flow
            graph[items[0]] += [open_valve_node]
            graph[open_valve_node] += items[2].strip().split(", ")
            print(line)

    graph['start'] = starts
    max_rate = find_path(graph, 'start', 30, rates)

    print(max_rate)

def calc_total_rate(open_state, rates, current_depth):
    total = 0
    for k, v in open_state.items():
        rate = rates[k]
        total += rate * (current_depth - v)

    return total


def find_path(graph, start, max_depth, rates):
    paths = []

    while paths:
        

    max_total_rate = 0

    visited, q = {}, deque([(0, {}, start)])

    while q:
        depth, open_state, current = q.popleft()

        max_total_rate = max(calc_total_rate(open_state, rates, depth), max_total_rate)

        if depth >= max_depth:
            continue

        if current in visited and visited[current] <= depth:
            continue

        visited[current] = depth

        for child in graph[current]:
            if child in visited and visited[child] <= depth:
                continue
            
            current_open_state = open_state
            if child in child and rates[child] > 0:
                current_open_state = open_state.copy()
                current_open_state[child] = depth
            q += [(depth + 1, current_open_state, child)]

    
    return max_total_rate

if __name__ == "__main__":
    main()