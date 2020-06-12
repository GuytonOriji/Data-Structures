"""
Binary search trees are a data structure that enforce an ordering over 
the data they store. That ordering in turn makes it a lot more efficient 
at searching for a particular piece of data in the tree. 
This part of the project comprises two days:
1. Implement the methods `insert`, `contains`, `get_max`, and `for_each`
   on the BSTNode class.
2. Implement the `in_order_print`, `bft_print`, and `dft_print` methods
   on the BSTNode class.
"""

import sys
sys.path.append("../singly_linked_list/")

from collections import deque

class BSTNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self,value):
        #if node is pointing 2 None or node has no value
        if self.value is None:

            #set self.value to the value of the node
            self.value = value

        elif value >= self.value:#cant remove '='...needs to be '>=' or test will not pass
            # if new value is greater it will go to the right, check if we already have a node on right
            if self.right:
            # if node.right is there, insert the value
                self.right.insert(value)            
            # if there is no right node, insert the new node with the value
            else:
                self.right = BSTNode(value)
        else:
            if self.left:
                self.left.insert(value)
            else:
                self.left = BSTNode(value) 
    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        current_node = self
        while current_node.value != target:
            if current_node.value > target:
                if current_node.left:
                    current_node = current_node.left
                else:
                    return False
            else:
                if current_node.right:
                    current_node = current_node.right
                else:
                    return False
        return True
    # Return the maximum value found in the tree
    def get_max(self):
        if self.right:
            return self.right.get_max()
        else:
            return self.value

    # Call the function `fn` on the value of each node
    def for_each(self, fn):
        fn(self.value)
        if self.left:
            self.left.for_each(fn)
        if self.right:
            self.right.for_each(fn)

    # Part 2 -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self, node):
        if self.left:
            self.left.in_order_print(node)
        print(self.value)
        if self.right:
            self.right.in_order_print(node)

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    def bft_print(self, node):
        # Q IS THE POINTER VARIABLE THAT UPDATES WITHIN THE LOOP BELOW
        q = deque()
        q.append(self)

        while q:
            node = q.popleft()
            print(node.value)
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)

    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self, node):
        # Q IS THE POINTER VARIABLE THAT UPDATES WITHIN THE LOOP BELOW
        q = deque()
        q.append(self)

        while q:
            node = q.pop()
            print(node.value)
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)

    # Stretch Goals -------------------------
    # Note: Research may be required

    # Print Pre-order recursive DFT
    def pre_order_dft(self, node):
        if node:
            print(node.value)
            if node.left:
                node.left.pre_order_dft(node.left)
            if node.right:
                node.right.pre_order_dft(node.right)

    # Print Post-order recursive DFT
    def post_order_dft(self, node):
        if node:
            if node.left:
                node.left.post_order_dft(node.left)
            if node.right:
                node.right.post_order_dft(node.right)
            print(node.value)