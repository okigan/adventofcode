#! /usr/bin/env python

print('hello')

import os
import sys
import re

draws = []
boards = []

def return_winning_board(board, draw):
    s = 0
    for r in board:
        for c in r:
            if c > 0:
                s += c
    result = s * draw

    if result == 0:
        print(result)
    return result

def main():
    with open('./input.txt') as f:
        draws = list(map(int, f.readline().split(',')))
        boards = []

        done = False
        while not done:
            board = []
            dummy = f.readline()
            for i in range(5):
                line = f.readline().strip()
                if len(line) == 0:
                    done = True
                    break
                s  = re.split(' +', line)
                row = list(map(int, s))
                board.append( row )
            if len(board) > 0:
                boards += [board]

        winnings = []
        already_won = set()
        for d in draws:
            # update board
            for ib, b in enumerate(boards):
                if ib not in already_won:
                    for r in b:
                        for i,n in enumerate(r):
                            if n == d:
                                r[i] *= -1
            # check board for winning row or columns (no diag, phew)
            for ib, b in enumerate(boards):
                if ib not in already_won:
                    for r in b:
                        if all(c<0 for c in r):
                            winnings += [return_winning_board(b, d)]
                            already_won.add(ib)
                    for c in range(len(b[0])):
                        column = []
                        for r in range(len(b)):
                            column.append(b[r][c])
                        if all(c<0 for c in column):
                            winnings += [return_winning_board(b, d)]
                            already_won.add(ib)

    return winnings

# print(draws)
# print(boards)
print(main())