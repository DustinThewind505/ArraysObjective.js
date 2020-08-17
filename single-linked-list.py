class Node:
    def __init__(self, value=None, next_node=None):
        self.value = value
        self.next_node = next_node


class Linkedlist:
    def __init__(self):
        self.head = None    # ===== First Node =====
        self.tail = None    # ===== Last Node =====
    

    def add_to_head(self, value):
        new_node = Node(value)  # ===== Create a node to add =====

        if self.head is None and self.tail is None:     # ===== Check if empty =====
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next_node = self.head  # ===== Point new node to current head =====
            self.head = new_node    # ===== Then change the head to the new node =====
    

    def add_to_tail(self, value):
        new_node = Node(value)  # ===== Create a node to add =====

        if self.head is None and self.tail is None: # ===== Check if empty =====
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next_node = new_node  # ===== Point current tail to new node =====
            self.tail = new_node    # ===== Then change the tail to the new node =====


    def remove_head(self):
        if not self.head:   # ===== Check if empty =====
            return None

        if self.head.next_node is None: # ===== If the list only has one node, set the head and tail to None =====
            head_value = self.head.value
            self.head = None
            self.tail = None
            return head_value

        head_value = self.head.value
        self.head = self.head.next_node
        return head_value


    def contains(self, value):
        if self.head is None:
            return False

        current_node = self.head

        while current_node is not None:
            if current_node.value == value:
                return True
            current_node = current_node.next_node
        
        return False


linked_list = Linkedlist()
linked_list.add_to_head(0)
linked_list.add_to_tail(1)
print(linked_list.contains(1))
print(linked_list.contains(2))





































# class Node:
#     def __init__(self, value =None, next_node=None):
#         self.value = value
#         self.next_node = next_node

#     def get_value(self):
#         return self.value

#     def get_next(self):
#         return self.next_node

#     def set_next(self, new_next):
#         self.next_node = new_next

# class LinkedList:
#     def __init__(self):
#         self.head = None
#         self.tail = None

#     def add_to_tail(self, value):
#         new_node = Node(value, None)

#         if not self.head:
#             self.head = new_node
#             self.tail = new_node
#         else:
#             self.tail.set_next(new_node)
#             self.tail = new_node
    
#     def remove_head(self, index)
#         if not self.head:
#             return None
#         if not self.head.get_next:
#             head = self.headself
#             self.head = None
#             self.tail = None
#             return head.get_value
#         value = self.head.get_value
#         self.head = self.head.get_next

#     def get_max(self):
#         if not self.head:
#             return None

#         current = self.head
#         max_val = self.head.value
#         while current:
#             if current.value > max_val:
#                 max_val = current.value
#             current = current.next_node
#         return max_val


      











# # ll = Node(1)
# # ll.next = Node(2)
# # ll.next.next = Node(3)
# # ll.next.next.next = Node(4)
# # ll.next.next.next.next = Node(5)

# # print(ll.value)
