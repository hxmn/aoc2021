import numpy as np
from aocd.models import Puzzle

puzzle = Puzzle(year=2021, day=3)
D = puzzle.input_data.splitlines()
M = np.array([[int(c) for c in d] for d in D])


def to_str(a: np.array):
    return ''.join([str(int(x)) for x in a])


def to_int(a: np.array):
    return int(to_str(a), 2)


gamma = M.sum(axis=0) > M.shape[0] / 2
puzzle.answer_a = to_int(gamma) * to_int(~gamma)

O = M.copy()
for i in range(len(D[0])):
    O = O[O[:, i] == (int(O[:, i].sum()) * 2 >= O.shape[0])]
    if O.shape[0] == 1: break

C = M.copy()
for i in range(len(D[0])):
    C = C[C[:, i] == (int(C[:, i].sum()) * 2 < C.shape[0])]
    if C.shape[0] == 1: break

puzzle.answer_b = to_int(O[0]) * to_int(C[0])
