### ================== Python LIST Basics ==================
# ====== Variables ======
array = ["Bob", "Linda", "Gene", "Mr. Fishowner", "Tina"]

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
    #print(f'{len(arr)}\n')

# ============ PUT ============
def change_Bob(arr, str):
    arr[0] = str


# ============ DELETE ============
def delete_Bob(arr):
    del arr[0]
    print(arr)
    print(f'{len(arr)}\n')
       


### ================== Printing ==================
# use_Bob(55)

# get_Bob(array)

add_Bob(array, "tammy")

# change_Bob(array, "Teddy")

# get_Bob_by_index(array, 0)

# delete_Bob(array)


### ================== ENUMERATION ==================
for (index, element) in enumerate(array):
    print(f'Element {index} is {element}')
    #print(f'Element {index} is {array[index]}')

# ============ Change Array ============
change_Bob(array, "Teddy")
get_Bob(array)

### ================== List comprehensions ==================
# numbers = [1, 4, 9, 16, 25]

# # Create a new list of sqaured numbers from numbers list
# squared = []

# # Regular
# for num in numbers:
#     squared.append(num * num)

# print(squared)

# # or return statement with for loop inside of empty array

# cooler_squared = [num * num for num in numbers]

# print(cooler_squared)

# # or return statement with for loop inside of empty array with conditional

# evens = [num for num in numbers if num % 2 == 0]

# print(evens)

# # or return statement with for loop inside of empty array with conditional + functions on elements in the for loop

# named_T = [name.capitalize() for name in array if name[0].lower() == "t"]

# print(named_T)