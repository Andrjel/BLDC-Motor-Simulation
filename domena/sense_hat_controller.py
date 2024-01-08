from sense_hat import SenseHat
import numpy as np


class SenseHatController(SenseHat):
    def __init__(self):
        super().__init__()
        # tworzenie silnika na macierzy LED
        w = (150, 150, 150)
        r = (200, 0, 0)
        e = (0, 0, 0)

        image = [
            e, e, w, w, w, w, e, e,
            e, w, e, e, e, e, w, e,
            w, e, e, e, e, e, e, w,
            r, e, e, e, e, e, e, w,
            w, e, e, e, e, e, e, w,
            w, e, e, e, e, e, e, w,
            e, w, e, e, e, e, w, e,
            e, e, w, w, w, w, e, e
        ]
        self.set_pixels(image)