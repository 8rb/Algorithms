# 2.7 Intersection

# Given two (singly) linked lists, determine
# if the two lists intersect

# the current implementation of the algorithm works
# comparing the nodes by value instead of by reference
# this is because of the logic of adding the nodes to the
# linked list. In order to adapt this implementation,
# it is necessary to change the append method of the class
# LinkedList and change the two comparisons of nodes by value
# inside the find_intersection function, named as (1) and (2)

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.size = 0
        self.head = None
        self.tail = None

    def appendy(self, data):
        node = Node(data)
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


def get_starting_node(l1, size):
    node = l1.head

    while(size != 0):
        node = node.next
        size -= 1

    return node


def find_intersection(l1, l2):
    print(l1.size)
    print(l2.size)

    # (1) Change l1.tail.data -> l1.tail to compare by reference
    # same for l2.tail.data -> l2.tail
    if(l1.tail.data != l2.tail.data):
        return False

    longer_list = l1 if l1.size > l2.size else l2
    shorter_list = l1 if l1.size < l2.size else l2

    diff_size = abs(l1.size - l2.size)

    s1 = get_starting_node(longer_list, diff_size)
    s2 = get_starting_node(shorter_list, 0)

    # (2) Change s1.data -> s1 to compare by reference
    # (the node, not only the value)
    # same for s2.data -> s2
    while s1.data != s2.data:
        s1 = s1.next
        s2 = s2.next

    return s1


l1 = LinkedList()

l1.appendy(3)
l1.appendy(1)
l1.appendy(5)
l1.appendy(9)
l1.appendy(7)
l1.appendy(2)
l1.appendy(1)

l2 = LinkedList()
l2.appendy(4)
l2.appendy(6)
l2.appendy(7)
l2.appendy(2)
l2.appendy(1)


# l1.show()
# l2.show()
print(find_intersection(l1, l2))
