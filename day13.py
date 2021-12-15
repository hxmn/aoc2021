from aocd.models import Puzzle

from snippets import *

puzzle = Puzzle(year=2021, day=13)
pid = blocks(puzzle.input_data)

i1 = ints2(pid[0])
P = np.zeros(i1.max(axis=0) + 1, dtype='bool')
P[i1[:, 0], i1[:, 1]] = True

for i, l in enumerate(pid[1].splitlines()):
    c = ints(l)[0]
    N, M = P.shape
    P = (P[0:c, :] | P[N - 1:c:-1, :]) if 'x' in l else \
        (P[:, 0:c] | P[:, M - 1:c:-1])
    if i == 0:
        puzzle.answer_a = P.sum()
print('\n'.join([''.join([('#' if c == 1 else ' ') for c in r]) for r in P.T]))
