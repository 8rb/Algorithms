# 2.4 Partition

# Write code to partition a linked list around a value x,
# such that all nodes less than x come before all nodes
# greater than or equal to x. (IMPORTANT: The partition
# element x can appear anywhere in the "right partition"
# it does not nedd to appear between the left and right
# partitions. The additional spacing in the example below
# indicates the partition. Yes, the output below is one of
# many valid outputs!)

# Example:
# 3 -> 5 -> 8 -> 5 -> 10 -> 2 -> 1 [partition = 5]
# 3 -> 1 -> 2      ->       10 -> 5 -> 5 -> 8

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
            if(node.next != None):
                print(node.data, end=" -> ")
            else:
                print(node.data)
            node = node.next
    
    def partition2(self, partition):
        partitionedList = LinkedList()
        node = self.head
        head = node
        tail = node
        
        while node != None:
            nexty = node.next
            if(node.data < partition):
                node.next = head
                head = node
            else:
                tail.next = node
                tail = node
            node = nexty
        tail.next = None
        partitionedList.tail = tail
        partitionedList.head = head

        return partitionedList

    def partition(self, partition):
        part1 = []
        part2 = []
        node = self.head
        while node != None:
            if(node.data < partition):
                part1.append(node)
            else:
                part2.append(node)
            node = node.next
        
        nodes = part1 + part2
        self.head = nodes[0]
        for i in range(len(nodes)-1):
            nodes[i].next = nodes[i+1]
        self.tail = nodes[-1]
        self.tail.next = None

listy = LinkedList()
listy.appendy(3)
listy.appendy(5)
listy.appendy(8)
listy.appendy(5)
listy.appendy(10)
listy.appendy(2)
listy.appendy(1)
listy.show()

partition = 5
print("Partition Method 1:", partition)
listy.partition(partition)
listy.show()

print("Partition Method 2:", partition)
listy2 = listy.partition2(partition)
listy2.show()