# 3.1 Three in One

# Describe how you could use a single array to implement
# three stacks.

# This implementation uses a fixed size for each Stack

class MultiStack:
    def __init__(self, capacity):
        self.stacks_number = 3
        self.stack_capacity = capacity
        self.values = [None] * (capacity * 3)
        self.sizes = [0, 0, 0]

    def push(self, stack_index, value):
        stack_size = self.sizes[stack_index - 1]
        if(stack_size == self.stack_capacity):
            return False
        pos = stack_size + ((stack_index - 1) * self.stack_capacity)
        self.values[pos] = value
        self.sizes[stack_index - 1] += 1

    def pop(self, stack_index):
        stack_size = self.sizes[stack_index - 1]
        if(stack_size == 0):
            return False
        pos = stack_size + ((stack_index - 1) * self.stack_capacity) - 1
        self.values[pos] = None
        self.sizes[stack_index - 1] -= 1

    def show_all(self):
        print(self.values)
        print(len(self.values))

    def peek(self, stack_index):
        stack_size = self.sizes[stack_index - 1]
        if(stack_size == 0):
            print("None")
            return
        pos = stack_size + ((stack_index - 1) * self.stack_capacity) - 1
        print(self.values[pos])

    def show(self, stack_index):
        starting_pos = 0 + self.stack_capacity * (stack_index - 1)
        if(self.sizes[stack_index - 1] == 0):
            print("[Empty Stack ", stack_index, "]", sep="")
            return
        for i in range(self.sizes[stack_index - 1]):
            if(i == self.sizes[stack_index - 1] - 1):
                print(self.values[starting_pos + i])
            else:
                print(self.values[starting_pos + i], end=" ")

    def is_empty(self, stack_index):
        return True if self.sizes[stack_index - 1] == 0 else False

    def is_full(self, stack_index):
        return True if self.sizes[stack_index - 1] == self.stack_capacity else False


stacky = MultiStack(10)
stacky.push(1, 1)
stacky.push(1, 2)
stacky.push(1, 3)
stacky.push(1, 4)
stacky.push(1, 5)
stacky.push(1, 6)
stacky.push(1, 7)
stacky.push(1, 8)
stacky.push(1, 9)
stacky.push(1, 10)
stacky.push(2, 11)
stacky.push(3, 21)

stacky.pop(2)
print("Stacks values:")
stacky.show(1)
stacky.show(2)
stacky.show(3)

print("Peeks:")
stacky.peek(1)
stacky.peek(2)
stacky.peek(3)

print("Is Empty:")
print("1:", stacky.is_empty(1))
print("2:", stacky.is_empty(2))
print("3:", stacky.is_empty(3))

print("Is Full:")
print("1:", stacky.is_full(1))
