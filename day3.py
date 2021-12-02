from pprint import pprint

from aocd.models import Puzzle, default_user

puzzle = Puzzle(year=2021, day=3)

# print(puzzle.input_data)

ans_a = 0
ans_b = 0

pprint(default_user().get_stats(years=2021))
