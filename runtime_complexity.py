import math
from math import sqrt

### ====== LIST ======
items = ["a", "b", "c", "d", "e"]

### ======================= CONSTANT Time =======================
def print_one(list): # O(1) ==> reduces to O(1)
    print(f'\n{items[0]}\n')# O(1)*******************************

print_one(items)

### ======================= LINEAR Time =========================
def print_list(list): # O(n) + O(1) ==> reduces to O(n)
    # O(n) * O(1) = O(n)*****************************************
    for i in items: # O(n)
        print(i) # O(1)

print_list(items)

### ======================= QUADRATIC Time =======================
def print_loops(num): # O(1) + O(n^2) + O(1) ==> reduces to O(n^2)
    result = 0 # O(1)

    # O(n) * O(n) = O(n^2)****************************************
    for i in range(0, num): # O(n)
        # O(n) * O(1) = O(n)
        for j in range(0, num): # O(n)
            result += i * j # O(1)
    
    return result # O(1)

print(print_loops(3))