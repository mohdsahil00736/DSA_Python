class Queuue:

    def __init__(self):
        self.items = []

    def IsEmpty(self):
        return len(self.items) == 0
    
    def InsertAtEnd(self, value):
        return self.items.append(value)

    def DeleteAtBeg(self):
        if self.IsEmpty():
            raise Exception("Queue is Empty")
        else:
            return self.items.pop(0)

qu = Queuue()
qu.InsertAtEnd(10)
qu.InsertAtEnd(20)
qu.InsertAtEnd(30)
print(qu.DeleteAtBeg())
print(qu.DeleteAtBeg())