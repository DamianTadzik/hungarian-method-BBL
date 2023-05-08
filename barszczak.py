# Algorym wykreslania zer macierzy minimalna liczba linii
from typing import List, Tuple, Union, Optional

import numpy as np


def barszczak(matrix: List[List[int]], ind_zeros: List[Tuple[int, int]], lower_bound):
    dep_zeros = [] # zera zalezne
    ind_zeros_row = [ind_zeros[i][0] for i in range(0, len(ind_zeros))] # pomocnicza lista zer niezaleznych, indeksy wierszow
    marked_rows = [i for i in range(0, len(matrix)) if not i in ind_zeros_row] # oznaczone wierze
    marked_cols = [] # oznaczone kolumny
    old_size_row = 0
    old_size_col = 0

    # szukanie zer zaleznych
    for i in range(len(matrix)):
        for j in range(len(matrix)):
            if matrix[i][j] == 0 and not (i, j) in ind_zeros:
                dep_zeros.append((i, j))

    # petla znakujaca wiersze i kolumny
    while old_size_row != len(marked_rows) or old_size_col != len(marked_cols):
        old_size_row = len(marked_rows)
        old_size_col = len(marked_cols)

        for i in marked_rows:
            for j in range(len(matrix)):
                if (i, j) in dep_zeros and not j in marked_cols:
                    marked_cols.append(j)

        for i in ind_zeros_row:
            for j in marked_cols:
                if (i, j) in ind_zeros and not i in marked_rows:
                    marked_rows.append(i)

    non_marked_rows = [i for i in range(0, len(matrix)) if not i in marked_rows] # nieoznaczone wiersze

    if len(non_marked_rows) + len(marked_cols) == len(matrix): # sprawdzanie czy znaleziono minimalne pokrycie dla wymiaru macierzy
        return matrix, lower_bound, True

    # szukanie najmniejszego nieprzekrytego elementu w macierzy
    min_value = np.inf
    for i in range(len(matrix)):
        for j in range(len(matrix)):
            if matrix[i][j] < min_value and not i in non_marked_rows and not j in marked_cols:
                min_value = matrix[i][j]

    # dodawanie i odejmowanie najmniejszego elementu w zaleznosci od pokrycia
    for i in range(len(matrix)):
        for j in range(len(matrix)):
            if not i in non_marked_rows and not j in marked_cols:
                matrix[i][j] -= min_value
            elif i in non_marked_rows and j in marked_cols:
                matrix[i][j] += min_value

    # zwiekaszanie kosztu (lower bound) w zaleznosci od krotnosci
    for i in range(len(matrix)):
        for j in range(len(matrix)):
            if matrix[i][j] == min_value and not i in non_marked_rows and not j in marked_cols:
                lower_bound += 1

    return matrix, lower_bound, False
