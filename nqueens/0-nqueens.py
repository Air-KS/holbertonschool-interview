#!/usr/bin/python3
""" Program that solves the N queens problem. """

import sys


def solveNQueens(n):
    """ Function that solves the N queens problem. """
    def could_place(board, row, col):
        """ Check if a queen could be placed on board[row][col]. """
        for i in range(row):
            if board[i] == col or abs(board[i] - col) == abs(i - row):
                return False
        return True

    def place_queen(board, row, n, result):
        """ Recursive function to solve N queens problem. """
        if row == n:
            result.append(board[:])
            return

        for col in range(n):
            if could_place(board, row, col):
                board[row] = col
                place_queen(board, row + 1, n, result)

    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        n = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    if n < 4:
        print("N must be at least 4")
        sys.exit(1)

    board = [-1] * n
    result = []
    place_queen(board, 0, n, result)
    return result


n = 0
result = solveNQueens(n)
for res in result:
    print([[i, j] for i, j in enumerate(res)])
