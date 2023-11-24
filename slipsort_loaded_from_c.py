import ctypes
import random

# Load the DLL
splitsort_lib = ctypes.CDLL('./splitsort.dll')

# Define the argument and return types of the C function
splitsort_lib.splitSort.argtypes = [ctypes.POINTER(ctypes.c_int), ctypes.c_int]
splitsort_lib.splitSort.restype = None

# Function to check if an array is sorted
def is_sorted(arr):
    return all(arr[i] <= arr[i+1] for i in range(len(arr)-1))

# Counter for successful sorts
successful_sorts = 0

# Test the sorting with 100 different arrays
for _ in range(100):
    # Create a random array of integers, each with size 20
    arr_type = ctypes.c_int * 20
    arr = arr_type(*[random.randint(0, 100) for _ in range(20)])

    # Print the original array
    print("Original array:", list(arr))

    # Call the C function to sort the array
    splitsort_lib.splitSort(arr, len(arr))

    # Convert the result back to a Python list
    sorted_arr = list(arr)

    # Print the sorted array
    print("Sorted array:", sorted_arr)

    # Check if the array is sorted
    if is_sorted(sorted_arr):
        print("The array is correctly sorted.")
        successful_sorts += 1
    else:
        print("Error: The array is not correctly sorted.")

# Check if all arrays were successfully sorted
if successful_sorts == 100:
    print("All 100 arrays were successfully sorted.")
else:
    print(f"Sorting failed for {100 - successful_sorts} out of 100 arrays.")
