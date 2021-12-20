import re
from typing import List, Dict, Union

import numpy as np

NEI4 = np.array([[1, 0], [0, 1], [0, -1], [-1, 0]], dtype='int16')

NEI8 = NEIGHBORS = np.array([[-1, -1],
                             [-1, 0],
                             [-1, 1],
                             [0, -1],
                             [0, 1],
                             [1, -1],
                             [1, 0],
                             [1, 1]], dtype='int16')

ROT_LEFT_90 = np.array([[0, -1],
                        [1, 0]])
ROT_RIGHT_90 = np.array([[0, 1],
                         [-1, 0]])
DIRS = {
    'N': np.array([0, 1], dtype='int64'),
    'S': np.array([0, -1], dtype='int64'),
    'E': np.array([1, 0], dtype='int64'),
    'W': np.array([-1, 0], dtype='int64'),
}

cat = ''.join

K = np.ones((3, 3))
K[1, 1] = 0

def neighbors(a: np.ndarray, i: int, j: int) -> np.ndarray:
    return np.array([a[i + n[0], j + n[1]] for n in NEIGHBORS], dtype=a.dtype)


def rot_l(a: np.ndarray, k=1) -> np.ndarray:
    return np.linalg.matrix_power(ROT_LEFT_90, k) @ a


def rot_r(a: np.ndarray, k=1) -> np.ndarray:
    return np.linalg.matrix_power(ROT_RIGHT_90, k) @ a


def ints(inp_data: str) -> np.ndarray:
    return np.array([int(x) for x in re.findall(r'-?[0-9]+', inp_data)], dtype='int64')


def ints2(inp_data: str) -> np.ndarray:
    return np.array([ints(line) for line in inp_data.splitlines()], dtype='int64')


def ints2m(inp_data: Union[str, list], m: Dict) -> np.ndarray:
    if isinstance(inp_data, str):
        inp_data = inp_data.splitlines()
    return np.array([[m[c] for c in l] for l in inp_data], dtype='int16')


def blocks(inp_data: str) -> List[str]:
    return [x.strip() for x in re.split(r'\n\n', inp_data)]


if __name__ == '__main__':
    assert np.array_equal(np.array([1, 2, -1, 10]), ints('1asdf2\n\n-1         10'))
    assert np.array_equal(np.array([[1, 2], [3, 4]]), ints2('1,2\n,3,4'))
