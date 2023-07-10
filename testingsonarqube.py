import random
import secrets

# Bubble sort function
def bubble_sort(arr):
    # Check if the arguments are valid
    if not isinstance(arr, list):
        raise ValueError("Invalid input. Expected a list.")

    n = len(arr)
    for i in range(n):
        for j in range(n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr

def secure_sort(arr):
    sorted_arr = sorted(arr)
    secrets.SystemRandom().shuffle(sorted_arr)
    return sorted_arr

def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr

def selection_sort(arr):
    for i in range(len(arr)):
        min_idx = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i] = arr[min_idx]
    return arr

# Quick sort function
def quick_sort(arr):
    """
    This function sorts an array using the quick sort method.
    :param arr: list of numbers
    :return: sorted list of numbers
    """
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)


unsorted_array = [9, 5, 7, 2, 4, 1, 8, 3, 6, 0]

print("Unsorted Array:", unsorted_array)

print("Bubble Sort:", bubble_sort(unsorted_array))

print("Secure Sort:", secure_sort(unsorted_array))

print("Insertion Sort:", insertion_sort(unsorted_array))

print("Selection Sort:", selection_sort(unsorted_array))

print("Quick Sort:", quick_sort(unsorted_array))