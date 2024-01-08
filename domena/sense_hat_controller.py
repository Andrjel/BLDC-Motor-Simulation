from sense_hat import SenseHat
import numpy as np
import time


class SenseHatController(SenseHat):
    def __init__(self):
        super().__init__()
        self.clear()
        self.__kat = 0
        # tworzenie silnika na macierzy LED
        w = (150, 150, 150)
        r = (200, 0, 0)
        e = (0, 0, 0)

        self.__silnik = np.array([
            [e, e, w, w, w, w, e, e],
            [e, w, e, e, e, e, w, e],
            [w, e, e, e, e, e, e, w],
            [w, e, e, e, e, e, e, w],
            [w, e, e, e, e, e, e, r],
            [w, e, e, e, e, e, e, w],
            [e, w, e, e, e, e, w, e],
            [e, e, w, w, w, w, e, e]
        ])
        self.set_pixels(self.__silnik.tolist())

    def obrot_silnika(self, predkosc_silnika):
        """
        obraca silnik o zadana predkosc
        """
        if predkosc_silnika < 10:
            return
        opoznienie = 1 // predkosc_silnika

        self.__silnik = np.rot90(self.__silnik, self.__kat % 360 // 45)
        self.set_pixels(self.__silnik.tolist())
        time.sleep(opoznienie)
        self.__kat += 1
        if self.__kat > 360:
            self.__kat = 0


if __name__ == "__main__":
    print("To jest moduł sense_hat_controller.py")
    print("Uruchom plik aplikacja/app.py")
    SenseHatController()