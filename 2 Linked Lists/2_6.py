# 2.6 Palindrome

# Implement a function to check if a linked 
# list is a palindrome.

from copy import deepcopy

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def appendy(self, data):
        node = Node(data)
        if(self.size == 0):
            self.head = node
            self.tail = node
        else:
            self.tail.next = node
            self.tail = node 
        self.size+=1

    def show(self):
        node = self.head
        while node:
            if(node.next):
                print(node.data, end="->")
            else:
                print(node.data)
            node = node.next

    def reverse(self):
        node1 = None
        node2 = self.head
        while node2:
            node3 = node2.next
            node2.next = node1
            node1 = node2
            node2 = node3
        self.tail = self.head
        self.head = node1

    def isEqual(self, l1, l2):
        travel = self.size // 2
        node1 = l1.head
        node2 = l2.head
        for _ in range(travel):
            if(node1.data != node2.data):
                return False
            node1 = node1.next
            node2 = node2.next
        return True

    def check_palindrome(self, l1):
        l2 = deepcopy(l1)
        l2.reverse()
        return self.isEqual(l1, l2)

listy = LinkedList()
listy.appendy(1)
listy.appendy(2)
listy.appendy(2)
listy.appendy(2)
listy.appendy(1)
listy.show()

print(listy.check_palindrome(listy))