import numpy as np
from aocd.models import Puzzle

from snippets import parse_arr

a_a, a_b = 1 << 63, 1 << 63
puzzle = Puzzle(year=2021, day=7)
pid = puzzle.input_data

a = parse_arr(pid)
for x in range(a.min(), a.max()):
    n = np.abs((a - x))
    if n.sum() < a_a:
        a_a = n.sum()
    n = (n + 1) * n // 2
    if n.sum() < a_b:
        a_b = n.sum()
puzzle.answer_a = a_a
puzzle.answer_b = a_b
