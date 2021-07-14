# 2.8 Loop Detection

# Given a linked list which might contain a loop, implement
# an algorithm that returns the node a the beginning of
# the loop (if one exists)

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def appendy(self, node):
        if(self.size == 0):
            self.head = node
            self.tail = node
        else:
            self.tail.next = node
            self.tail = node
        self.size += 1

    def show(self):
        node = self.head
        while node:
            print(node.data)
            node = node.next


def detect_loop(l1):
    nodes = {}
    node = l1.head
    i = 0
    loop = False
    while node and not loop:
        if(node in nodes):
            loop = True
            return node
        else:
            nodes[node] = i
            i += 1
        node = node.next
    return False


l1 = LinkedList()

node_a = Node('A')
node_b = Node('B')
node_c = Node('C')
node_d = Node('D')
node_e = Node('E')

l1.appendy(node_a)
l1.appendy(node_b)
l1.appendy(node_c)
l1.appendy(node_d)
l1.appendy(node_e)
l1.appendy(node_c)

print(detect_loop(l1))
