#!/usr/bin/python3
"""
Module which contains minoperations function
"""


def minOperations(n):
    """
    Calculates the fewest number of operations required to
    obtain exactly n 'H' characters in the file.

    Args:
    n (int): The target number of 'H' characters.

    Returns:
    int: The minimum number of operations needed.
    """

    # Comment
    if n <= 1:
        return 0

    # Comment
    operations = 0
    factor = 2

    # Comment
    while factor <= n:
        while n % factor == 0:
            operations += factor
            n //= factor
        factor += 1

    # omment
    return operations
