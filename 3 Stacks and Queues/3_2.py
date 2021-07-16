# 3.2 Stack Min

# How would you design a stack which, in addition to push
# and pop, has a function min which returns the minimum
# element? Push, pop and min should all operate in O(1) time

class MinStack:
    def __init__(self):
        self.values = []
        self.min = None

    def pushy(self, value):
        if(self.min == None):
            self.min = value
            self.values.append(value)
        elif(value < self.min):
            temp = (2 * value) - self.min
            self.min = value
            self.values.append(temp)
        else:
            self.values.append(value)

    def popy(self):
        removed_ele = self.values.pop(-1)
        if(removed_ele < self.min):
            self.min = ((2 * self.min) - removed_ele)

    def miny(self):
        return self.min


min_stack = MinStack()

min_stack.pushy(5)
min_stack.pushy(3)
min_stack.pushy(1)
min_stack.pushy(2)
print(min_stack.values)
print(min_stack.miny())
min_stack.popy()
print(min_stack.miny())
min_stack.popy()
print(min_stack.miny())
min_stack.popy()
print(min_stack.miny())
