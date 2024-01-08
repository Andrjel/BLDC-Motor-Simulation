from sense_hat import SenseHat
import numpy as np
import time
from domena.encje.stany_silnika_wizualizacja import *


class SenseHatController(SenseHat):
    def __init__(self):
        super().__init__()
        self.clear()
        self.__silnik_do_wyswietlenia = []
        self.__stan = 1

        self.__silnik_obrot = STANY[self.__stan]
        self.przygotowanie_silnika_do_wyswietlenia()
        self.set_pixels(self.__silnik_do_wyswietlenia)

    def obrot_silnika(self, predkosc_silnika):
        """
        obraca silnik o zadana predkosc
        """
        if predkosc_silnika < 10:
            return
        opoznienie = 1 // predkosc_silnika

        self.__stan += 1 if self.__stan + 1 < 21 else -19
        self.__silnik_obrot = STANY[self.__stan]
        self.przygotowanie_silnika_do_wyswietlenia()
        self.set_pixels(self.__silnik_do_wyswietlenia)
        time.sleep(opoznienie)


    def przygotowanie_silnika_do_wyswietlenia(self):
        """
        wyplaszcza macierz silnika do wizualizacji
        """
        self.__silnik_do_wyswietlenia = [j for i in self.__silnik_obrot.tolist() for j in i]


if __name__ == "__main__":
    print("To jest moduł sense_hat_controller.py")
    print("Uruchom plik aplikacja/app.py")
    SenseHatController()