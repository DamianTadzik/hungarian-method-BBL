import numpy as np
import random
from brzana import brzana
from lewicka import lewicka


def main():
    random.seed(1)      # Ziarno generatora
    matrix = np.array([[random.randint(0, 9) for i in range(6)] for j in range(6)])   # Tworzymy losową macierz 6 x 6

    print("Macierz początkowa:\n{}".format(matrix))

    reduced_matrix, lower_bound = lewicka(matrix)   # redukcja macierzy
    independent_zeros = brzana(reduced_matrix)  # wyszukanie zer niezależnych
    x = 1


# Alg wykreślania zer macierzy minimalną liczbą linii
def barszczak():
    return 0


if __name__ == "__main__":
    main()
