from aocd.models import Puzzle
from scipy.ndimage import convolve

from snippets import *

puzzle = Puzzle(year=2021, day=11)
pid = puzzle.input_data
ans_a = 0

# energy
E = np.array([[int(x) for x in l] for l in pid.splitlines()], dtype='int8')
E = np.pad(E, 1, mode='constant')

# energy mask
M = np.zeros_like(E)
M[1:-1, 1:-1] = 1

for k in range(1000):
    E += 1
    F = np.zeros_like(E)
    while True:
        total_flashes = (F * M > 0).sum()
        C = ((E > 9) * (1 - F)).astype('int8')
        Ap = convolve(C, K, mode='constant') * (1 - F)
        E += Ap
        F |= C
        if total_flashes == (F * M > 0).sum():
            break
    E[E > 9] = 0
    E *= M
    if k < 100:
        ans_a += (E[1:-1, 1:-1] == 0).sum()
    if len(np.unique(E)) == 1:
        puzzle.answer_b = k + 1
        break

puzzle.answer_a = ans_a
