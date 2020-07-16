# x = 321
# y = 154323

# if x == y:
#     print(f'{x} and {y} are equal')
# else:
#     if x < y:
#         print(f'{x} is less than {y}')
#     else:
#         print(f'{x} is greater than {y}')

### ===================================== Lists(arrays) =====================================
# evens = []

# for i in range(501):
#     if i % 10 == 0:
#         evens.append(i)

# print(evens)

# ### ====== List Comprhension(short hand) ======
# odds = [i for i in range(501) if i % 30 == 0]

# print(odds)

### ===================================== Multiply =====================================
array = [1, 2, 3, 210]

def multiply2(int):
    return int*2

print(multiply2(210))

def listMultiply2(a):
    for i in range(len(a)):
        a[i] *= 2
    return a

print(listMultiply2(array))