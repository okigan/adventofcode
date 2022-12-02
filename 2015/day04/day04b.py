#! env python

from itertools import *
from functools import *
from collections import *

import hashlib

import os 

dir_path = os.path.dirname(os.path.realpath(__file__))

def main():

    prefix = ''
    with open(dir_path + "/input.txt", "rt") as f:
        for line in f.readlines():
            prefix = line.strip()
            break

    n = 0
    while True:
        result = hashlib.md5((prefix + str(n)).encode())
        if result.hexdigest()[:6] == "000000":
            break
        n += 1
    print(n)
if __name__ == "__main__":
    main()