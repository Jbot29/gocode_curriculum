
'''

A very common data strucutre is a linked list. It is away of creating a list of data when you don't
know the size of the array ahead of time.

Python does this internally for many data structures.

We can easily mimic them in Python with a class.

A linked list has nodes.

Each node can have a value, and then a pointer or link to the next node. 


1) write as functions or possibly methods


2) print all the nodes, can be done recursively or iteratively 


3) add node - takes a root and find then end, add a new node to the end.


4) insert - takes a root, and new node, and a value to find, when found it inserts that value after
#i.e. 1 -> 3. insert LL(2) to make 1->2->3


5) remove takes the root, and a value to remove from the list

6) Search and find a node data

'''



class LLNode():
    def __init__(self,value=None):
        self.value = value
        self.next = None

class LL():
    def __init__(self):
        self.root = None

    def print_all(self):
        return self.print_all_i(self.root)

    def print_all_i(self,node):
        if not node:
            return

        print node.value
        print_all_nodes(node.next)
        
    def add(self,value):
        if not self.root:
            self.root = LLNode(value)
        else:
            return self.add_node(self.root,LLNode(value))
    
    def add_node(self,node,new_node):
        if not node.next:
            node.next = new_node
            return

        add_node(node.next,new_node)
    

    def insert(self,new_value,value):
        return self.insert_node(self.root,LLNode(new_value),value)
    
    def insert_node(self,node,new_node,value):
        if not node:
            return None
    
        if node.value == value:
            new_node.next = node.next
            node.next = new_node
            return

        insert_node(node.next,new_node,value)

    def remove(self,value):
        return self.remove_node(self.root,value)
    
    def remove_node(self,node,value):
        if not node:
            return None
        if not node.next:
            return
        if node.next.value == value:
            node.next = node.next.next
            return
        remove_node(node.next,value)
        
    
ll = LL()

ll.add(1)
ll.add(2)

ll.add(5)

ll.insert(3,2)

ll.add(7)

ll.add(9)

ll.remove(7)

ll.print_all()
