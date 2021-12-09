from functools import reduce

from aocd.models import Puzzle

from snippets import *

puzzle = Puzzle(year=2021, day=9)
pid = puzzle.input_data

M = np.array([[int(x) for x in line] for line in pid.splitlines()])
Mp = np.pad(M, 1, constant_values=(9,))
Mm = reduce(lambda x, y: np.minimum(x, y), [Mp,
                                            np.roll(Mp, 1, axis=0),
                                            np.roll(Mp, -1, axis=0),
                                            np.roll(Mp, 1, axis=1),
                                            np.roll(Mp, -1, axis=1)])
Ml = (Mm[1:-1, 1:-1] == M) & (M < 9)
puzzle.answer_a = Ml.sum() + M[Ml].sum()

from scipy import ndimage

B = ndimage.label(M < 9, structure=np.array([[0, 1, 0],
                                             [1, 1, 1],
                                             [0, 1, 0]]))
puzzle.answer_b = np.sort(np.unique(B[0], return_counts=True)[1])[-4:-1].prod()
