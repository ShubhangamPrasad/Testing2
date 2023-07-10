import secrets
from typing import List

def bubble_sort(arr: List[int])-> List[int]:
    """
    Sorts a list of integers in ascending order using Bubble Sort.

    Parameters:
        arr (List[int]): The list of integers to sort.

    Returns:
        List[int]: The sorted list of integers.
    """
    try:
        n = len(arr)
        for i in range(n):
            for j in range(n - i - 1):
                if arr[j] > arr[j + 1]:
                    arr[j], arr[j + 1] = arr[j + 1], arr[j]
        return arr
    except Exception as e:
        print(f"An error occurred: {e}")
        return []

def secure_sort(arr: List[int])-> List[int]:
    """
    Sorts a list of integers in ascending order and then shuffles it.

    The shuffle method is used for cryptographic purposes, therefore using
    the secrets module to ensure true randomness.

    Parameters:
        arr (List[int]): The list of integers to sort.

    Returns:
        List[int]: The sorted and then shuffled list of integers.
    """
    arr = sorted(arr)
    arr = list(secrets.SystemRandom().shuffle(arr))
    return arr

def insert_sort(arr: List[int])-> List[int]:
    """
    Sorts a list of integers in ascending order using Insertion Sort.

    Parameters:
        arr (List[int]): The list of integers to sort.

    Returns:
        List[int]: The sorted list of integers.
    """
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr

def selection_sort(arr: List[int])-> List[int]:
    """
    Sorts a list of integers in ascending order using Selection Sort.

    Parameters:
        arr (List[int]): The list of integers to sort.

    Returns:
        List[int]: The sorted list of integers.
    """
    for i in range(len(arr)):
        min_idx = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr

def quick_sort(arr: List[int])-> List[int]:
    """
    Sorts a list of integers in ascending order using Quick Sort.

    Parameters:
        arr (List[int]): The list of integers to sort.

    Returns:
        List[int]: The sorted list of integers.
    """
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)