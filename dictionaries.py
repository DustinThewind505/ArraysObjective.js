### ================== Python DICTIONARIES Basics ==================
# ====== Variables ======
object = {
    "Co-Owner1": "Bob"
    }

name = "Linda"
age = 33

# ============ Sample Function ============
def add_Linda(obj):
    #print(f'\n{obj}')
    obj["Co-Owner2"] = name
    #print(f'{obj}\n')

add_Linda(object)

### ================== CRUD Functions ==================
# ============ GET ============
def get_Family(obj):
    print(f'\n{obj}\n')
    

# ============ GET by key ============
def get_Bob_by_key(obj, str):
    print(obj[str])
    

# ============ POST ============
def add_fam(obj, role, name):
    obj[role] = name
    print(f'\n{obj}\n')


# ============ PUT ============
def change_fam(obj, role, name):
    obj[role] = name


# ============ DELETE ============
def delete_Bob(obj):
    del obj["Co-Owner1"]
    print(obj)
       


### ================== Printing ==================
#get_Family(object)

#get_Bob_by_key(object, "Co-Owner1")

add_fam(object, "Waitress", "Tina")

#change_fam(object, "Waitress", "Gene")

#delete_Bob(object)

# ============ Looping ============
for key, value in object.items():
    print(f'{key} : {value}\n')

# ============ Check if exists ============
print("Jimmy Pesto" in object.values())
print("Tina" in object.values())


# ============ Change Object ============
change_fam(object, "Waitress", "Gene")

for key, value in object.items():
    print(f'{key} : {value}\n')