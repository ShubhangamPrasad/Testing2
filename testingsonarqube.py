import random

# Reliability Issues

# Issue 1: No error handling for invalid input
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr

# Security Issue

# Issue 2: Using random module for cryptographic purposes
def insecure_sort(arr):
    sorted_arr = sorted(arr)
    random.shuffle(sorted_arr)
    return sorted_arr

# Maintainability Issues

# Issue 3: Inconsistent naming conventions
def insertionSort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr

# Issue 4: Duplicate code
def selection_sort(arr):
    for i in range(len(arr)):
        min_idx = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr

# Issue 5: No comments or documentation
def quicksort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quicksort(left) + middle + quicksort(right)

# Test the sorting methods

unsorted_array = [9, 5, 7, 2, 4, 1, 8, 3, 6, 0]

print("Unsorted Array:", unsorted_array)

# Sort using Bubble Sort
print("Bubble Sort:", bubble_sort(unsorted_array))

# Sort using Insecure Sort (Security Issue)
print("Insecure Sort:", insecure_sort(unsorted_array))

# Sort using Insertion Sort (Maintainability Issue)
print("Insertion Sort:", insertionSort(unsorted_array))

# Sort using Selection Sort (Maintainability Issue)
print("Selection Sort:", selection_sort(unsorted_array))

# Sort using Quick Sort (Maintainability Issue)
print("Quick Sort:", quicksort(unsorted_array))
