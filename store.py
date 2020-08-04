### =============== Categories ===============
class Catergory:
    def __init__(self, name, description, products):
        self.name = name
        self.description = description
        self.products = products

    def __str__(self):
        return f"{self.name}: {self.description}"

    def __repr__(self):
            return f"self.name = {self.name}, self.description = {self.description}, self.products = {self.products}"


# ======= Dictionaries? =======
hiking_category = Catergory("Hiking", "Long distance, Section, and Day hiking", [])
camping_category = Catergory("Camping", "Summer and Winter camping", [])
climbing_category = Catergory("Climbing", "Ropes and stuff", [])

sandwhich_category = Catergory("Sandwhich", "Vietnamese sandwhiches", [])
pho_category = Catergory("Pho", "Vietnamese Soup", [])
bear_liver_category = Catergory("Bear Liver", "Meat", [])



class Store:
    def __init__(self, name, catergories):
        self.name = name
        self.catergories = catergories

    def __str__(self):
        output = f"\nWelcome to {self.name}!"
        for catergory in self.catergories:
            output += f"\n {catergory}"
        return output

    def __repr__(self):
        return f"self.name = {self.name}, self.catergories = {self.catergories}"

### =============== Stores ===============
hiking_store = Store("Gander Mountain", [hiking_category, camping_category, climbing_category])
food_store = Store("Lee's Bakery", [sandwhich_category, pho_category, bear_liver_category])

print(hiking_store)
print(food_store)

# print(repr(hiking_category))
# print(repr(camping_category))





























# class Store:
#     def __init__(self, name, departments):
#         self.name = name
#         self.departments = departments

#     def print_welcome(self):
#         print(f"\n\nWelcome to {self.name}! Which department would you like to visit?")

#         for i in self.departments:
#             print(i)

# class Department:
#     def __init__(self, id,  name, products):
#         self.id = id
#         self.name = name
#         self.products = products

#     def __str__(self):
#         return f"{self.id}: {self.name}"


# store1 = Store("Manny's", [Department(1, "foods", []), Department(2, "cleaning", []), Department(3, "home", [])])

# while True:
#     store1.print_welcome()

#     selection = input("Which department would you like to visit? ")

#     if selection == "quit":
#         break

#     choosen_dept = store1.departments[int(selection)-1]

#     print(f"You picked the {choosen_dept.name} department")