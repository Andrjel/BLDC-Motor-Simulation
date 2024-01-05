class Kolejka:
    """
    Klasa reprezentująca kolejkę (FIFO)
    """
    def __init__(self, maksymalny_rozmiar: int = 1000):
        self.maksymalny_rozmiar = maksymalny_rozmiar
        self.kolejka = []

    def dodanie_do_kolejkie(self, element):
        """
        Dodaje element do kolejki
        """
        if len(self.kolejka) >= self.maksymalny_rozmiar:
            self.kolejka.pop(0)
        self.kolejka.append(element)

    def aktualna_kolejka(self):
        """
        Zwraca aktualną kolejke
        """
        return self.kolejka
