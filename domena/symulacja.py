from scipy import signal
from domena.encje.obiekt_silnika import ObiektSilnika
from domena.encje.kolejka import Kolejka
from matplotlib import pyplot as plt
import threading
import time


class Symulacja:
    """
    Klasa, która ma za zadanie symulować pracę silnika
    w czasie rzeczywistym
    """
    def __init__(self):
        self.__czas_probkowania = 0.002
        self.__silnik = ObiektSilnika().transmitancja
        # [czas, wejście, wyjście]
        self.dane = {"czas": Kolejka(), "wejscie": Kolejka(), "wyjscie": Kolejka()}

    def aktualizacja_symulacji(self, wejscie:float):
        """
        Aktualizuje symulacje
        """
        self.dane["czas"].dodanie_do_kolejki(self.dane['czas'].ostatnia_wartosc() + self.__czas_probkowania)
        self.dane['wejscie'].dodanie_do_kolejki(wejscie)
        _, y, _ = signal.lsim(self.__silnik, U=self.dane['wejscie'].aktualna_kolejka(), T=self.dane['czas'].aktualna_kolejka())
        self.dane['wyjscie'].dodanie_do_kolejki(y[-1])


if __name__ == "__main__":
    sym = Symulacja()
    from matplotlib import pyplot as plt

    for i in range(100):
        wejscie = input("Podaj wejście: ")
        sym.aktualizacja_symulacji(float(wejscie))

        plt.plot(sym.dane[0].aktualna_kolejka(), sym.dane[2].aktualna_kolejka())
        plt.xlabel("Czas")
        plt.ylabel("Wyjście")
        plt.title("Odpowiedź obiektu w czasie rzeczywistym")
        plt.show(block=False)
        plt.pause(0.1)
