import random
from typing import List, Tuple
import numpy as np
# https://zasoby1.open.agh.edu.pl/dydaktyka/matematyka/c_badania_operacyjne/krok/krok8_03.html


def brzana(matrix: np.ndarray, N: int = None) -> List[Tuple[int, int]]:
    """
    Funkcja wyszukuje zera niezależne, N razy, losowo. Potem z tych N razy wybiera najlepszy output i go zwraca.

    :param matrix: np.ndarray - Zredukowana macierz kosztów.
    :param N: int - liczba przeszukiwań.
    :return: List[Tuple[int, int]] - lista krotek ze współrzędnymi zer niezależnych.
    """
    rows, cols = matrix.shape
    zeros = list()
    for i in range(rows):
        for j in range(cols):
            if matrix[i, j] == 0:   # Wyszukuje zera w macierzy.
                zeros.append((i, j))    # Zapisuję je do listy

    if N is None or N <= 0:   # Jak N jest niezdefiniowane albo źle zdefiniowane
        N = len(zeros)

    independent_zeros_set = list()
    for n in range(N):  # szukam zer niezależnych kilka razy
        random.shuffle(zeros)    # mieszam listę po to, żeby znaleźć różne listy zer niezależnych (super pomysł xD)

        independent_row = list()    # pomocnicza lista
        independent_col = list()    # pomocnicza lista
        independent_zeros = list()  # lista zer niezależnych
        for zero in zeros:
            if zero[0] not in independent_row and zero[1] not in independent_col:
                independent_row.append(zero[0])
                independent_col.append(zero[1])
                independent_zeros.append(zero)

        independent_zeros_set.append(independent_zeros)

    largest_zeros_list = list()    # Wybieram ten wariant, w którym mam najwięcej zer niezależnych i go zwracam.
    largest_list_size = 0
    for elem in independent_zeros_set:
        if len(elem) > largest_list_size:
            largest_zeros_list = elem
            largest_list_size = len(elem)

    return largest_zeros_list
