import random

def split_sort(arr):
    n = len(arr)
    if n <= 1:
        return arr

    split_point = max(1, n // 3)  # Ensure at least one element in the left part
    left, right = arr[:split_point], arr[split_point:]

    # Sorting the smaller part using insertion sort
    insertion_sort(left)

    # Sorting the larger part using split_sort, with added base case check
    if len(right) > 1:
        right = split_sort(right)

    # Merging both parts
    return merge(left, right)

def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

def merge(left, right):
    merged = []
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            j += 1

    merged.extend(left[i:])
    merged.extend(right[j:])

    return merged

# Example usage
arr = [random.randint(0, 100) for _ in range(10)]
print("Original array:", arr)
sorted_arr = split_sort(arr)
print("Sorted array:", sorted_arr)
