from dataclasses import dataclass, field
from scipy import signal


@dataclass
class ObiektSilnika:
    """
    Klasa reprezentująca obiekt silnika
    Pola:
    licznik - współczynniki licznika transmitancji
    mianownik - współczynniki mianownika transmitancji
    transmitancja - transmitancja obiektu
    """
    licznik: list = field(default_factory=list)
    mianownik: list = field(default_factory=list)

    def __post_init__(self):
        self.licznik = [1.146e+06]
        self.mianownik = [1.0, 68.44, 491.3]
        self.transmitancja = signal.TransferFunction(self.licznik,
                                                     self.mianownik)
