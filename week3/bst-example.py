''' 

Binary search tree (BST)

A binary tree is made up of nodes.

Each node stores a piece of data, and then has two child nodes, left and right.

The left node is always less or lower in value then the previous node, the right higher.

The main advantage of binary search trees is that it remains ordered, which provides quicker search times than many other data structures.

Read the intro section and the definitions section here:
http://en.wikipedia.org/wiki/Binary_search_tree

There are many ways to implement a BST.  We are going to walk you through a simple implementation of it and build a tree.  Then you will traverse the tree to print out all the nodes in order.

To complete this assignment, you need to understand how to traverse a BST:

1) Pre-order:
Display the data part of root element (or current element)
Traverse the left subtree by recursively calling the pre-order function.
Traverse the right subtree by recursively calling the pre-order function.

2) In-order:
Traverse the left subtree by recursively calling the in-order function.
Display the data part of root element (or current element).
Traverse the right subtree by recursively calling the in-order function.

3) Post-order:
Traverse the left subtree by recursively calling the post-order function.
Traverse the right subtree by recursively calling the post-order function.
Display the data part of root element (or current element).

For more information on tree traversal, read this: http://en.wikipedia.org/wiki/Tree_traversal

'''


# This is your Node class that we have defined for you. You do not need to edit this.
class Node:
    def __init__(self, val):
        self.l_child = None
        self.r_child = None
        self.data = val

        
def binary_insert(root, node):
    """ recursive insert """

    pass
    #if node data is less then the root data, insert the data to the l_child instance variable
    #else insert the node on the r_child instance variable
            
def in_order_print(root):
    """ in order print """
    pass

def pre_order_print(root):
    """ pre order print """
    pass

def post_order_print(root):
    """ post order print """
    pass

r = Node(3)
binary_insert(r, Node(7))
binary_insert(r, Node(1))

print "In order print"

in_order_print(r)

#Output should be
#1
#3
#7


print "Pre order print"

pre_order_print(r)

#Output should be
#3
#1
#7

print "Post order print"

post_order_print(r)

#Output should be
#1
#7
#3
