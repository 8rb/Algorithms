# 2.5 Sum Lists

# You have two numbers represented by a linked list, where each
# node contains a single digit. The digits are stored in reverse
# order, such that the 1's digit is at the head of the list.
# Write a function that adds the two numbers and returns the sum
# as a linked list

# EXAMPLE:
# Input: (7->1->6) + (5->9->2). That's 617 + 295
# Output: 2 -> 1 -> 9. That's 912

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0
    
    def appendy(self, data):
        node = Node(data)
        if(self.length == 0):
            self.head = node
            self.tail = node
        else:
            self.tail.next = node
            self.tail = node
        self.length+=1
    
    def show(self):
        node = self.head
        while node != None:
            if(node.next):
                print(node.data, end="->")
            else:
                print(node.data)
            node = node.next

    def reverse(self):
        node1 = None
        node2 = self.head
        while node2 != None:
            node3 = node2.next
            node2.next = node1
            node1 = node2
            node2 = node3
        self.tail = self.head
        self.head = node1

l1 = LinkedList()
l2 = LinkedList()

l1.appendy(7)
l1.appendy(1)
l1.appendy(6)

l2.appendy(5)
l2.appendy(9)
l2.appendy(2)

l1.show()
l1.reverse()
l1.show()

l2.show()
l2.reverse()
l2.show()
