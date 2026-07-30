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
obj.PrintLinkedList()

