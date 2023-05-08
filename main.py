import copy

import numpy as np
import random
from brzana import brzana
from lewicka import lewicka
from barszczak import barszczak


def hungarianMethod(matrix: np.ndarray):
    is_found = False # zmienna pomocnicza informujaca czy znaleziono wszyskie zera niezalezne
    independent_zeros = [] # zera niezalezne
    stage = 1 # etap

    print("Macierz początkowa:\n{}".format(matrix), end='\n\n') # wypiwywanie poczatkowej macierzy
    reduced_matrix = copy.deepcopy(matrix) # tworzenie kopii
    reduced_matrix, lower_bound = lewicka(reduced_matrix)  # redukcja macierzy

    print("Macierz po redukcji:\n{}".format(reduced_matrix), end='\n\n')  # wypiwywanie macierzy po redukcji

    while not is_found:
        independent_zeros = brzana(reduced_matrix)  # wyszukanie zer niezależnych
        reduced_matrix, lower_bound, is_found = barszczak(reduced_matrix, independent_zeros, lower_bound)  # Alg wykreślania zer macierzy minimalną liczbą linii
        print("Macierz w {} etapie:\n{}".format(stage, matrix), end='\n\n')  # wypiwywanie macierzy w okreslonym etapie wykonywania algorytmu
        stage += 1

    print("Macierz koncowa:", reduced_matrix, sep='\n', end='\n\n')

    for i in range(len(matrix)):
        for j in range(len(matrix)):
            if (i, j) in independent_zeros:
                reduced_matrix[i][j] = 1
            else:
                reduced_matrix[i][j] = 0

    return reduced_matrix, lower_bound


def main():
    random.seed(2)  # Ziarno generatora
    matrix = np.array([[random.randint(0, 9) for i in range(6)] for j in range(6)])  # Tworzymy losową macierz 6 x 6

    # matrix = np.array([
    #     [1, 2, 0, 4, 0, 5],
    #     [0, 4, 2, 0, 5, 6],
    #     [4, 5, 0, 4, 5, 1],
    #     [6, 2, 2, 0, 3, 3],
    #     [4, 3, 3, 4, 0, 6],
    #     [2, 4, 1, 2, 5, 7]
    # ])

    result_matrix, cost = hungarianMethod(matrix) # wywolanie glownej funkcji

    # prezentowanie wynikow
    print("Macierz przydzialu zadan:", result_matrix, sep='\n', end='\n\n')
    print("Koszt: {}".format(cost))


if __name__ == "__main__":
    main()
