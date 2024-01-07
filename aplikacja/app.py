import time
from domena.symulacja import Symulacja
from matplotlib import pyplot as plt


class Aplikacja:
    """
    Główna klasa kontrolująca aplikacje
    """
    akt_wartosc = 0
    poprzed_wartosc = None

    def __init__(self):
        self.__symulacja = Symulacja()

    def glowna_petla(self):
        """
        Główna pętla aplikacji
        """
        import threading
        t = threading.Thread(target=self.thread_job)
        t.start()
        try:
            while True:
                self.akt_wartosc = float(input("Podaj wejście: "))
                if self.poprzed_wartosc != self.akt_wartosc:
                    self.poprzed_wartosc = self.akt_wartosc
                if not (0 <= self.akt_wartosc <= 255):
                    print(self.__symulacja.aktualne_wartosci()["czas"].aktualna_kolejka(),
                          self.__symulacja.aktualne_wartosci()["wejscie"].aktualna_kolejka(),
                          self.__symulacja.aktualne_wartosci()["wyjscie"].aktualna_kolejka(),
                          sep="\n")
        except KeyboardInterrupt:
            exit(0)

    def thread_job(self):
        """
        Funkcja wykonywana w osobnym wątku
        """
        while True:
            if not (0 <= self.akt_wartosc <= 255):
                print("Zakończono symulacje")
                break
            self.__symulacja.aktualizacja_symulacji(self.akt_wartosc)


# if __name__ == "__main__":
#     sym = Symulacja()
#     from matplotlib import pyplot as plt
#     import threading
#     t = threading.Thread(target=thread_job)
#     t.start()
#     try:
#         while True:
#             wejscie = float(input("Podaj wejście: "))
#     except KeyboardInterrupt:
#         plt.close()
#         exit(0)
