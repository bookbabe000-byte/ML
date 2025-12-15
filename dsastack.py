class stack:
    def __init__(self):
        self.stack=[]


    def push(self,element):
        self.stack.append(element)


    def is_empty(self):
        return len(self.stack)==0

    def pop(self):
        if self.is_empty():
            return "is empty!"
            

    def peek(self):
        return self.stack[-1]
        

    def size(self):
        return len(self.stack)        
        

mystack=stack()
mystack.push(12)
mystack.push(34)
mystack.push(43)
mystack.push(64)


print(f"original stack:{mystack.stack}")
print(f"popped element:{mystack.pop()}")
print(f"stack after pop:{mystack.stack}")
print(f"accessed element:{mystack.peek()}")
print(f"size of stack:{mystack.size()}")

