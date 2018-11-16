"""
    Bubble Sort Algorithm

    Best case:
        - Nearly sorted arrays

    Pratical use:
        - No

    Created: ~1950
    Also known by: Sinking Sort, Exchange Sort
"""


def sort(array):

    for final in range(len(array), 0, -1):
        exchanging = False

        for current in range(0, final - 1):
            if array[current] > array[current + 1]:
                array[current + 1], array[current] = array[current], array[current + 1]
                exchanging = True

        if not exchanging:
            break
