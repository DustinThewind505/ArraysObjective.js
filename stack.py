class Stack:
    def __init__(self):
        self.size = 0       # ========== Not needed in arrays ==========
        self.storage = []


    def __len__(self):
        return self.size


    def __str__(self):
        return f'{self.storage}'


    def push(self, value):
        self.size += 1      # ========== Not needed in arrays ==========
        self.storage.insert(0, value)   # ========== ADDS to the front of the array ==========


    def pop(self):
        self.size -= 1      # ========== Not needed in arrays ==========
        if len(self.storage) == 0:
            return None

        return self.storage.pop(0)  # ========== REMOVES to the front of the array ==========



new_stack = Stack()
print(len(new_stack))
new_stack.push(23)
new_stack.push(24)
new_stack.push(25)
print(len(new_stack))
print(new_stack.pop())
print(new_stack)
