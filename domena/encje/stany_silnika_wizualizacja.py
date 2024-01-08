import numpy as np

w = (150, 150, 150)
r = (200, 0, 0)
e = (0, 0, 0)
STANY = {
    1: np.array([
        [e, e, w, w, w, w, e, e],
        [e, w, e, e, e, e, w, e],
        [w, e, e, e, e, e, e, w],
        [w, e, e, e, e, e, e, w],
        [w, e, e, e, e, e, e, r],
        [w, e, e, e, e, e, e, w],
        [e, w, e, e, e, e, w, e],
        [e, e, w, w, w, w, e, e]
    ]),
    2: np.array([
        [e, e, w, w, w, w, e, e],
        [e, w, e, e, e, e, w, e],
        [w, e, e, e, e, e, e, w],
        [w, e, e, e, e, e, e, w],
        [w, e, e, e, e, e, e, w],
        [w, e, e, e, e, e, e, r],
        [e, w, e, e, e, e, w, e],
        [e, e, w, w, w, w, e, e]
    ]),
    3: np.array([
        [e, e, w, w, w, w, e, e],
        [e, w, e, e, e, e, w, e],
        [w, e, e, e, e, e, e, w],
        [w, e, e, e, e, e, e, w],
        [w, e, e, e, e, e, e, w],
        [w, e, e, e, e, e, e, w],
        [e, w, e, e, e, e, r, e],
        [e, e, w, w, w, w, e, e]
    ]),
    4: np.array([
        [e, e, w, w, w, w, e, e],
        [e, w, e, e, e, e, w, e],
        [w, e, e, e, e, e, e, w],
        [w, e, e, e, e, e, e, w],
        [w, e, e, e, e, e, e, w],
        [w, e, e, e, e, e, e, w],
        [e, w, e, e, e, e, w, e],
        [e, e, w, w, w, r, e, e]
    ]),
    5: np.array([
        [e, e, w, w, w, w, e, e],
        [e, w, e, e, e, e, w, e],
        [w, e, e, e, e, e, e, w],
        [w, e, e, e, e, e, e, w],
        [w, e, e, e, e, e, e, w],
        [w, e, e, e, e, e, e, w],
        [e, w, e, e, e, e, w, e],
        [e, e, w, w, r, w, e, e]
    ]),
    6: np.array([
        [e, e, w, w, w, w, e, e],
        [e, w, e, e, e, e, w, e],
        [w, e, e, e, e, e, e, w],
        [w, e, e, e, e, e, e, w],
        [w, e, e, e, e, e, e, w],
        [w, e, e, e, e, e, e, w],
        [e, w, e, e, e, e, w, e],
        [e, e, w, r, w, w, e, e]
    ]),
    7: np.array([
        [e, e, w, w, w, w, e, e],
        [e, w, e, e, e, e, w, e],
        [w, e, e, e, e, e, e, w],
        [w, e, e, e, e, e, e, w],
        [w, e, e, e, e, e, e, w],
        [w, e, e, e, e, e, e, w],
        [e, w, e, e, e, e, w, e],
        [e, e, r, w, w, w, e, e]
    ]),
    8: np.array([
        [e, e, w, w, w, w, e, e],
        [e, w, e, e, e, e, w, e],
        [w, e, e, e, e, e, e, w],
        [w, e, e, e, e, e, e, w],
        [w, e, e, e, e, e, e, w],
        [w, e, e, e, e, e, e, w],
        [e, r, e, e, e, e, w, e],
        [e, e, w, w, w, w, e, e]
    ]),
    9: np.array([
        [e, e, w, w, w, w, e, e],
        [e, w, e, e, e, e, w, e],
        [w, e, e, e, e, e, e, w],
        [w, e, e, e, e, e, e, w],
        [w, e, e, e, e, e, e, w],
        [r, e, e, e, e, e, e, w],
        [e, w, e, e, e, e, w, e],
        [e, e, w, w, w, w, e, e]
    ]),
    10: np.array([
        [e, e, w, w, w, w, e, e],
        [e, w, e, e, e, e, w, e],
        [w, e, e, e, e, e, e, w],
        [w, e, e, e, e, e, e, w],
        [r, e, e, e, e, e, e, w],
        [w, e, e, e, e, e, e, w],
        [e, w, e, e, e, e, w, e],
        [e, e, w, w, w, w, e, e]
    ]),
    11: np.array([
        [e, e, w, w, w, w, e, e],
        [e, w, e, e, e, e, w, e],
        [w, e, e, e, e, e, e, w],
        [r, e, e, e, e, e, e, w],
        [w, e, e, e, e, e, e, w],
        [w, e, e, e, e, e, e, w],
        [e, w, e, e, e, e, w, e],
        [e, e, w, w, w, w, e, e]
    ]),
    12: np.array([
        [e, e, w, w, w, w, e, e],
        [e, w, e, e, e, e, w, e],
        [r, e, e, e, e, e, e, w],
        [w, e, e, e, e, e, e, w],
        [w, e, e, e, e, e, e, w],
        [w, e, e, e, e, e, e, w],
        [e, w, e, e, e, e, w, e],
        [e, e, w, w, w, w, e, e]
    ]),
    13: np.array([
        [e, e, w, w, w, w, e, e],
        [e, r, e, e, e, e, w, e],
        [w, e, e, e, e, e, e, w],
        [w, e, e, e, e, e, e, w],
        [w, e, e, e, e, e, e, w],
        [w, e, e, e, e, e, e, w],
        [e, w, e, e, e, e, w, e],
        [e, e, w, w, w, w, e, e]
    ]),
    14: np.array([
        [e, e, r, w, w, w, e, e],
        [e, w, e, e, e, e, w, e],
        [w, e, e, e, e, e, e, w],
        [w, e, e, e, e, e, e, w],
        [w, e, e, e, e, e, e, w],
        [w, e, e, e, e, e, e, w],
        [e, w, e, e, e, e, w, e],
        [e, e, w, w, w, w, e, e]
    ]),
    15: np.array([
        [e, e, w, r, w, w, e, e],
        [e, w, e, e, e, e, w, e],
        [w, e, e, e, e, e, e, w],
        [w, e, e, e, e, e, e, w],
        [w, e, e, e, e, e, e, w],
        [w, e, e, e, e, e, e, w],
        [e, w, e, e, e, e, w, e],
        [e, e, w, w, w, w, e, e]
    ]),
    16: np.array([
        [e, e, w, w, r, w, e, e],
        [e, w, e, e, e, e, w, e],
        [w, e, e, e, e, e, e, w],
        [w, e, e, e, e, e, e, w],
        [w, e, e, e, e, e, e, w],
        [w, e, e, e, e, e, e, w],
        [e, w, e, e, e, e, w, e],
        [e, e, w, w, w, w, e, e]
    ]),
    17: np.array([
        [e, e, w, w, w, r, e, e],
        [e, w, e, e, e, e, w, e],
        [w, e, e, e, e, e, e, w],
        [w, e, e, e, e, e, e, w],
        [w, e, e, e, e, e, e, w],
        [w, e, e, e, e, e, e, w],
        [e, w, e, e, e, e, w, e],
        [e, e, w, w, w, w, e, e]
    ]),
    18: np.array([
        [e, e, w, w, w, w, e, e],
        [e, w, e, e, e, e, r, e],
        [w, e, e, e, e, e, e, w],
        [w, e, e, e, e, e, e, w],
        [w, e, e, e, e, e, e, w],
        [w, e, e, e, e, e, e, w],
        [e, w, e, e, e, e, w, e],
        [e, e, w, w, w, w, e, e]
    ]),
    19: np.array([
        [e, e, w, w, w, w, e, e],
        [e, w, e, e, e, e, w, e],
        [w, e, e, e, e, e, e, r],
        [w, e, e, e, e, e, e, w],
        [w, e, e, e, e, e, e, w],
        [w, e, e, e, e, e, e, w],
        [e, w, e, e, e, e, w, e],
        [e, e, w, w, w, w, e, e]
    ]),
    20: np.array([
        [e, e, w, w, w, w, e, e],
        [e, w, e, e, e, e, w, e],
        [w, e, e, e, e, e, e, w],
        [w, e, e, e, e, e, e, r],
        [w, e, e, e, e, e, e, w],
        [w, e, e, e, e, e, e, w],
        [e, w, e, e, e, e, w, e],
        [e, e, w, w, w, w, e, e]
    ]),
}
