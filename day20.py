import numpy as np
from aocd.models import Puzzle

from snippets import blocks

m = {'.': 0, '#': 1}
puzzle = Puzzle(year=2021, day=20)
pid = blocks(puzzle.input_data)
algo = np.array([m[c] for c in pid[0]], dtype='int8')
img = np.array([[m[c] for c in l] for l in pid[1].splitlines()], dtype='int8')


def convert(img,  inf):
    img = np.pad(img, 2, constant_values=inf)
    new_img = np.ones_like(img) * inf
    for i in range(1, img.shape[0] - 1):
        for j in range(1, img.shape[1] - 1):
            ind = int(''.join([str(x) for x in img[i - 1:i + 2, j - 1:j + 2].flatten()]), 2)
            new_img[i, j] = algo[ind]
    return new_img[1:-1, 1:-1], algo[0] if inf == 0 else algo[511]

inf = 0
for i in range(50):
    img,  inf = convert(img, inf)
    if i == 1:
        puzzle.answer_a = img.sum()

puzzle.answer_b = img.sum()
