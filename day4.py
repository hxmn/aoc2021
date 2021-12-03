from aocd.models import Puzzle

puzzle = Puzzle(year=2021, day=4)
D = puzzle.input_data.splitlines()

puzzle.answer_a = None
puzzle.answer_b = None