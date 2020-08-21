class Node:
    def __init__(self, value=None, next_node=None):
        self.value = value
        self.next_node = next_node

    def get_value(self):
        return self.value

    def get_next(self):
        return self.next_node

    def set_next(self, new_next):
    # set this node's next_node reference to the passed in node
        self.next_node = new_next
    

class Linkedlist:
    def __init__(self):
        self.head = None    # ===== First Node =====
        self.tail = None    # ===== Last Node =====

    def __str__(self):
        output = ''
        current_node = self.head
        while current_node is not None:
            output += f'{current_node.value}--> '
            current_node = current_node.next_node
        return output
    

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

def print_ll_elements(self):
        current = self.head

        while current is not None:
            print(current.value)
            current = current.get_next()        


# linked_list = Linkedlist()
# linked_list.add_to_head(0)
# linked_list.add_to_tail(1)
# print(linked_list)
