#! /usr/bin/env python

print('hello')

import os
import sys

numbers = []
width = 0

with open('./input.txt') as f:
    for line in f.readlines():
        if len(line) > 1:
            numbers.append(int(line, 2))
            width = max(width, len(line))

oxygen_generator_rating = 0

width -= 1

numbers_back = numbers[:]
while len(numbers)> 1:
    for i in range(width):
        stat = {0: 0, 1: 0}
        mask = 1 << (width - i -1) 
        for n in numbers:
            key = 1 if (n & mask) > 0 else 0
            stat[key] += 1

        filtered = []
        for i, n in enumerate(numbers):
            if stat[1] >= stat[0]:
                if n & mask:
                    filtered.append(n)
            if stat[0] > stat[1]:
                if n & mask == 0:
                    filtered.append(n)
        numbers = filtered

        if len(numbers) < 2:
            break




oxygen_generator_rating = numbers[0]

numbers = numbers_back[:]

while len(numbers)> 1:
    for i in range(width):
        stat = {0: 0, 1: 0}
        mask = 1 << (width - i -1) 
        for n in numbers:
            key = 1 if (n & mask) > 0 else 0
            stat[key] += 1

        filtered = []
        for i, n in enumerate(numbers):
            if stat[0] <= stat[1]:
                if n & mask == 0:
                    filtered.append(n)
            if stat[1] < stat[0]:
                if n & mask != 0:
                    filtered.append(n)
        numbers = filtered

        if len(numbers) < 2:
            break


CO2_scrubber_rating = numbers[0]

life = oxygen_generator_rating * CO2_scrubber_rating


print(life) 
