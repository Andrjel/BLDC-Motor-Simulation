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
        self.__kat = 1

        self.__silnik_obrot = STANY[self.__stan]
        self.przygotowanie_silnika_do_wyswietlenia()
        self.set_pixels(self.__silnik_do_wyswietlenia)

    def obrot_silnika(self, dane_silnika_poprzednie, dane_silnika_aktualne):
        """
        obraca silnik o zadana predkosc
        """
        czas_poprzedni, predkosc_silnika_poprzednia = dane_silnika_poprzednie
        czas_aktualny, predkosc_silnika_aktualna = dane_silnika_aktualne

        self.__kat += self.obliczenie_obrotu(czas_poprzedni,
                                             czas_aktualny,
                                             predkosc_silnika_poprzednia,
                                             predkosc_silnika_aktualna)
        self.__kat = self.__kat if self.__kat < 360 else self.__kat - 360
        self.__stan = int(self.__kat / 18) + 1
        self.__silnik_obrot = STANY[self.__stan]
        self.przygotowanie_silnika_do_wyswietlenia()
        self.set_pixels(self.__silnik_do_wyswietlenia)


    def przygotowanie_silnika_do_wyswietlenia(self):
        """
        wyplaszcza macierz silnika do wizualizacji
        """
        self.__silnik_do_wyswietlenia = [j for i in self.__silnik_obrot.tolist() for j in i]

    def obliczenie_obrotu(self, czas_poprzedni,
                          czas_aktualny,
                          predkosc_silnika_poprzednia,
                          predkosc_silnika_aktualna):
        """
        oblicza obrot silnika
        """
        delta_czas = czas_aktualny - czas_poprzedni
        return ((predkosc_silnika_poprzednia + predkosc_silnika_aktualna)
                / 2 * delta_czas)


if __name__ == "__main__":
    print("To jest moduł sense_hat_controller.py")
    print("Uruchom plik aplikacja/app.py")
    SenseHatController()
