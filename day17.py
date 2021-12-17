from aocd.models import Puzzle

puzzle = Puzzle(year=2021, day=17)
Tx = [70, 125]
Ty = [-159, -121]


def simulate(vx: int, vy: int):
    mY = 0
    x, y = 0, 0
    while True:
        x, y = x + vx, y + vy
        mY = max(y, mY)
        if vx > 0:
            vx -= 1
        vy -= 1
        if Tx[0] <= x <= Tx[1] and Ty[0] <= y <= Ty[1]:
            return mY
        elif (x > Tx[1] or vx == 0) and y < Ty[0]:
            return None


ans_a = 0
vs = set()
for vx in range(130):
    for vy in range(-160, 200):
        mY = simulate(vx, vy)
        if mY is not None and mY > ans_a:
            ans_a = mY
        if mY is not None:
            vs.add((vx, vy))

puzzle.answer_a = ans_a
puzzle.answer_b = len(vs)
