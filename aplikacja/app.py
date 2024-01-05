from domena.symulacja import Symulacja


class Aplikacja:
    """
    Główna klasa kontrolująca aplikacje
    """
    def __init__(self):
        self.__symulacja = Symulacja()
        self.__running = True


    def glowna_petla(self):
        """
        Główna pętla aplikacji
        """
        while self.__running:
            wejscie = input("Podaj wejście: ")
            self.__symulacja.aktualizacja_symulacji(float(wejscie))
            self.__symulacja.aktualne_wartosci()