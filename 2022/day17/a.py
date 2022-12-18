#! env python

from itertools import *
from functools import *
from collections import *

import os 

dir_path = os.path.dirname(os.path.realpath(__file__))

def find_highest_filled_row(cave:dict):
    height = len(cave.items()) // 7
    for r in range(height - 1, -1, -1):
        for c in range(7):
            if cave[(c, r)] != ".":
                return r

    return 0

def add_rock_to_cave(cave, rock):
    h = find_highest_filled_row(cave)

    for r in range(h + 1, h + 1 + 3 + 1):
        for c in range(7):
            cave[(c, r)] = '.'

    for y, rock_row in enumerate(reversed(rock)):
        for c in range(7):
            cave[(c, h + 3 + y)] = '@' if rock_row[c] == '#' else rock_row[c]

def move_rocks_right(cave:dict):
    rows = len(cave.items()) // 7

    moved = False
    for r in range(rows - 1, -1, -1):
        for c in range(7-1, 0, -1):
            if cave[(c, r)] == ".":
                cave[(c, r)] = cave[(c - 1, r)]
                if cave[(c, r)] == "@":
                    moved = True
                cave[(c-1, r)] = "."
    return moved

def move_rocks_left(cave:dict):
    rows = len(cave.items()) // 7

    moved = False
    for r in range(rows - 1, -1, -1):
        for c in range(7 - 1):
            if cave[(c, r)] == ".":
                cave[(c, r)] = cave[(c + 1, r)]
                if cave[(c, r)] == "@":
                    moved = True

                cave[(c + 1, r)] = "."

    return moved

def move_rocks_down(cave:dict, start_row = 0):
    rows = len(cave.items()) // 7


    moved = False
    max_changed_rows = [rows]*7
    for r in range(start_row, rows - 1):
        for c in range(7):
            if cave[(c, r)] == ".":
                cave[(c, r)] = cave[(c, r + 1)]
                if cave[(c, r)] == "@":
                    moved = True
                    max_changed_rows[c] = min(r, max_changed_rows[c]) 

                cave[(c, r + 1)] = "."

            if (r == 0 and cave[(c, r)] == "@"):
                cave[(c, r)] = "#"

            if cave[(c, r)] == "#" and cave[(c, r+1)] == "@":
                cave[(c, r+1)] = "#"

    return moved, max_changed_rows

def main():
    rocks = []
    with open(dir_path + "/rocks.txt") as f:
        batch = []
        for line in f.readlines():
            line = line.strip()
            if line == "":
                rocks += [batch]
                batch = []
                continue
            line = '..' + line
            line = line + '.'*(7 - len(line))
            batch += [line]
        rocks += [batch]

    wind = ''
    with open(dir_path + "/input.txt") as f:
        for line in f.readlines():
            line = line.strip()
            wind = line

    cave = {}
    for r in range(1):
        for c in range(7):
            cave[(c, r)] = '.'
    
    highest_rock_per_column = []

    step_counter = 0
    while True:
        if step_counter >= 2022:
            break

        add_rock_to_cave(cave, rocks[step_counter % len(rocks)])
        step_counter += 1
        print_cave(cave)

        for c in wind:
            moved = True
            while moved:
                moved = False
                if c == ">":
                    moved = move_rocks_right(cave) or moved 
                    print_cave(cave)
                if c == "<":
                    moved = move_rocks_right(cave) or moved
                    print_cave(cave)
                moved, x = move_rocks_down(cave) or moved
                print_cave(cave)
            if step_counter >= 2022:
                break
            add_rock_to_cave(cave, rocks[step_counter % len(rocks)])
            step_counter += 1
        
        max_changed_row = 0
        while True:
            if step_counter >= 2022:
                break
            add_rock_to_cave(cave, rocks[step_counter % len(rocks)])
            step_counter += 1
            moved = True
            while moved:
                moved = False
                just_moved, max_changed_rows = move_rocks_down(cave, max_changed_row) 
                moved = just_moved or moved
                max_changed_row = min(max_changed_rows)

    print(find_highest_filled_row(cave))

def print_cave(cave):
    h = find_highest_filled_row(cave)

    for r in range(h, -1, -1):
        print("|", end="")
        for c in range(7):
            print(cave[(c, r)], end="")
        print("|", end="")
        print()
    print()


if __name__ == "__main__":
    main()