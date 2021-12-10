from aocd.models import Puzzle

puzzle = Puzzle(year=2021, day=10)
ans_a = 0
open, closed = '([{<', ')]}>'
m_oc = {k: v for k, v in zip(open, closed)}
m_co = {k: v for k, v in zip(closed, open)}
a_c = {k: v for k, v in zip(closed, [3, 57, 1197, 25137])}
b_c = {k: v for k, v in zip(closed, range(1, 5))}


scores = list()
for line in puzzle.input_data.splitlines():
    stack = list()

    for c in line:
        if c in open:
            stack.append(c)
        if c in closed:
            if stack[-1] == m_co[c]:
                stack.pop()
            else:
                ans_a += a_c[c]
                break
    else:
        score = 0
        for c in [m_oc[c] for c in stack[::-1]]:
            score = score * 5 + b_c[c]
        scores.append(score)

puzzle.answer_a = ans_a
puzzle.answer_b = sorted(scores)[len(scores) // 2]