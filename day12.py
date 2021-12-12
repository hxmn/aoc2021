from collections import defaultdict, Counter

from aocd.models import Puzzle

puzzle = Puzzle(year=2021, day=12)
pid = puzzle.input_data

conns = defaultdict(lambda: list())
for l in puzzle.input_data.splitlines():
    u, v = l.split('-')
    conns[u].append(v)
    conns[v].append(u)

ps = [['start']]
while not all([p[-1] == 'end' for p in ps]):
    new_ps = list()
    for p in ps:
        if p[-1] == 'end':
            new_ps.append(p)
            continue
        for c in conns[p[-1]]:
            if c == 'start':
                continue
            if c.islower() and c in p:
                continue
            new_ps.append([*p, c])
    ps = new_ps
puzzle.answer_a = len(ps)

ps = [['start']]
while not all([p[-1] == 'end' for p in ps]):
    new_ps = list()
    for p in ps:
        if p[-1] == 'end':
            new_ps.append(p)
            continue
        for c in conns[p[-1]]:
            if c == 'start':
                continue
            if c.islower() and c in p:
                if 2 in Counter([x for x in p if x.islower()]).values():
                    continue
            new_ps.append([*p, c])
    ps = new_ps
puzzle.answer_b = len(ps)

