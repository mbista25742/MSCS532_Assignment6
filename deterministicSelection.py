def median_of_medians(arr, k): 
    #Finds the k-th smallest element in an array using the deterministic Median of Medians algorithm.
    if len(arr) <= 5:
        # Base case: directly sort and return the k-th element
        return sorted(arr)[k]
    
    # Step 1: Divide the array into groups of 5
    sublists = [arr[i:i + 5] for i in range(0, len(arr), 5)]

    # Step 2: Find the median of each sublist
    medians = [sorted(sublist)[len(sublist) // 2] for sublist in sublists]

    # Step 3: Recursively find the median of medians
    pivot = median_of_medians(medians, len(medians) // 2)

    # Step 4: Partition the array around the pivot
    low = [x for x in arr if x < pivot]
    high = [x for x in arr if x > pivot]
    pivot_list = [x for x in arr if x == pivot]

    # Step 5: Determine which part to search
    if k < len(low):
        return median_of_medians(low, k)
    elif k < len(low) + len(pivot_list):
        return pivot_list[0]
    else:
        return median_of_medians(high, k - len(low) - len(pivot_list))

if __name__ == "__main__":
    arr = [12, 3, 5, 7, 19, 1, 1,1,10, 15, 8, 6, 4]
    #k is index based starting from 0
    k = 1
    print(f"The {k}-th smallest element is: {median_of_medians(arr, k)}")
