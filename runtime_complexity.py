### ====== LIST ======
items = ["a", "b", "c", "d", "e"]

### ======================= CONSTANT Time =======================
def print_one(list):
    print(f'\n{items[0]}\n')

print_one(items)

### ======================= LINEAR Time =======================
def print_list(list):
    for i in items:
        print(i)

print_list(items)

### ======================= QUADRATIC Time =======================
