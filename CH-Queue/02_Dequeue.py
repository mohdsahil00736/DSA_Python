class Dequeuue:

    def __init__(self):
        self.items = []

    def IsEmpty(self):
        return len(self.items) == 0
    
    def InsertAtEnd(self, value):
        return self.items.append(value)

    def DeleteAtBeg(self):
        if self.IsEmpty():
            raise Exception("Dequeue is Empty")
        else:
            return self.items.pop(0)

    def InsertAtBeg(self, value):       
        return self.items.insert(0, value)

    def DeleteATEnd(self):
        if self.IsEmpty():
            raise Exception("Dequeue is Empty")
        else:
            return self.items.pop()


qu = Dequeuue()
qu.InsertAtEnd(10)
qu.InsertAtBeg(50)
qu.InsertAtEnd(20)
qu.InsertAtEnd(30)
qu.InsertAtBeg(90)
print(qu.items)
print(qu.DeleteATEnd())
print(qu.DeleteATEnd())
print(qu.DeleteAtBeg())
print(qu.DeleteAtBeg())
print(qu.DeleteATEnd())
qu.DeleteATEnd()
