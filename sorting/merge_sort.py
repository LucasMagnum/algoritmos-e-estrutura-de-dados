"""
    Merge Sort Algorithm

    Is an algorithm created by John Von Neumann in 1945.
    It uses the technique called Divide and Conquer to approach
    sorting problem.

    It is an algorithm used in many programming languages to sort
    huge amount of data.
"""


def sort(array):
    aux = array[:]
    sort_half(array, aux, 0, len(array) - 1)


def sort_half(array, aux, start, end):
    if start >= end:
        return

    middle = (start + end) // 2

    sort_half(array, aux, start, middle)
    sort_half(array, aux, middle + 1, end)

    merge(array, aux, start, end)


def merge(array, aux, start, end):
    left = start
    left_end = (start + end) // 2

    right = left_end + 1
    right_end = end

    for position in range(start, end + 1):
        #  There's no left element to be processed
        if left > left_end:
            aux[position] = array[right]
            right += 1

        #  There's no right element to be processed
        elif right > right_end:
            aux[position] = array[left]
            left += 1

        #  Compare left with right
        elif array[left] < array[right]:
            aux[position] = array[left]
            left += 1

        else:
            aux[position] = array[right]
            right += 1

    for k in range(start, end + 1):
        array[k] = aux[k]



import random
array = [random.randint(0, 100) for i in range(1000000)]
copy = array[:]
import time

start = time.time()
sort(array)
end = time.time()
print(end - start)

assert array == sorted(copy)
