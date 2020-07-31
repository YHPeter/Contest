# -*-utf-8-*- 
# stack
class stack():
    def __init__(self):
        self.stack = []

    def isEmpty(self):
        return self.stack==[]

    def size(self):
        return len(self.stack)

    def push(self,x):
        self.stack.append(x)
    
    def pop(self):
        return self.stack.pop()
    