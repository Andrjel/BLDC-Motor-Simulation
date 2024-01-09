import time
from domena.symulacja import Symulacja
from domena.filemanager import FileManager
import os
from domena.sense_hat_controller import SenseHatController


class Aplikacja:
    """
    Główna klasa kontrolująca aplikacje
    """
    def __init__(self):
        if os.uname()[0] == "Linux":
            self.__sense_hat = SenseHatController()
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
                print(self.__symulacja.dane["czas"].aktualna_kolejka(),
                      self.__symulacja.dane["wejscie"].aktualna_kolejka(),
                      self.__symulacja.dane["wyjscie"].aktualna_kolejka(),
                      sep="\n")
                self.__kontrola_watku = True
                t = threading.Thread(target=self.watek_symulacji)
                t.start()
            elif wartosc_pwm == "save":
                self.__kontrola_watku = False
                t.join()
                FileManager.zapisz_dane(self.__symulacja)
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
            self.__sense_hat.obrot_silnika(self.__symulacja.dane["wyjscie"].ostatnia_wartosc())
