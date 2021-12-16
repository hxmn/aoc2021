import io
from functools import reduce

ops = {
    0: int.__add__,
    1: int.__mul__,
    2: min,
    3: max,
    5: int.__gt__,
    6: int.__lt__,
    7: int.__eq__
}


class Packet:
    def __init__(self, f) -> None:
        self.ver = int(f.read(3), 2)
        self.typ = int(f.read(3), 2)
        self.subs = list()
        self.val = None

        if self.typ == 4:
            vs = list()
            t = '1'
            while t[0] != '0':
                t = f.read(5)
                vs.append(t[1:])
            self.val = int(''.join(vs), 2)
        else:
            i = f.read(1)
            if i == '0':
                end_pos = int(f.read(15), 2) + f.tell()
                while f.tell() < end_pos: self.subs.append(Packet(f))
            else:
                for _ in range(int(f.read(11), 2)): self.subs.append(Packet(f))

    def sum_vers(self) -> int:
        return self.ver + sum([s.sum_vers() for s in self.subs])

    def get_val(self) -> int:
        return self.val or reduce(lambda x, y: ops[self.typ](x, y), [v.get_val() for v in self.subs])


from aocd.models import Puzzle

puzzle = Puzzle(year=2021, day=16)
pid = ''.join([f'{int(c, 16):04b}' for c in puzzle.input_data])
p = Packet(io.StringIO(pid))
puzzle.answer_a = p.sum_vers()
puzzle.answer_b = p.get_val()
