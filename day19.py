from itertools import permutations, product

import numpy as np
from aocd.models import Puzzle

from snippets import blocks

puzzle = Puzzle(year=2021, day=19)
pid = blocks(puzzle.input_data)

AXES = [np.array(a) for a in permutations([1, 2, 3])]
DIRS = [np.array(d) for d in product([-1, 1], [-1, 1], [-1, 1])]
ALL = [(ax, d) for ax, d in product(AXES, DIRS)]


class Scanner:
    def __init__(self, bs: str) -> None:
        lines = bs.splitlines()
        self.points = np.array([[int(x) for x in l.split(',')] for l in lines[1:]], dtype='int16')
        self.pos = None

    def make_shift(self, s2: 'Scanner'):
        if s2.pos is not None: return False
        p1 = self.points
        for ax, d in ALL:
            p2 = s2.points[:, ax - 1] * d
            d = p1[np.newaxis, :] - p2[:, np.newaxis]
            uns = [np.unique(d[..., i], return_counts=True) for i in range(3)]
            if all([un[1].max() >= 12 for un in uns]):
                s2.points = p2
                s2.pos = np.array([u[0][u[1] >= 12][0] for u in uns], dtype='int16')
                s2.pos += self.pos
                return True
        return False


scanners = [Scanner(b) for b in pid]
scanners[0].pos = np.array([0, 0, 0])
while any(s.pos is None for s in scanners):
    for s in scanners:
        if s.pos is None:
            for posed in scanners:
                if posed.pos is not None and posed.make_shift(s):
                    break

beacons = set()
for s in scanners:
    for p in (s.points + s.pos):
        beacons.add(tuple(p))
puzzle.answer_a = len(beacons)

mx = 0
for s1, s2 in permutations(scanners, 2):
    d = np.abs(s1.pos - s2.pos).sum()
    mx = max(mx, d)
puzzle.answer_b = mx
