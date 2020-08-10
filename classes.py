### ============ Classes ============
class Bicycle():
    def __init__(self, number_of_wheels, description):
        self.number_of_wheels = number_of_wheels
        self.description = description

    def __str__(self):
        print(f"Has this many wheels: {self.number_of_wheels}\n{self.description}")


    def wipeout(self):
        print("WIPEOUT!")

class Unicycle(Bicycle):
    def __init__(self, number_of_wheels, description, bounceyness):
        super().__init__(number_of_wheels, description)
        self.bounceyness = bounceyness

### ============ Using Classes ============
mountain_bike = Bicycle(2, "Can go up and down dirt trails")
stunt_unicycle = Unicycle(1, "You can juuggle while you ride", "Very Bouncey")

# mountain_bike.wipeout()
# stunt_unicycle.wipeout()

# print(mountain_bike.number_of_wheels)
# print(stunt_unicycle.number_of_wheels)
# print(mountain_bike)
print(stunt_unicycle.number_of_wheels)
print(stunt_unicycle.description)
print(stunt_unicycle.bounceyness)