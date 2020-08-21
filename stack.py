### ==================== IMPORTS ====================
from singly_Linkedlist import Linkedlist

### ==================== THE STACK using a Linked List ====================
class Stack:
    def __init__(self):
        self.size = 0       # ========== Keeps track of length ==========
        self.storage = Linkedlist()


    def __len__(self):
        return self.size


    def __str__(self):
        return f'{self.storage}'


    def push(self, value):
        self.size += 1      # ========== Keeps track of length, adds 1 to length ==========
        self.storage.add_to_head(value)   # ========== ADDS to the front of the array ==========


    def pop(self):
        self.size -= 1      # ========== Keeps track of length, subtracts 1 from length ==========
        if self.size == 0:
            return None

        return self.storage.remove_head()  # ========== REMOVES to the front of the array ==========

# ========== Make a stack with using a Linked List ==========
new_stack = Stack()
new_stack.push(50)
print(new_stack)
new_stack.push(60)
print(new_stack)
new_stack.push(70)
print(new_stack)
new_stack.push(80)
print(new_stack)
new_stack.pop()
print(new_stack)






# ### ==================== THE STACK using a list/array ====================
# class Stack:
#     def __init__(self):
#         self.size = 0       # ========== Not needed in arrays ==========
#         self.storage = []


#     def __len__(self):
#         return self.size


#     def __str__(self):
#         return f'{self.storage}'


#     def push(self, value):
#         self.size += 1      # ========== Not needed in arrays ==========
#         self.storage.insert(0, value)   # ========== ADDS to the front of the array ==========


#     def pop(self):
#         self.size -= 1      # ========== Not needed in arrays ==========
#         if len(self.storage) == 0:
#             return None

#         return self.storage.pop(0)  # ========== REMOVES to the front of the array ==========


# ========== Make a stack with using a List/Array ==========
# new_stack = Stack()
# print(len(new_stack))
# new_stack.push(23)
# new_stack.push(24)
# new_stack.push(25)
# print(len(new_stack))
# print(new_stack.pop())
# print(new_stack)
