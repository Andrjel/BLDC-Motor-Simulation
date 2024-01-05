from entities.obiekt_silnika import ObiektSilnika
from entities.kolejka import Kolejka


class Applikacja:
    """
    Główna klasa kontrolująca aplikacje
    """
    def __init__(self):
        self.__silnik = ObiektSilnika()
        self.__dane = [Kolejka(), Kolejka()]
        print("Aplikacja została uruchomiona")
