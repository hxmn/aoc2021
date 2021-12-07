import numpy as np

NEIGHBORS = np.array([[-1, -1], [-1, 0], [-1, 1], [0, -1], [0, 1], [1, -1], [1, 0], [1, 1]], dtype='int16')
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


def neighbors(a: np.ndarray, i: int, j: int) -> np.ndarray:
    return np.array([a[i + n[0], j + n[1]] for n in NEIGHBORS], dtype=a.dtype)


def rot_l(a: np.ndarray, k=1) -> np.ndarray:
    return np.linalg.matrix_power(ROT_LEFT_90, k) @ a


def rot_r(a: np.ndarray, k=1) -> np.ndarray:
    return np.linalg.matrix_power(ROT_RIGHT_90, k) @ a


def parse_arr(inp_data: str) -> np.ndarray:
    tokens = inp_data.splitlines() if '\n' in inp_data else inp_data.split(',')
    return np.array([int(x) for x in tokens], dtype='int64')
