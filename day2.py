from aocd.models import Puzzle

puzzle = Puzzle(year=2021, day=2)

steps = [(x.split()[0], int(x.split()[1]))
         for x in puzzle.input_data.splitlines()]

H, D = 0, 0
aim, D_b = 0, 0
for step in steps:
    v = step[1]
    match step[0]:
        case 'forward':
            H += v
            D_b += aim * v
        case 'up':
            D -= v
            aim -= v
        case 'down':
            D += v
            aim += v

puzzle.answer_a = H * D
puzzle.answer_b = H * D_b