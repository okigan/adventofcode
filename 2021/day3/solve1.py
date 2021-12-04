#! /usr/bin/env python

print('hello')

import os
import sys

numbers = []
width = 2

with open('./input.txt') as f:
    for line in f.readlines():
        if len(line) > 1:
            numbers.append(int(line, 2))
            width = max(width, len(line))

gamma_rate = ''
epsilon_rate = ''


width -= 1

for i in range(width):
    stat = {0: 0, 1: 0}
    mask = 1 << (width - i -1) 
    for n in numbers:
        key = 1 if (n & mask) > 0 else 0
        stat[key] += 1

    gamma_rate += '1' if stat[1] > stat[0] else '0'
    epsilon_rate += '0' if stat[0] < stat[1] else '1'

g = int(gamma_rate, 2)
e = int(epsilon_rate, 2)

power = g * e

print(power)
