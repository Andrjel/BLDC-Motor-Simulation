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
        self.dane = {"czas": Kolejka(), "wejscie": Kolejka(), "wyjscie": Kolejka()}

    def aktualizacja_symulacji(self, wejscie):
        """
        Aktualizuje symulacje
        """
        if wejscie is None:
            return
        self.dane["czas"].dodanie_do_kolejki(self.dane['czas'].ostatnia_wartosc() + self.__czas_probkowania)
        self.dane['wejscie'].dodanie_do_kolejki(wejscie)
        _, y, _ = signal.lsim(self.__silnik, U=self.dane['wejscie'].aktualna_kolejka(),
                              T=self.dane['czas'].aktualna_kolejka())
        self.dane['wyjscie'].dodanie_do_kolejki(y[-1])

    def aktualne_wartosci(self):
        """
        Zwraca aktualne wartosci
        """
        return self.dane
