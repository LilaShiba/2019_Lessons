# This problem was asked by Microsoft.
# Implement 3 stacks using a single list


class Stack():
    
    def __init__(self):
        self.size = 10
        self.list = [None] * self.size
        self.s0 = 0
        self.s1 = len(self.list)//2
        self.s2 = len(self.list) - 1
    
    def pop(self, stack_num):
        if stack_num == 0:
            self.s0 -= 1
            del self.list[self.s0]
        elif stack_num == 1:
            self.s1 -= 1
            del self.list[self.s1]
        else:
            # extend
            self.s2 += 1
            del self.list[self.s2]
        
    def push(self, stack_num, item):
        if stack_num == 0:
            self.list[self.s0] = item
            self.s0 += 1
        elif stack_num == 1:
            self.list[self.s1] = item
            self.s1 += 1
        else:
            self.list[self.s2] = item
            self.s2 -= 1
        
        if self.is_resize_needed():
            self.resize(self.size * 2)
    
    def is_resize_needed(self):
        return self.s0 == len(self.list) // 2 or self.s1 > self.s2
    
    def resize(self, size):
        # save old info
        prev_list = self.list
        prev_s0 = self.s0
        prev_s1 = self.s1
        prev_s2 = self.s2
        self.list = [None]*size
        
        # new values
        self.s0 = 0
        self.s1 = len(self.list)//2
        self.s2 = len(self.list) - 1
        
        # map old values to new
        
        for idx in range(prev_s0):
            self.push(0,prev_list[idx])
        
        for idx in range(len(prev_list)//2, prev_s1):
            self.push(1,prev_list[idx])
        
        for idx in reversed(range(prev_s2 + 1, len(prev_list))):
            self.push(2,prev_list[idx])
        
    def show(self):
        for x in range(len(self.list)):
            print(self.list[x])
            

wow = Stack()
wow.push(0,1)
wow.push(0,2)
wow.push(0,3)
wow.push(1,4)
wow.push(1,5)
wow.push(1,6)
wow.push(2,7)
wow.push(2,8)
wow.push(2,9)
wow.pop(2)
wow.show()
             
