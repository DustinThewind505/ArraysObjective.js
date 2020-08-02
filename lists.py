### ================== Python LIST Basics ==================
# ====== Variables ======
array = ["Bob", "Linda", "Gene", "Mr. Fishowner"]

name = "Bob"
age = 42

# ============ Sample Function ============
def use_Bob(num):
    if num >= 55:
        print(f'\n{name} is {str(age)}\n')
    else:
        print('Need a bigger number')


### ================== CRUD Functions ==================
# ============ GET ============
def get_Bob(arr):
    print(arr)
    print(f'{len(arr)}\n')

# ============ GET by id ============
def get_Bob_by_index(arr, num):
    print(f'{arr[num]}\n')

# ============ POST ============
def add_Bob(arr, str):
    array.append(str)
    print(array)
    print(f'{len(arr)}\n')

# ============ PUT ============

# ============ DELETE ============
def delete_Bob(arr):
    del arr[0]
    print(arr)
    print(f'{len(arr)}\n')
       


### ================== Printing ==================
# use_Bob(55)

# get_Bob(array)

# add_Bob(array, "Tammy")

# get_Bob_by_index(array, 0)

# delete_Bob(array)

for (index, element) in enumerate(array):
    print(f'Element {index} is {element}')
    #print(f'Element {index} is {array[index]}')



### ================== List comprehensions ==================
numbers = [1, 4, 9, 16, 25]

# Create a new list of sqaured numbers from numbers list
squared = []

for num in numbers:
    squared.append(num * num)

print(squared)

# or

cooler_squared = [num * num for num in numbers]

print(cooler_squared)