# 3.4 Queue via Stack

# Implement a MyQueue class which implements a queue
# using two stacks.

class MyQueue:
    def __init__(self):
        self.stack_newest = []
        self.stack_oldest = []

    def add(self, value):
        self.stack_newest.append(value)

    def shiftStacks(self):
        if(len(self.stack_oldest) == 0):
            while (len(self.stack_newest) != 0):
                self.stack_oldest.append(self.stack_newest.pop(-1))

    def peek(self):
        self.shiftStacks()
        return self.stack_oldest[-1]

    def remove(self):
        self.shiftStacks()
        return self.stack_oldest.pop(-1)


my_queue = MyQueue()

my_queue.add(1)
my_queue.add(2)
my_queue.add(3)

print(my_queue.peek())

my_queue.remove()

print(my_queue.peek())
