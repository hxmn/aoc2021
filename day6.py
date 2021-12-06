import numpy as np
from aocd.models import Puzzle

ans_a, ans_b = None, None
puzzle = Puzzle(year=2021, day=6)
pid = puzzle.input_data

a = np.array([0] * 9, dtype='int64')
ages = np.array([int(x) for x in pid.split(',')])
uniqs, counts = np.unique(ages, return_counts=True)
a[uniqs] = counts

for i in range(256):
   b = a.copy()
   for j in range(8):
       b[j] = a[j+1]
   b[6] += a[0]
   b[8] = a[0]
   a = b
   if i == 79:
       puzzle.answer_a = sum(a)
puzzle.answer_b = sum(a)
