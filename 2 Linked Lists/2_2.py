# 2.2 Return Kth to Last

# Implement an algorithm to find the kth to last element
# of a singly linked list.

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

    def return_kth_to_last(self, index):
        node = self.head
        i = 0
        kth_elem = []
        if(index >= self.length):
            return kth_elem
        while i != index:
            node = node.next
            i+=1
        while node != None:
            kth_elem.append(node.data)
            node = node.next
        return kth_elem

listy = LinkedList()

listy.appendy(1)
listy.appendy(2)
listy.appendy(3)
listy.appendy(4)
listy.appendy(5)
listy.appendy(6)

print(listy.return_kth_to_last(0))
print(listy.return_kth_to_last(1))
print(listy.return_kth_to_last(4))
print(listy.return_kth_to_last(5))
print(listy.return_kth_to_last(6))