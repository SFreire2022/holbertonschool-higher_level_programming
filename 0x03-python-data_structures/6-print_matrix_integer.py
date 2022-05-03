#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for i in matrix[0:]:
        sep = ""
        for j in i[0:]:
            print(f"{sep:s}{j:d}", end="")
            sep = " "
        print()
