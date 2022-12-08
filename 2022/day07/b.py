#! env python

from itertools import *
from functools import *
from collections import *

import os 

dir_path = os.path.dirname(os.path.realpath(__file__))

def main():
    lines = []

    with open(dir_path + "/input.txt") as f:
        for line in f.readlines():
            line = line.strip()
            lines += [line]

    mode = 'COMMAND'
    cwd = []
    file_sizes = {}
    for l in lines:
        if mode == "LS":
            if l.startswith("$"):
                mode = "COMMAND"
            else:
                size, name = l.split()
                if size == "dir":
                    continue
                else:
                    size = int(size)
                    file_sizes["/".join(cwd + [name])] = size

        if mode == 'COMMAND':
            if l.startswith("$ cd "):
                d = l[len("$ cd "):]
                if d == "..":
                    cwd.pop()
                elif d == "/":
                    cwd.append("root")
                else:
                    cwd.append(d)
            elif l.startswith("$ ls"):
                mode = "LS"
            else:
                print("should not be here")

    dir_sizes = defaultdict(int)
    for file_path, file_size in file_sizes.items():
        path_parts = file_path.split('/')
        file_name = path_parts.pop()

        while path_parts:
            dir_sizes["/".join(path_parts)] += file_size
            path_parts.pop()

    filtered = []
    for dir_name, dir_size in dir_sizes.items():
        if dir_size <= 100*1000:
            filtered += [dir_name]

    total = 0
    for dir_name in filtered:
        total += dir_sizes[dir_name]


    print(total)

    total_disk = 70000000
    total_needed = 30000000

    free = total_disk - dir_sizes['root']
    still_needed = total_needed - free

    candidates = sorted(filter(lambda x: x > still_needed, dir_sizes.values()))
    print(candidates[0])

if __name__ == "__main__":
    main()