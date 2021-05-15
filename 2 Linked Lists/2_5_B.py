# 2.5 Sum Lists

# Scenario B

# Suppose the digits are stored in forward order.
# Repeat the 2_5 problem.

# EXAMPLE:
# Input: (6->1->7) + (2->9->5). That's 617 + 295
# Output: 2 -> 1 -> 9. That's 912

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

def pad_lists(l1, l2):
    if(l1.size > l2.size):
        times = l1.size - l2.size
        for _ in range(times):
            temp_node = Node(0)
            temp_node.next = l2.head
            l2.head = temp_node
            l2.size+=1
    else:
        times = l2.size - l1.size
        for _ in range(times):
            temp_node = Node(0)
            temp_node.next = l1.head
            l1.head = temp_node
            l1.size+=1
    return l1, l2

def sum_nodes(node1, node2, carry):
    total = node1.data + node2.data + carry
    val = total % 10
    carry = total // 10
    return val, carry


def sum_lists(l1, l2):
    l3 = LinkedList()
    l1, l2 = pad_lists(l1, l2)
    l1.reverse()
    l2.reverse()
    node1 = l1.head
    node2 = l2.head
    val = 0
    carry = 0
    for _ in range(l1.size):
        val, carry = sum_nodes(node1, node2, carry)
        l3.appendy(val)
        node1 = node1.next
        node2 = node2.next
    l3.reverse()
    return l3




l1 = LinkedList()
l2 = LinkedList()

l1.appendy(1)
l1.appendy(2)
l1.appendy(3)

l2.appendy(5)
l2.appendy(6)
l2.appendy(7)
l2.appendy(7)

l3 = sum_lists(l1, l2)

l3.show()
print(l3.size)