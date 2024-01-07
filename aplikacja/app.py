import time
from domena.symulacja import Symulacja


class Aplikacja:
    """
    Główna klasa kontrolująca aplikacje
    """
    def __init__(self):
        self.__symulacja = Symulacja()
        self.akt_wartosc = 0
        self.poprzed_wartosc = 0
        self.__kontrola_watku = True

    def glowna_petla(self):
        """
        Główna pętla aplikacji
        """
        import threading
        t = threading.Thread(target=self.watek_symulacji)
        t.start()
        while True:
            wartosc_pwm = input("Podaj wartość PWM (0-255): ")
            if wartosc_pwm.isdigit() and 0 <= int(wartosc_pwm) <= 255:
                self.akt_wartosc = (int(wartosc_pwm) / 255) * 5
            elif wartosc_pwm == "q":
                self.__kontrola_watku = False
                t.join()
                break
            elif wartosc_pwm == "data":
                self.__kontrola_watku = False
                t.join()
                print(self.__symulacja.aktualne_wartosci()["czas"].aktualna_kolejka(),
                      self.__symulacja.aktualne_wartosci()["wejscie"].aktualna_kolejka(),
                      self.__symulacja.aktualne_wartosci()["wyjscie"].aktualna_kolejka(),
                      sep="\n")
                self.__kontrola_watku = True
                t = threading.Thread(target=self.watek_symulacji)
                t.start()
            else:
                print("Podaj liczbę z zakresu 0-255")
                continue

    def watek_symulacji(self):
        """
        Funkcja wykonywana w osobnym wątku
        """
        while self.__kontrola_watku:
            self.__symulacja.aktualizacja_symulacji(self.akt_wartosc)

