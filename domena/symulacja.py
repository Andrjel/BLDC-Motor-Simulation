from scipy import signal

from domena.encje.kolejka import Kolejka
from domena.encje.obiekt_silnika import ObiektSilnika


class Symulacja:
    """
    Klasa, która ma za zadanie symulować pracę silnika
    w czasie rzeczywistym
    """

    def __init__(self):
        self.__czas_probkowania = 0.002
        self.__silnik = ObiektSilnika().transmitancja
        # [czas, wejście, wyjście]
        self.__dane = {"czas": Kolejka(), "wejscie": Kolejka(), "wyjscie": Kolejka()}

    def aktualizacja_symulacji(self, wej: float):
        """
        Aktualizuje symulacje
        """
        self.__dane["czas"].dodanie_do_kolejki(self.__dane['czas'].ostatnia_wartosc() + self.__czas_probkowania)
        self.__dane['wejscie'].dodanie_do_kolejki(wej)
        _, y, _ = signal.lsim(self.__silnik, U=self.__dane['wejscie'].aktualna_kolejka(),
                              T=self.__dane['czas'].aktualna_kolejka())
        self.__dane['wyjscie'].dodanie_do_kolejki(y[-1])

    def aktualne_wartosci(self):
        """
        Zwraca aktualne wartosci
        """
        return self.__dane


if __name__ == "__main__":
    sym = Symulacja()
    from matplotlib import pyplot as plt

    for i in range(100):
        wejscie = input("Podaj wejście: ")
        sym.aktualizacja_symulacji(float(wejscie))
        plt.plot(sym.__dane[0].aktualna_kolejka(), sym.__dane[2].aktualna_kolejka())
        plt.xlabel("Czas")
        plt.ylabel("Wyjście")
        plt.title("Odpowiedź obiektu w czasie rzeczywistym")
        plt.show(block=False)
        plt.pause(0.1)
