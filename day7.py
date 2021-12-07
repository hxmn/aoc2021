import numpy as np
from aocd.models import Puzzle

from snippets import parse_arr

a_a, a_b = 1 << 63, 1 << 63
puzzle = Puzzle(year=2021, day=7)
pid = puzzle.input_data

a = parse_arr(pid)
for x in range(a.min(), a.max()):
    s = np.abs(a - x)
    a_a = min(a_a, s.sum())
    a_b = min(a_b, ((s + 1) * s // 2).sum())
puzzle.answer_a, puzzle.answer_b = a_a, a_b
