# 3.3 Stack of Plate

# Implement a data structure SetOfStacks that mimics this.
# SetOfStacks should be composed of several stacks and
# should create a new stack once the previous one exceeds
# capacity. push() and pop() should behave identically to
# a single stack

class SetOfStacks:
    def __init__(self, exceed_size):
        self.exceed_size = exceed_size
        self.values = []
        self.actual_stack = 0
        self.free_space = []
        self.is_there_space = False

    def push(self, value):
        if(len(self.values) == 0):
            self.values.append([value])
        elif(self.is_there_space):
            for i in range(len(self.free_space)):
                if(self.free_space[i] != 0):
                    self.values[i].append(value)
                    self.free_space[i] -= 1
                    break
            self.is_there_space = False
            for i in range(len(self.free_space)):
                if(self.free_space[i] != 0):
                    self.is_there_space = True
                    break

        elif(len(self.values[self.actual_stack]) == self.exceed_size):
            self.values.append([value])
            self.actual_stack += 1
            self.free_space.append(0)
        else:
            self.values[self.actual_stack].append(value)

    def pop(self):
        if(len(self.values) > 0 and len(self.values[self.actual_stack]) > 0):
            self.values[self.actual_stack].pop(-1)
            if(len(self.values[self.actual_stack]) == 0):
                self.actual_stack -= 1
                self.values.pop(-1)
                self.free_space.pop(-1)

    def popAt(self, stack_index):
        if(len(self.values) > 0 and len(self.values[stack_index]) > 0):
            self.values[stack_index].pop(-1)
            if(stack_index != self.actual_stack):
                self.free_space[stack_index] += 1
                self.is_there_space = True


set_of_stacks = SetOfStacks(3)

set_of_stacks.pop()
set_of_stacks.push(1)
set_of_stacks.push(2)
set_of_stacks.push(3)
set_of_stacks.push(4)
set_of_stacks.push(5)
set_of_stacks.push(6)
set_of_stacks.push(7)

print(set_of_stacks.values)

set_of_stacks.popAt(0)
set_of_stacks.popAt(1)
set_of_stacks.popAt(1)
set_of_stacks.popAt(1)
set_of_stacks.popAt(1)

print(set_of_stacks.values)

set_of_stacks.push(33)
print(set_of_stacks.values)

set_of_stacks.push(44)
set_of_stacks.push(55)
set_of_stacks.push(66)
print(set_of_stacks.values)
