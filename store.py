class Store:
    def __init__(self, name, departments):
        self.name = name
        self.departments = departments

    def print_welcome(self):
        print(f"\n\nWelcome to {self.name}! Which department would you like to visit?")

        for i in self.departments:
            print(i)

class Department:
    def __init__(self, id,  name, products):
        self.id = id
        self.name = name
        self.products = products

    def __str__(self):
        return f"{self.id}: {self.name}"


store1 = Store("Manny's", [Department(1, "foods", []), Department(2, "cleaning", []), Department(3, "home", [])])

while True:
    store1.print_welcome()

    selection = int(input("Which department would you like to visit? "))

    if selection == "quit":
        break

    choosen_dept = store1.departments[selection-1]

    print(f"You picked the {choosen_dept.name} department")