"""
    Merge Sort Algorithm

    Is an algorithm created by John Von Neumann in 1945.
    It uses the technique called Divide and Conquer to approach
    sorting problem.

    It is an algorithm used in many programming languages to sort
    huge amount of data.
"""


def sort(array):
    sort_half(array, 0, len(array) - 1)


def sort_half(array, start, end):
    if start >= end:
        return

    middle = (start + end) // 2

    sort_half(array, start, middle)
    sort_half(array, middle + 1, end)

    merge(array, start, end)


def merge(array, start, end):
    array[start: end + 1] = sorted(array[start: end + 1])
