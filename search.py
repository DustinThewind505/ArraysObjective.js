### ==================== IMPORTS ====================
import random
import time

### ==================== VARIABLES ====================
my_range = 1000
my_size = 100

random_nums = random.sample(range(my_range), my_size)

print(random_nums)


num_to_find = 14

# ========== LINEAR SEARCH *O(n) linear time* ==========
def linear_search(arr, target):
    for num in arr:
        if num == target:
            return True
    return False

print("Linear")
start = time.time()
print(linear_search(random_nums, num_to_find))
end = time.time()
print(f"Runtime: {end - start}")

# ========== BINARY SEARCH *O(log n) logarithmic time*==========
def binary_search(arr, target):
    start = 0
    end = (len(arr) - 1)

    found = False
    while end >= start and not found:
        middle_index = (start + end) // 2
        if arr[middle_index] == target:
            found = True
        else:
            if target < arr[middle_index]:
                end = middle_index - 1
            if target > arr[middle_index]:
                start = middle_index + 1

    return found

print("Binary")
start = time.time()
random_nums.sort()
print(binary_search(random_nums, num_to_find))
end = time.time()
print(f"Runtime: {end - start}")