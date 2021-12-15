import re
from collections import defaultdict, Counter
from itertools import permutations

from aocd.models import Puzzle

from snippets import cat

puzzle = Puzzle(year=2021, day=8)
pid = puzzle.input_data
N = ["abcefg", "cf", "acdeg", "acdfg", "bcdf", "abdfg", "abdefg", "acf", "abcdefg", "abcdfg"]
Ns = {*N}
nums = list()
for l in pid.splitlines():
    t = re.findall(r'[a-g]+', l)
    for p in permutations('abcdefg'):
        m = {a: b for a, b in zip(p, 'abcdefg')}
        s = [cat(sorted([m[c] for c in x])) for x in t]
        if {*s} == Ns:
            nums.append(cat([str(N.index(x)) for x in s[-4:]]))
c = Counter(cat(nums))
puzzle.answer_a = sum([c[str(i)] for i in {1, 4, 7, 8}])
puzzle.answer_b = sum([int(x) for x in nums])