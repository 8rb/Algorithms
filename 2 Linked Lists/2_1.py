# 2.1 Remove dups

# Write code to remove duplicates from an unsorted linked
# list. 

# First we implement the node, that will contain the data and
# a pointer to the next element in the list.

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# Then we implement a class called LinkedList to hold all the
# methods that could be required for its correct functioning.

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
            self.tails = node
            self.head.next = self.tails
        else:
            self.tails.next = node
            self.tails = node
        self.length+=1
    
    def printy(self):
        val = self.head
        while val != None:
            print(val.data)
            val = val.next
    
    def removeDups(self):
        # We can use a hash table to store the values
        # and validate if it contains duplicates.
        # This solution has a runtime of O(n)
        values = {}
        first = self.head
        second = self.head.next
        values[first.data] = 1
        
        while second != None:
            if second.data in values:
                # Remove element
                temp = second
                first.next = temp.next
                second = temp.next
                self.length-=1
            else:
                values[second.data] = 1
                first = second
                second = second.next

    def removeDupsNoSpace(self):
        # Without using a temporary buffer (hash table)
        # The solution would take O(n^2) time
        first = self.head
        
        while first != None:
            prevSecond = first
            second = first.next
            while second != None:
                if(first.data == second.data):
                    # Remove element
                    temp = second
                    prevSecond.next = temp.next
                    second = temp.next
                    self.length-=1
                else:
                    prevSecond = second
                    second = second.next
            first = first.next

listy = LinkedList()

listy.appendy(1)
listy.appendy(1)
listy.appendy(8)
listy.appendy(3)
listy.appendy(3)
listy.appendy(3)
listy.appendy(4)
listy.appendy(2)
listy.appendy(1)
listy.appendy(4)
listy.appendy(4)
listy.appendy(8)
listy.appendy(5)
listy.appendy(5)
listy.appendy(5)
listy.printy()

print("Removed duplicates using hash table")
listy.removeDups()
listy.printy()

listy.appendy(1)
listy.appendy(1)
listy.appendy(8)
listy.appendy(3)
listy.appendy(3)
listy.appendy(3)
listy.appendy(4)
listy.appendy(2)
listy.appendy(1)
listy.appendy(4)
listy.appendy(4)
listy.appendy(8)
listy.appendy(5)
listy.appendy(5)
listy.appendy(5)

print("Removed duplicates without using buffer")
listy.removeDupsNoSpace()
listy.printy()