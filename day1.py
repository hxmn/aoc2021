from itertools import pairwise

from aocd.models import Puzzle

puzzle = Puzzle(year=2021, day=1)

M = [int(x) for x in puzzle.input_data.splitlines()]
ans_a = 0
for a, b in pairwise(M):
    if a < b:
        ans_a += 1

ans_b = 0
for i in range(0, len(M) - 3):
    if sum(M[i:i + 3]) < sum(M[i + 1:i + 4]):
        ans_b += 1

puzzle.answer_a = ans_a
puzzle.answer_b = ans_b
