#! env python

from itertools import *
from functools import *
from collections import *

import os 
import re

dir_path = os.path.dirname(os.path.realpath(__file__))

def main():

    d = defaultdict(deque)
    commands = []
    with open(dir_path + "/input.txt") as f:
        lines = deque(f.readlines())
        while lines:
            line = lines.popleft()
            m = re.findall(r"(?:.( |[A-Z]).)\s{0,1}", line, re.MULTILINE)
            
            if len(m) != 9:
                break
            for i, c in enumerate(m):
                if c == ' ':
                    continue
                d[i + 1].append(c)

        lines.popleft()

        while lines:
            line = lines.popleft()
            m = re.findall(r"(.+) (\d+) from (\d+) to (\d+)", line, re.MULTILINE)
            commands += [[m[0][0], int(m[0][1]), int(m[0][2]), int(m[0][3])]]

    for c in commands:
        taken = []
        for n in range(c[1]):
            taken += [d[c[2]].popleft()]

        for x in reversed(taken):
            d[c[3]].appendleft(x)

    print("".join(d[i][0] for i in sorted(d.keys())))
        

if __name__ == "__main__":
    main()