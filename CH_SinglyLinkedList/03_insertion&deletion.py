class Node:
    def __init__(self, info , next = None):
        self.data = info
        self.next = next

class SinglyLinkedList:

    def __init__(self, head= None):
        self.head = head

    def InsertAtBeg(self, vlaue):
        temp = Node(vlaue)
        temp.next = self.head
        self.head = temp


    def InsertAtMid(self, vlaue, x):
        temp = Node(vlaue)
        t1 = self.head

        while(t1.next != None):
            if(t1.data == x):
                temp.next = t1.next
                t1.next = temp
            t1 = t1.next

    def deleteLL(self, value ):
        t1 = self.head
        prev = t1
        if (t1.data == value):
            self.head = t1.next
        while(t1.next != None):
            if(t1.data == value):
                prev.next = t1.next
                break
            else :
                prev = t1
                t1 = t1.next
        if (t1.data == value):
            prev.next = None
     
    def PrintLinkedList(self):
        t1 = self.head
        while(t1.next != None):
            print(t1.data)
            t1 = t1.next
        print(t1.data) 
            
              
obj = SinglyLinkedList()
obj.InsertAtBeg(5)
obj.InsertAtBeg(8)
obj.InsertAtBeg(1)
obj.InsertAtMid(10, 8)
obj.InsertAtMid(20, 10)
obj.deleteLL(20)
obj.PrintLinkedList()


