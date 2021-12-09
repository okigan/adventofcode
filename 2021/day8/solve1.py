#! /usr/bin/env python

print('hello')

import os
import sys
import re

from functools import * 
from collections import *

def main():
    segments_lines = []
    with open('./input.txt', 'rt') as f:
        while True:
            line = f.readline().strip()
            if len(line) == 0:
                break
            segments = re.split(' |\|', line)
            segments_lines += [segments]

    outputs = []

    for segment_line in segments_lines:
        outputs += segment_line[-4:]

    outputs_length = map(lambda x: len(x), outputs)
    outputs_length_hist = Counter(outputs_length)

    return outputs_length_hist[2] + outputs_length_hist[3] + outputs_length_hist[4] + outputs_length_hist[7]
 
print(main())   