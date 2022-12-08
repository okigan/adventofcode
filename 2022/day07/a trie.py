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

    dir_tree = {}
    for file_path, file_size in file_sizes.items():
        path_parts = file_path.split('/')
        file_name = path_parts.pop()

        curr_dir_sizes = dir_tree
        for p in path_parts:
            curr_dir_sizes = curr_dir_sizes.setdefault(p, {})

        curr_dir_sizes[file_name] = file_size

    def calc_size(d:dict):
        total = 0
        for k,v in d.items():
            if type(v) == type({}):
                total += calc_size(v)
            else:
                total += v
        return total
    total_size = calc_size(dir_tree)

    tree_sizes = {}
    def calc_tree_sizes(path:str, d:dict):
        total = 0
        for k,v in d.items():
            if type(v)==type({}):
                total += calc_tree_sizes(path + k, v)
            else:
                total += v
        tree_sizes[path] = total
        return total

    calc_tree_sizes("", dir_tree)


    filtered = []
    for k,v in tree_sizes.items():
        if v <= 100*1000:
            filtered += [k]

    total = 0
    for k in filtered:
        total += tree_sizes[k]
    print(total)



if __name__ == "__main__":
    main()