import numpy as np
import random
from typing import List


def main():
    random.seed(1)
    matrix = np.array([[random.randint(0, 9) for i in range(6)] for j in range(6)])

    print("Macierz początkowa:\n{}".format(matrix))


#Redukcja macierzy
def lewicka(matrix) ->  List[List]:

    sum_reduction = 0
    for row in range(len(matrix)):
        min_value = min(matrix[row])
        sum_reduction += min_value
        for col in range(len(matrix)):
            matrix[row][col]  -= min_value
    
    return matrix, sum_reduction #macierz, dolne ograniczenie


# Alg wyznaczania zer niezależnych
def brzana():
    return 0    # macierz,


# Alg wykreślania zer macierzy minimalną liczbą linii
def barszczak():
    return 0


if __name__ == "__main__":
    main()
