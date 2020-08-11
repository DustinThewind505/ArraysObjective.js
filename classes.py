### ============ Classes ============
class Bicycle():
    def __init__(self, number_of_wheels, description):
        self.number_of_wheels = number_of_wheels
        self.description = description

    def __str__(self):
        return f"\nHas this many wheels: {self.number_of_wheels}\n{self.description}"


    def wipeout(self):
        print("WIPEOUT!")

class Unicycle(Bicycle):
    def __init__(self, number_of_wheels, description, bounceyness):
        super().__init__(number_of_wheels, description)
        self.bounceyness = bounceyness
    
    def __str__(self):
        parent_str = super().__str__()
        return f"{parent_str}: This thing is {self.bounceyness}!"

### ============ Using Classes ============
mountain_bike = Bicycle(2, "Can go up and down dirt trails")
stunt_unicycle = Unicycle(1, "You can juggle while you ride", "Very Bouncey")

# mountain_bike.wipeout()
# stunt_unicycle.wipeout()


print(mountain_bike)
print(stunt_unicycle)
