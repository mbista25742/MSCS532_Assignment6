import random
def randomized_partition(arr, low, high):
   # Partitions the array around a randomly chosen pivot.
    # Randomly select a pivot index
    pivot_index = random.randint(low, high)
    # Move the pivot to the end
    arr[pivot_index], arr[high] = arr[high], arr[pivot_index]

    pivot = arr[high]
    i = low - 1  # Pointer for smaller elements

    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]  # Swap smaller element

    # Place pivot in the correct position
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1

def randomized_quickselect(arr, low, high, k):
    #Finds the k-th smallest element using Randomized Quickselect.
    if low == high:
        return arr[low]

    # Partition the array
    pivot_index = randomized_partition(arr, low, high)

    # Find the rank of the pivot
    rank = pivot_index - low + 1

    if rank == k:  # Pivot is the k-th smallest element
        return arr[pivot_index]
    elif k < rank:
        return randomized_quickselect(arr, low, pivot_index - 1, k)
    else:
        return randomized_quickselect(arr, pivot_index + 1, high, k - rank)

if __name__ == "__main__":
    arr = [12, 3, 5,5, 7, 19, 1, 10, 15, 8, 6,5, 4]
    #k is index based smalles element position
    k = 5
    print(f"The {k}-th smallest element is: {randomized_quickselect(arr, 0, len(arr) - 1, k)}")
