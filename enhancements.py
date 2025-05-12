# enhancements.py
# Optional enhancements: Descending order sort and a stable version of Selection Sort

def selection_sort_desc(arr):
    """
    Sorts the input list in descending order using Selection Sort.
    """
    n = len(arr)
    for i in range(n):
        max_idx = i
        for j in range(i + 1, n):
            if arr[j] > arr[max_idx]:
                max_idx = j
        arr[i], arr[max_idx] = arr[max_idx], arr[i]
    return arr


def stable_selection_sort(arr):
    """
    Performs a stable selection sort (preserves the order of equal elements).
    This is done by inserting the minimum element at its correct position
    instead of swapping, which avoids reordering duplicates.
    """
    n = len(arr)
    for i in range(n - 1):
        # Find the minimum element and its index
        min_idx = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j

        # Extract the minimum value and shift elements to make space
        key = arr[min_idx]
        while min_idx > i:
            arr[min_idx] = arr[min_idx - 1]
            min_idx -= 1
        arr[i] = key

    return arr
