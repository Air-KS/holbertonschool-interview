#!/usr/bin/python3

import sys


def is_safe(board, row, col):
    for i in range(col):
        if board[i] == row or \
           board[i] - i == row - col or \
           board[i] + i == row + col:
            return False
    return True


def solve_n_queens_util(board, col, n, solutions):
    if col == n:
        solutions.append(list(board))
        return

    for row in range(n):
        if is_safe(board, row, col):
            board[col] = row
            solve_n_queens_util(board, col + 1, n, solutions)


def solve_n_queens(n):
    if not isinstance(n, int):
        print("N must be a number")
        sys.exit(1)

    if n < 4:
        print("N must be at least 4")
        sys.exit(1)

    board = [-1] * n
    solutions = []
    solve_n_queens_util(board, 0, n, solutions)

    for solution in solutions:
        print([[i, solution[i]] for i in range(n)])


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        n = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    solve_n_queens(n)
