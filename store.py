
class Store:
    def __init__(self, name, catergories):
        self.name = name
        self.catergories = catergories

    def __str__(self):
        return f"Welcome to {self.name}, here are the catergories {self.catergories}"

    def __repr__(self):
        return f"self.name = {self.name}, self.catergories = {self.catergories}"

hiking_store = Store("Gander Mountain", ["Hiking", "Camping", "Climbing"])
food_store = Store("Lee's Bakery", ["Sandwhich", "Pho", "Bear Liver"])
print(repr(hiking_store))
print(repr(food_store))
































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