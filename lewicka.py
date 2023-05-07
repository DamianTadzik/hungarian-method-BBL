from typing import List


def lewicka(matrix) -> List[List]:
    sum_reduction = 0
    for row in range(len(matrix)):
        min_value = min(matrix[row])
        sum_reduction += min_value
        for col in range(len(matrix)):
            matrix[row][col] -= min_value

    return matrix, sum_reduction  # macierz, dolne ograniczenie
