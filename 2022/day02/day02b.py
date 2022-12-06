#! env python

from itertools import *
from functools import *
from collections import *

import os 

dir_path = os.path.dirname(os.path.realpath(__file__))

def main():

    data = []

    with open(dir_path + "/input.txt") as f:
        for line in f.readlines():
            line = line.strip()
            data += [line.split()]

    score = 0

    scoring = {
        "A": 1,
        "B": 2,
        "C": 3,
        "X": 1, # lose
        "Y": 2, # draw
        "Z": 3, # win
    }

    eq_map = {
        "A": "X",
        "B": "Y",
        "C": "Z",
    }

    winif = {
        "A": "Y",
        "B": "Z",
        "C": "X",
    }

    loseif = {
        "A": "C",
        "B": "A",
        "C": "B",
    }

    for k,v in data:
        curr_score = 0
        use = ''
        if v == "X": # lose
            use = loseif[k]
        elif v == "Y": # draw
            use = k
            curr_score += 3
        else: #win
            use = winif[k]
            curr_score += 6

        curr_score += scoring[use]
        
        score += curr_score
        
    print(score)


if __name__ == "__main__":
    main()