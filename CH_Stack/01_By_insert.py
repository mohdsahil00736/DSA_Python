class Stack:
    # follows LIFO -> Last In First Out

    def __init__(self):     
        self.s = []

    def push(self, value):  # For insert the value at index 0 always 
        return self.s.insert(0, value)

    def peek(self):   # To see top of the stack 
        if len(self.s) == 0:
            raise Exception ("Stack is Empty")
        else:
            return self.s[0]

    def pop(self):   # To Delete the top of the stack
        if len(self.s) == 0:
            raise Exception ("Stack is Empty")
        else:
            return self.s.pop(0)

    def print_stack(self):
        print(self.s)

stk = Stack()
stk.push(10)
stk.push(20)
stk.push(30)
print(stk.peek()) 
print(stk.pop())
stk.print_stack()