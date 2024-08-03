"""
This code tests and compares the performance of different sorting algorithms:
"""

import timeit
import random

def merge_sort(arr):
    """
    Perform merge sort.
    """
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left_half = arr[:mid]
    right_half = arr[mid:]

    return merge(merge_sort(left_half), merge_sort(right_half))

def merge(left, right):
    """
    Merge two sorted lists into one sorted list.
    """
    merged = []
    left_index = 0
    right_index = 0

    while left_index < len(left) and right_index < len(right):
        if left[left_index] <= right[right_index]:
            merged.append(left[left_index])
            left_index += 1
        else:
            merged.append(right[right_index])
            right_index += 1

    while left_index < len(left):
        merged.append(left[left_index])
        left_index += 1

    while right_index < len(right):
        merged.append(right[right_index])
        right_index += 1

    return merged

def insertion_sort(lst):
    """
    Perform insertion sort.
    """
    for i in range(1, len(lst)):
        key = lst[i]
        j = i - 1
        while j >= 0 and key < lst[j]:
            lst[j + 1] = lst[j]
            j -= 1
        lst[j + 1] = key
    return lst

def timsort(arr):
    """
    Perform Timsort.
    """
    arr.sort()

def generate_data(size):
    """
    Generate a list of random integers.
    """
    return [random.randint(0, 10000) for _ in range(size)]

def measure_time(algorithm, sizes):
    """
    Measure the execution time of the a sorting algorithm on different sizes.
    """
    for size in sizes:
        data = generate_data(size)
        time_taken = timeit.timeit(lambda: algorithm(data.copy()), number=1)
        print(f"Size {size}: {time_taken:.5f} seconds")

def main():
    """
    Main function.
    """
    sizes = [100, 1000, 5000, 10000]

    print("Testing merge_sort")
    measure_time(merge_sort, sizes)

    print("\nTesting insertion_sort")
    measure_time(insertion_sort, sizes)

    print("\nTesting timsort")
    measure_time(timsort, sizes)

if __name__ == "__main__":
    main()
