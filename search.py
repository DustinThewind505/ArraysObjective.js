import random
import time
my_range = 100
my_size = 15
nums = list(range(0, my_size))
shuffled_nums = list(range(0, my_size))
random.shuffle(shuffled_nums)

print(nums)
print(shuffled_nums)

num_to_find = 14

# ========== O(n) LINEAR TIME ==========
def linear_search(arr, target):
    for num in arr:
        if num == target:
            return True
    return False


print(linear_search(nums, num_to_find))
print(linear_search(shuffled_nums, 33))