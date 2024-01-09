class Kolejka:
    """
    Klasa reprezentująca kolejkę (FIFO)
    """
    def __init__(self, maksymalny_rozmiar: int = 1000):
        self.maksymalny_rozmiar = maksymalny_rozmiar
        self.__kolejka = [0, ]

    def dodanie_do_kolejki(self, element):
        """
        Dodaje element na koniec kolejki
        """
        if len(self.__kolejka) >= self.maksymalny_rozmiar:
            self.__kolejka.pop(0)
        self.__kolejka.append(element)

    def aktualna_kolejka(self):
        """
        Zwraca aktualną kolejke
        """
        return self.__kolejka

    def ostatnia_wartosc(self):
        return self.__kolejka[-1]
