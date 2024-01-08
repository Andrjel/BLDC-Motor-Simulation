import numpy as np


w = (150, 150, 150)
r = (200, 0, 0)
e = (0, 0, 0)

silnik = np.array([
    [e, e, w, w, w, w, e, e],
    [e, w, e, e, e, e, w, e],
    [w, e, e, e, e, e, e, w],
    [w, e, e, e, e, e, e, w],
    [w, e, e, e, e, e, e, r],
    [w, e, e, e, e, e, e, w],
    [e, w, e, e, e, e, w, e],
    [e, e, w, w, w, w, e, e]
])

silnik_do_wyswietlenia = []
for i in silnik.tolist():
    for j in i:
        silnik_do_wyswietlenia.append(j)

print(silnik_do_wyswietlenia)