### ==================== IMPORTS ====================
from singly_Linkedlist import Linkedlist

### ==================== A QUEUE using a Linked List ====================
class Queue:
    def __init__(self):
        self.size = 0
        self.storage = Linkedlist()

    def __len__(self):
        return self.size

    def enqsueue(self, value):
        self.size += 1
        self.storage.add_to_tail(value)

    def dequeue(self):
        if self.size == 0:
            return None
        self.size -= 1
        return self.storage.remove_head()





# ========== Make a QUEUE with using a Linked List ==========