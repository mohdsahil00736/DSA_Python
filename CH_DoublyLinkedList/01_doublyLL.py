class Node:
    def __init__(self, value = None):
        self.value = value
        self.next = None
        self.prev = None

class DoublyLL:
    def __init__(self):
        self.head = None

    def InsertAtEnd(self, value):
        temp = Node(value)
        if(self.head == None):
            self.head = temp
            return
        
        t = self.head
        while(t.next != None):
            t = t.next

        t.next = temp
        temp.prev = t 

    def InsertionAtBeg(self , value):
        temp = Node(value)
        if (self.head == None):
            self.head = temp
            return
        
        if (self.head != None):
            temp.next = self.head
            self.head.prev = temp
            self.head = temp

    def InsertionAtMid(self,value, x):
        temp = Node(value)
        t = self.head

        while (t.next != None):
            if (t.value == x ):
                break
            else :
                t = t.next

        temp.next = t.next
        t.next.prev = temp
        t.next = temp
        temp.prev = t

    def DeletionLinkedList(self,value_give):
        
        if (self.head == None ):
            print("Linked List is Empty")
            return
        
        t = self.head
        if (t.value == value_give):
            self.head = t.next
            self.head.prev = None
            return

        while(t.next != None):
            if (t.value == value_give):
                t.prev.next = t.next
                t.next.prev = t.prev
                return
            else:
                t = t.next

        if (t.value == value_give):
            t.prev.next = None
        


    def printDoublyLL(self):
        t1 = self.head
        while(t1.next != None):
            print(t1.value, end = " <--> ")
            t1 = t1.next
        print(t1.value)

obj = DoublyLL()
obj.InsertAtEnd(4)
obj.InsertAtEnd(5)
obj.InsertAtEnd(6)
obj.InsertAtEnd(7)
obj.InsertionAtBeg(3)
obj.InsertionAtBeg(2)
obj.InsertionAtMid(10, 6)
obj.DeletionLinkedList(2)
obj.DeletionLinkedList(6)
obj.DeletionLinkedList(7)
obj.printDoublyLL()
        