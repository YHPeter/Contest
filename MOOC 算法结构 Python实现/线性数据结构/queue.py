# -*-utf-8-*- 
# queue
class queue():
    def __init__(self):
        self.queue = []
        
    def isEmpty(self):
        return self.queue==[]

    def size(self):
        return len(self.queue)

    def push(self,x):
        self.queue.insert(0,x)
    
    def pop(self):
        return self.queue.pop()
    