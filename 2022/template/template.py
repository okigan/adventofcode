#! env python

from itertools import *
from functools import *
from collections import *

import os 

dir_path = os.path.dirname(os.path.realpath(__file__))

def main():

    with open(dir_path + "/input.txt") as f:
        for line in f.readlines():
            line = line.strip()
            print(line)

    print("hello, world!")

if __name__ == "__main__":
    main()