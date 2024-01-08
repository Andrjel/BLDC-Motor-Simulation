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
            w, e, e, e, e, e, e, w,
            w, e, e, e, e, e, e, r,
            w, e, e, e, e, e, e, w,
            e, w, e, e, e, e, w, e,
            e, e, w, w, w, w, e, e
        ]
        self.set_pixels(image)


if __name__ == "__main__":
    print("To jest moduł sense_hat_controller.py")
    print("Uruchom plik aplikacja/app.py")
    SenseHatController()