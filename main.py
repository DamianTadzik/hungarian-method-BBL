import numpy as np
import random
import brzana


def main():
    random.seed(1)      # Ziarno generatora
    A = np.array([[random.randint(0, 9) for i in range(6)] for j in range(6)])   # Tworzymy losową macierz 6 x 6

    print("Macierz początkowa:\n{}".format(A))

    brzana.brzana()


# Redukcja macierzy
def lewicka():
    return 0  # macierz, lower bound


# Alg wykreślania zer macierzy minimalną liczbą linii
def barszczak():
    return 0


if __name__ == "__main__":
    main()
