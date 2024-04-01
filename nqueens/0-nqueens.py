#!/usr/bin/python3
"""
    N-queen problem
    The next algo solve any N queen in any NxN
    Being N > 3
"""
import sys


def n_q(t_arr, arr, col, index, n):
    """
       n_q - Find all posibles solution for N-queen problem and return it
             in a list
       @t_arr: temporaly list to store the all points of a posible solution
       @arr: store all the solution
       @col: save a colum use for a queen
       @i: the row of the chess table
       @n: Number of queens
    """
    if (index > n):
        arr.append(t_arr[:])
        return arr

    for j in range(n + 1):
        if index == 0 or ([index - 1, j - 1] not in t_arr and
                      [index - 1, j + 1] not in t_arr and
                      j not in col):
            if index > 1:
                dia = 0
                for k in range(2, index + 1):
                    if ([index - k, j - k] in t_arr) or ([index - k, j + k] in t_arr):
                        dia = 1
                        break
                if dia:
                    continue
            t_arr.append([index, j])
            col.append(j)
            n_q(t_arr, arr, col, index + 1, n)
            col.pop()
            t_arr.pop()

    return arr

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        exit(1)

    try:
        n = int(sys.argv[1])
    except:
        print("N must be a number")
        exit(1)

    if not isinstance(n, int):
        print("N must be a number")
        exit(1)

    elif n < 4:
        print("N must be at least 4")
        exit(1)

    n_q_arr = n_q([], [], [], 0, n - 1)
    for index in n_q_arr:
        print(index)
