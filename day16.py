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
            while True:
                t = f.read(5)
                vs.append(t[1:])
                if t[0] == '0':
                    break
            self.val = int(''.join(vs), 2)
        else:
            i = f.read(1)
            if i == '0':
                tl = int(f.read(15), 2)
                start = f.tell()
                while f.tell() < start + tl:
                    self.subs.append(Packet(f))
            else:
                pn = int(f.read(11), 2)
                for _ in range(pn):
                    self.subs.append(Packet(f))

    def sum_vers(self) -> int:
        return self.ver + sum([s.sum_vers() for s in self.subs])

    def get_val(self) -> int:
        if self.val is not None:
            return self.val
        else:
            return reduce(lambda x, y: ops[self.typ](x, y), [v.get_val() for v in self.subs])


from aocd.models import Puzzle

puzzle = Puzzle(year=2021, day=16)
pid = puzzle.input_data
pid = ''.join([f'{int(c, 16):04b}' for c in pid])
f = io.StringIO(pid)
p = Packet(f)
puzzle.answer_a = p.sum_vers()
puzzle.answer_b = p.get_val()
