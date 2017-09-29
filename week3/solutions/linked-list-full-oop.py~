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



class LL():
    def __init__(self,value=None):
        self.value = value
        self.next = None


def print_all_nodes(node):
    if not node:
        return

    print node.value
    print_all_nodes(node.next)
        

def add_node(node,new_node):
    if not node.next:
        node.next = new_node
        return

    add_node(node.next,new_node)
    

def insert_node(node,new_node,value):
    if not node:
        return None
    
    if node.value == value:
        new_node.next = node.next
        node.next = new_node
        return

    insert_node(node.next,new_node,value)
        
def remove_node(node,value):
    if not node:
        return None
    if not node.next:
        return
    if node.next.value == value:
        node.next = node.next.next
        return
    remove_node(node.next,value)
        
    
root = LL()
root.value = 1

add_node(root,LL(3))
insert_node(root,LL(2),1)

#next_value = LL()
#next_value.value = 2

#root.next = next_value



