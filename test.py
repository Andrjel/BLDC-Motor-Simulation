import numpy as np
import matplotlib.pyplot as plt
from scipy import signal
# Definiowanie transmitancji obiektu
numerator = [1]  # współczynniki licznika
denominator = [1, 2, 1]  # współczynniki mianownika

sys = signal.TransferFunction(numerator, denominator)

# Parametry symulacji
dt = 0.01  # krok czasowy
t_sim = np.arange(0, 10, dt)  # czas symulacji

# Inicjalizacja sygnału wejściowego
u = np.zeros_like(t_sim)

# Inicjalizacja sygnału wyjściowego
y = np.zeros_like(t_sim)

# Pętla symulacyjna
for i in range(len(t_sim)):
    # Zczytywanie wartości wejścia od użytkownika (możesz to dostosować do własnych potrzeb)
    u[i] = float(input(f'Podaj wartość wejścia w kroku {i + 1}: '))

    # Symulacja jednej próbki i pobranie odpowiedzi
    t, response, _ = signal.lsim(sys, u[:i + 1], t_sim[:i + 1])

    # Zapisywanie wartości wyjścia
    y[:i + 1] = response

    # Wykres wyników w czasie rzeczywistym
    plt.plot(t, response, label=f'Próbka {i + 1}')
    plt.xlabel('Czas')
    plt.ylabel('Odpowiedź obiektu')
    plt.title('Odpowiedź obiektu w czasie rzeczywistym')
    plt.legend()
    plt.grid(True)
    plt.show(block=False)
    plt.pause(0.1)  # Pause for a short time to make it visually real-time

plt.show()