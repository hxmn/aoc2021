from more_itertools import pairwise
from collections import Counter

from aocd.models import Puzzle

from snippets import *

puzzle = Puzzle(year=2021, day=14)
poly, rules = blocks(puzzle.input_data)
rules = {k: v for k, v in [l.split(' -> ') for l in rules.splitlines()]}

pair_count = Counter([a + b for a, b in pairwise(poly)])
for i in range(40):
    next_pairs_count = Counter()
    for pair, val in pair_count.items():
        if pair in rules:
            insert_letter = rules[pair]
            next_pairs_count[pair[0] + insert_letter] += val
            next_pairs_count[insert_letter + pair[1]] += val
        else:
            next_pairs_count[pair] = val
    pair_count = next_pairs_count

    if i == 9 or i == 39:
        letters_counter = Counter()
        for pair, val in pair_count.items():
            letters_counter[pair[0]] += val
            letters_counter[pair[1]] += val

        answer = (letters_counter.most_common()[0][1] - letters_counter.most_common()[-1][1]) // 2
        if i == 9:
            puzzle.answer_a = answer
        else:
            puzzle.answer_b = answer
