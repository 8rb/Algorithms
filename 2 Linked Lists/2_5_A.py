# 2.5 Sum Lists

# Scenario A

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

def sum_nodes(n1, n2, carry):
    s1 = int(n1.data) if n1 else 0
    s2 = int(n2.data) if n2 else 0
    return s1 + s2 + carry


def sum_lists(l1, l2):
    l3 = LinkedList()
    carry = 0
    node1 = l1.head
    node2 = l2.head
    while node1 != None or node2 != None:
        sumy = sum_nodes(node1, node2, carry)
        ans = sumy % 10
        l3.appendy(ans)
        carry = sumy // 10
        if(node1):
            node1 = node1.next
        if(node2):
            node2 = node2.next
    return l3

def show_answer(l3):
    node = l3.head
    ans = ""
    while node:
        ans+=str(node.data)
        if(node.next):
            print(node.data, end="->")
        else:
            print(node.data, end=". ")
        node = node.next
    print("That is,", ans[::-1])

l1 = LinkedList()
l2 = LinkedList()

l1.appendy(7)
l1.appendy(1)
l1.appendy(6)

l2.appendy(5)
l2.appendy(9)
l2.appendy(2)

l3 = sum_lists(l1, l2)

show_answer(l3)