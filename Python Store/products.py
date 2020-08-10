### ============ Classes ============
class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price
    
    def __str__(self):
        print(f"{self.name}: ${self.price}")


class Sneakers(Product):
    def __init__(self, name, price, shoe_size, brand):
        super().__init__(name, price)
        self.shoe_size = shoe_size
        self.brand = brand



### ============ Using Classes ============
ugz = Sneakers("Ugzz", "49.99", "12", "Ugzz Boots")

print(ugz.name)
print(ugz.price)
print(ugz.shoe_size)
print(ugz.brand)