class Node:
    def __init__(self, value =None, next_node=None):
        self.value = value
        self.next_node = next_node

    def get_value(self):
        return self.value

    def get_next(self):
        return self.next_node

    def set_next(self, new_next):
        self.next_node = new_next

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def add_to_tail(self, value):
        new_node = Node(value, None)

        if not self.head:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.set_next(new_node)
            self.tail = new_node
    
    def remove_head(self, index)
        if not self.head:
            return None
        if not self.head.get_next:
            head = self.headself
            self.head = None
            self.tail = None
            return head.get_value
        value = self.head.get_value
        self.head = self.head.get_next

    def get_max(self):
        if not self.head:
            return None

        current = self.head
        max_val = self.head.value
        while current:
            if current.value > max_val:
                max_val = current.value
            current = current.next_node
        return max_val


      











# ll = Node(1)
# ll.next = Node(2)
# ll.next.next = Node(3)
# ll.next.next.next = Node(4)
# ll.next.next.next.next = Node(5)

# print(ll.value)
