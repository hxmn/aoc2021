import networkx as nx
from aocd.models import Puzzle

from snippets import *


def shortest(A: np.ndarray) -> int:
    G = nx.Graph()
    n, m = A.shape
    for i in range(n):
        for j in range(m):
            if j > 0:
                G.add_edge((i, j - 1), (i, j), w=A[i, j - 1] + A[i, j])
            if i > 0:
                G.add_edge((i - 1, j), (i, j), w=A[i - 1, j] + A[i, j])
            if j < m - 1:
                G.add_edge((i, j + 1), (i, j), w=A[i, j + 1] + A[i, j])
            if i < n - 1:
                G.add_edge((i + 1, j), (i, j), w=A[i + 1, j] + A[i, j])
    return sum([A[n] for n in nx.shortest_path(G, source=(0, 0), target=(n - 1, m - 1), weight='w')]) - A[0, 0]


puzzle = Puzzle(year=2021, day=15)
pid = puzzle.input_data.splitlines()

A = np.array([[int(c) for c in l] for l in pid], dtype='int64')
puzzle.answer_a = shortest(A)

a = np.arange(5 * A.shape[0]) // A.shape[0]
A = np.tile(A, (5, 5))
A += a[np.newaxis, :] + a[:, np.newaxis]
A[A > 9] -= 9
puzzle.answer_b = shortest(A)
