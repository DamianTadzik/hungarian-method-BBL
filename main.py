import numpy as np
import random
import brzana
import lewicka


def main():
    random.seed(1)      # Ziarno generatora
    matrix = np.array([[random.randint(0, 9) for i in range(6)] for j in range(6)])   # Tworzymy losową macierz 6 x 6

    print("Macierz początkowa:\n{}".format(matrix))

    lewicka.lewicka(matrix)
    brzana.brzana()




# Alg wykreślania zer macierzy minimalną liczbą linii
def barszczak():
    return 0


if __name__ == "__main__":
    main()
