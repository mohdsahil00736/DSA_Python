class CircularQueue :

    def __init__(self, size):             # for the size it create sotrage 
        self.size = size
        self.items = [None] * size         #  It creates the list of that size 
        self.front = self.rear = -1

    def enqueue(self, value):
        if ((self.rear +1)% self.size == self.front):
            print("Circular Queue is full ")
        elif self.front == -1:
            self.rear = self.front = 0
            self.items[self.rear] = value
        else:
            self.rear = (self.rear + 1) % self.size
            self.items[self.rear] = value

    def dequeue(self):
        if (self.front == -1):
            print("CirCular Queue is Empty")
        elif self.front == self.rear:
            print(self.items[self.front])
            self.items[self.front] = None    # it will remove the value to None
            self.front = self.rear = -1
        else:
            print(self.items[self.front])
            self.items[self.front] = None     # It will remove the value to None
            self.front = (self.front + 1) % self.size

cq = CircularQueue(3)
cq.enqueue(10)
cq.enqueue(20)
cq.enqueue(30)
cq.enqueue(40)   # this time it will show the queue is full
print(cq.items)
cq.dequeue()
cq.dequeue()
cq.dequeue()
cq.dequeue()
print(cq.items)



            

    