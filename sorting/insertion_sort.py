"""
    Insertion Sort Algorithm

    Is an in-place comparison-based algorithm.

    For each position, swap the current element to its left
    while the left element is larger than the current element.
"""


def sort(array):
    for p in range(0, len(array)):
        current_element = array[p]

        while p > 0 and array[p - 1] > current_element:
            array[p] = array[p - 1]
            p -= 1

        array[p] = current_element
