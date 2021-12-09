from aocd.models import Puzzle
from scipy import ndimage

from snippets import *

puzzle = Puzzle(year=2021, day=9)
pid = puzzle.input_data

M = np.array([[int(x) for x in line] for line in pid.splitlines()])

B, Nb = ndimage.label(M < 9, structure=np.array([[0, 1, 0],
                                                 [1, 1, 1],
                                                 [0, 1, 0]]))
beds = [M[B == i].min() for i in range(1, Nb + 1)]
puzzle.answer_a = sum(beds) + len(beds)
puzzle.answer_b = np.sort(np.unique(B, return_counts=True)[1])[-4:-1].prod()
