# 3.5 Sort Stack

# Write a program to sort a stack sucht that the smallest
# items are on the top.

# This implementation's complexity is O(n^2) since it
# was asked to prioritize space, which is O(n)

# With unlimited space we could implement a sorting algorithm
# Therefore, we would have a O(nlogn) time complexity.

class SortStack:
    def __init__(self):
        self.stack = []

    def push(self, value):
        self.stack.append(value)

    def pop(self):
        return self.stack.pop(-1)

    def is_empty(self):
        return True if len(self.stack) == 0 else False

    def peek(self):
        if(len(self.stack) > 0):
            return self.stack[-1]
        return False

    def sorty(self):
        temp_stack = SortStack()
        while not self.is_empty():
            temp = self.pop()
            print(temp)
            while not temp_stack.is_empty() and temp_stack.peek() > temp:
                self.push(temp_stack.pop())
            temp_stack.push(temp)
        while not temp_stack.is_empty():
            self.push(temp_stack.pop())


sort_stack = SortStack()

sort_stack.push(5)
sort_stack.push(7)
sort_stack.push(13)
sort_stack.sorty()
print(sort_stack.stack)
