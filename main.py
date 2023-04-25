import numpy as np
import random


def main():
    random.seed(1)
    A = np.array([[random.randint(0, 9) for i in range(6)] for j in range(6)])

    print("Macierz początkowa:\n{}".format(A))


# Redukcja macierzy
def lewicka():
    return 0  # macierz, lower bound


# Alg wyznaczania zer niezależnych
def brzana():
    return 0    # macierz,


# Alg wykreślania zer macierzy minimalną liczbą linii
def barszczak():
    return 0


if __name__ == "__main__":
    main()
