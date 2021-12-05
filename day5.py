import numpy as np
from aocd.models import Puzzle

puzzle = Puzzle(year=2021, day=5)

A = np.zeros((1000, 1000), dtype='int16')
B = np.zeros((1000, 1000), dtype='int16')
for l in puzzle.input_data.splitlines():
    x1, y1, x2, y2 = [int(x) for x in l.replace(' -> ', ',').split(',')]
    L = (abs(x1 - x2) or abs(y1 - y2)) + 1

    xr = np.linspace(x1, x2, L, dtype='int16')
    yr = np.linspace(y1, y2, L, dtype='int16')

    if x1 == x2 or y1 == y2:
        A[xr, yr] += 1
    B[xr, yr] += 1
puzzle.answer_a = (A > 1).sum()
puzzle.answer_b = (B > 1).sum()
