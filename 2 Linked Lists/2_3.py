# 2.3 Delete Middle Node

# Implement an algorithm to delete a node in the middle.
# (i.e., any node but the first and last node, not necessarily
# the exact middle) of a singly linked list, given only access
# to that node.

# Example:
# Input the node "c" from the linked list:
# a -> b -> c -> d -> e -> f 
# The new linked list looks like:
# a -> b -> d -> e -> f

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.tails = None
        self.length = 0
    
    def appendy(self, data):
        node = Node(data)
        if(self.length == 0):
            self.head = node
        elif(self.length == 1):
            self.head.next = node
            self.tails = node
        else:
            self.tails.next = node
            self.tails = node
        self.length+=1
    
    def show(self):
        node = self.head
        while node != None:
            print(node.data)
            node = node.next

    def delete_middle_node(self, node):
        actual = self.head
        prevActual = self.head
        while actual != None and actual.data != node:
            prevActual = actual
            actual = actual.next
        if(actual == None):
            return False
        else:
            prevActual.next = actual.next


listy = LinkedList()
listy.appendy("a")
listy.appendy("b")
listy.appendy("c")
listy.appendy("d")
listy.appendy("e")
listy.appendy("f")

listy.delete_middle_node("c")
listy.delete_middle_node("d")
listy.delete_middle_node("g") # Validated non existing node

listy.show()