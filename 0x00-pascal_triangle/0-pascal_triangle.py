#!/usr/bin/python3

"""
pascal's triangle

"""


def pascal_triangle(n):

    """
    Create a function that returns
    a list of lists of integers
    representing the Pascal’s triangle of n
    """

    new_pascal = []

    """ Assumes that n is an integer """
    if n <= 0:
        return new_pascal

    for i in range(n):
        row_index = [1]
        if new_pascal:
            final_row = new_pascal[-1]
            row_index.extend([sum(pair) for pair in
                              zip(final_row, final_row[1:])])
            row_index.append(1)
        new_pascal.append(row_index)
    return (new_pascal)
