class Stack:

    def __init__(self):
        self.s = []

    def push(self, value):
        return self.s.append(value)

    def peek(self):
        if len(self.s) == 0:
            raise Exception ("Stack is Empty")
        else:
            return self.s[- 1]

    def pop(self):
        if len(self.s) == 0 :
            raise Exception ("Stack is Empty")
        else:
            return self.s.pop()

    def Print_stack(self):
        print(self.s)

stk = Stack()
stk.push(10)
stk.push(20)
stk.push(30)
print(stk.peek())
print(stk.pop())
stk.Print_stack()