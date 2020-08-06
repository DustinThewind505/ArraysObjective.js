### ==================== IMPORTS ====================
import random
import time

### ==================== VARIABLES ====================
my_range = 100
my_size = 15

random_nums = random.sample(range(my_range), my_size)

print(random_nums)


num_to_find = 14

# ========== LINEAR SEARCH *O(n) linear time* ==========
def linear_search(arr, target):
    for num in arr:
        if num == target:
            return True
    return False

random_nums.sort()
print(random_nums)

# ========== BINARY SEARCH ==========
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

print(binary_search(random_nums, 13))