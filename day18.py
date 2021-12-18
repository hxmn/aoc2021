from functools import reduce
from itertools import permutations

from aocd.models import Puzzle

puzzle = Puzzle(year=2021, day=18)
pid = puzzle.input_data


class Pair:
    def __init__(self, s: str) -> None:
        self.vals, self.depths, cur_d = list(), list(), 0
        for c in s:
            if c == '[':
                cur_d += 1
            elif c == ']':
                cur_d -= 1
            elif c != ',':
                self.vals.append(int(c))
                self.depths.append(cur_d)

    def explode(self):
        v, d = self.vals, self.depths
        while any([x == 5 for x in d]):
            for i in range(len(v) - 1):
                if d[i] == d[i + 1] and d[i] == 5:
                    if i > 0: v[i - 1] += v[i]
                    if i + 1 < len(v) - 1: v[i + 2] += v[i + 1]
                    del v[i + 1], d[i + 1]
                    v[i] = 0
                    d[i] -= 1
                    return True
        return False

    def split(self):
        v, d = self.vals, self.depths
        while any([x >= 10 for x in v]):
            for i in range(len(v)):
                if v[i] >= 10:
                    x, y = v[i] // 2, (v[i] + 1) // 2
                    v[i] = x
                    v.insert(i + 1, y)
                    d[i] += 1
                    d.insert(i + 1, d[i])
                    self.explode()
                    return True
        return False

    def final_sum(self):
        a, d = self.vals.copy(), self.depths.copy()
        for l in range(5, 0, -1):
            while any([x == l for x in d]) and len(a) != 1:
                for i in range(len(d) - 1):
                    if d[i] == d[i + 1] and d[i] == l:
                        a[i] = 3 * a[i] + 2 * a[i + 1]
                        d[i] -= 1
                        del a[i + 1], d[i + 1]
                        break
        return a[0]

    def reduce(self):
        while self.explode(): pass
        while self.split(): pass

    def __add__(self, p2):
        self.depths = list(map(lambda x: x + 1, self.depths))
        p2.depths = list(map(lambda x: x + 1, p2.depths))
        self.vals.extend(p2.vals)
        self.depths.extend(p2.depths)
        self.reduce()
        return self

    def __repr__(self) -> str:
        return str(self.vals) + '\n' + str(self.depths)


p = reduce(lambda x, y: x + y, [Pair(l) for l in pid.splitlines()])
puzzle.answer_a = p.final_sum()

ans_b = 0
for l1, l2 in permutations(pid.splitlines(), 2):
    p1, p2 = Pair(l1), Pair(l2)
    ans_b = max((p1 + p2).final_sum(), ans_b)
puzzle.answer_b = ans_b
