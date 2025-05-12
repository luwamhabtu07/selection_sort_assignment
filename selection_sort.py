def selection_sort(arr):
    """
    Sorts the input list in ascending order using Selection Sort algorithm.
    """
    n = len(arr)
    for i in range(n):
        # Assume the current index is the smallest
        min_idx = i
        for j in range(i + 1, n):
            # Find index of the smallest element in the rest of the array
            if arr[j] < arr[min_idx]:
                min_idx = j
        # Swap the found minimum element with the element at index i
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr
