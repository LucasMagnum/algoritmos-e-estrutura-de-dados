"""
    Selection Sort Algorithm

    Is an algorithm known for its simplicity.

    The algorithm divides the input into two parts: the sublist of items
    already sorted, which is built up from the left to right at the front(left)
    of the list, and the sublist of items remaining to be sorted that occupy the
    rest of the list.

    The algorithm proceeds by finding the smallest element in the unsorted sublist,
    exchanging it with the leftmost unsorted element.
"""


def sort(array):
    for index in range(0, len(array)):
        min_index = index

        for right in range(index + 1, len(array)):
            if array[right] < array[min_index]:
                min_index = right

        array[index], array[min_index] = array[min_index], array[index]
