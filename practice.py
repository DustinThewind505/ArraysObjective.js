### ==================== Practice ====================
# ========== Arrays ==========
array = ['Slipknot', 'Korn', 'Limp Bizkit', '311', 'Pantera']

# ===== CRUD =====
# == GET ==
def get_bands(arr):
    print(f'\n{arr}\n')

def get_bands_by_id(arr, num):
    print(f'\n{arr[num]}\n')

# == POST ==
def add_band(arr, str):
    arr.append(str)
    print(f'\n{arr}\n')

# == PUT ==
def edit_list(arr, num, str):
    arr[num] = str
    print(f'\n{arr}\n')

get_bands(array)

get_bands_by_id(array, 0)

add_band(array, "Sublime")

edit_list(array, 4, "Rob Zombie")