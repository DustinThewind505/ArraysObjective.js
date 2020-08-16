### ======= Imports =======
from category import Category
from products import Sneakers

### ======= Categories/Dictionaries? =======
ugz = Sneakers("Ugzz", "49.99", "12", "Ugzz Boots")

hiking_category = Category("Hiking", "Long distance, Section, and Day hiking", [])
camping_category = Category("Camping", "Summer and Winter camping", [ugz])
climbing_category = Category("Climbing", "Ropes and stuff", [])

sandwhich_category = Category("Sandwhich", "Vietnamese sandwhiches", [])
pho_category = Category("Pho", "Vietnamese Soup", [])
bear_liver_category = Category("Bear Liver", "Meat", [])



class Store:
    def __init__(self, name, categories):
        self.name = name
        self.categories = categories

    def __str__(self):
        output = f"\nWelcome to {self.name}!"
        counter = 1
        for category in self.categories:
            output += f"\n {counter}. {category.name}"
            counter += 1
        return output

    def __repr__(self):
        return f"self.name = {self.name}, self.catergories = {self.catergories}"

### =============== Stores ===============
hiking_store = Store("Gander Mountain", [hiking_category, camping_category, climbing_category])
food_store = Store("Lee's Bakery", [sandwhich_category, pho_category, bear_liver_category])

#print(hiking_store)
#print(food_store)

# print(repr(hiking_category))
# print(repr(camping_category))



### =============== REPL <- READ EVALUATE PRINT LOOP ===============
choice = -1

print('Type "Q" to exit')
print(food_store)
# LOOP
while True:
    # READ
    choice = input("Please choose a category (#): ")
    try:
        # EVALUATE
        chosen_category = food_store.categories[int(choice) - 1]

        # PRINT
        print(chosen_category)

    # Error handling
    except IndexError:
        print("Please enter a valid number")
    except ValueError:
        print("Please enter a valid number")

    finally:
        # Exit program
        if (choice == "Q" or "q"):
            break




























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