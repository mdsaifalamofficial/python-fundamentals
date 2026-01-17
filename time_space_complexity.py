# Time and Space Complexity

# O(1) - Constant Time
def get_first(arr):
    return arr[0]

# O(n) - Linear Time
def print_elements(arr):
    for i in arr:
        print(i)

# O(n^2) - Quadratic Time
def print_pairs(n):
    for i in range(n):
        for j in range(n):
            print(i, j)

# O(log n) - Logarithmic Time (Binary Search concept)
def binary_search_example(arr, target):
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1

    return -1

# Space Complexity examples

# O(1) space
total = 0
print(total)

# O(n) space
numbers = [1, 2, 3, 4]
print(numbers)
