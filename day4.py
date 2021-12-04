import re

import numpy as np
from aocd.models import Puzzle

ans_a, ans_b = None, None
puzzle = Puzzle(year=2021, day=4)
D = puzzle.input_data
D = re.split(r'\n\n', D)
nums = [int(x) for x in D[0].split(',')]
C = np.array([[[int(d) for d in l.split()] for l in s.splitlines()] for s in D[1:]])
M = np.zeros(C.shape, dtype='int16')
for num in nums:
    pred_wins = M.prod(axis=1).any(axis=1) + M.prod(axis=2).any(axis=1)
    M[C == num] = 1
    wins = M.prod(axis=1).any(axis=1) + M.prod(axis=2).any(axis=1)
    if wins.any():
        if ans_a is None:
            card_num = wins.nonzero()[0][0]
            ans_a = num * (C[card_num][M[card_num] == 0]).sum()
    if wins.all():
        if ans_b is None:
            card_num = np.argwhere(pred_wins == False)[0][0]
            ans_b = num * (C[card_num][M[card_num] == 0]).sum()
puzzle.answer_a = ans_a
puzzle.answer_b = ans_b
