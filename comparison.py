import random
import time

# --- Median of Medians Algorithm (Deterministic) ---
def median_of_medians(arr, k):
    if len(arr) <= 5:
        return sorted(arr)[k]

    # Split arr into groups of 5
    groups = [arr[i:i + 5] for i in range(0, len(arr), 5)]

    # Find the medians of each group
    medians = [sorted(group)[len(group) // 2] for group in groups]

    # Recursively find the median of medians
    pivot = median_of_medians(medians, len(medians) // 2)

    # Partition the array around the pivot
    lows = [x for x in arr if x < pivot]
    highs = [x for x in arr if x > pivot]
    pivots = [x for x in arr if x == pivot]

    # Recursively select from the correct partition
    if k < len(lows):
        return median_of_medians(lows, k)
    elif k < len(lows) + len(pivots):
        return pivots[0]
    else:
        return median_of_medians(highs, k - len(lows) - len(pivots))

# --- Randomized Quickselect Algorithm (Randomized) ---
def randomized_quickselect(arr, k):
    if len(arr) == 1:
        return arr[0]
    
    pivot = random.choice(arr)
    lows = [x for x in arr if x < pivot]
    highs = [x for x in arr if x > pivot]
    pivots = [x for x in arr if x == pivot]

    if k < len(lows):
        return randomized_quickselect(lows, k)
    elif k < len(lows) + len(pivots):
        return pivots[0]
    else:
        return randomized_quickselect(highs, k - len(lows) - len(pivots))

# --- Helper Functions for Performance Testing ---
def measure_time(selection_algorithm, arr, k):
    start_time = time.time()
    selection_algorithm(arr, k)
    return time.time() - start_time

def generate_random_array(size):
    return [random.randint(0, 1000000) for _ in range(size)]

def generate_test_arrays(sizes):
    arrays = {}
    for size in sizes:
        arr = generate_random_array(size)
        arrays[size] = {
            "random": arr,
            "sorted": sorted(arr),
            "reverse_sorted": sorted(arr, reverse=True)
        }
    return arrays

# --- Performance Comparison ---
def compare_algorithms():
    sizes = [100, 1000, 10000, 100000, 1000000]
    test_arrays = generate_test_arrays(sizes)

    print(f"{'Size':<10}{'Algorithm':<20}{'Random Array Time (s)':<25}{'Sorted Array Time (s)':<25}{'Reverse-Sorted Array Time (s)'}")
    print("="*90)

    for size in sizes:
        for algorithm, algo_name in zip([median_of_medians, randomized_quickselect], ["Median of Medians", "Randomized Quickselect"]):
            random_time = measure_time(algorithm, test_arrays[size]["random"], size // 2)
            sorted_time = measure_time(algorithm, test_arrays[size]["sorted"], size // 2)
            reverse_sorted_time = measure_time(algorithm, test_arrays[size]["reverse_sorted"], size // 2)
            
            print(f"{size:<10}{algo_name:<20}{random_time:<25.6f}{sorted_time:<25.6f}{reverse_sorted_time:<25.6f}")

# Run the performance comparison
compare_algorithms()
