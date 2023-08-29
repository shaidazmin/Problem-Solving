class Node:
    def __init__(self, data):
        self.data = data
        self.ref = None

node1 = Node(10)
# print(node1)

class LinkedList:
    def __init__(self) -> None:
        self.head = None
    def print_ll(self):
        if self.head is None:
            print("Linked List is empty")
        else:
            n = self.head
            while n is not None:
                print(n.data)
                n = n.ref
    def add_begin(self, data):
        new_node = Node(data)
        new_node.ref = self.head
        self.head = new_node   

    def add_end(self, data):
        new_node = Node(data)   
        if self.head is None:
            self.head 







LL1 = LinkedList()
LL1.print_ll()    
LL1.add_begin(10)
LL1.print_ll()    
LL1.add_begin(15)   
LL1.add_begin(17)  
LL1.add_begin(13)  
LL1.print_ll()        