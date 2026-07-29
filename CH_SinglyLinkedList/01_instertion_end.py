class Node:
    def __init__(self, info, next= None):  # Created a node , self executable contains info , next 
        self.data = info
        self.next = next

class SinglyLinkedList:              # Created singly linked list , first put head, then perform operation of insertin 
    def __init__(self, head=None):
        self.head = head

    def insertionAtEnd(self, value):
        temp = Node(value)
        if(self.head != None):
            t1 = self.head
            while(t1.next != None):
                t1 = t1.next
            t1.next = temp
        else:
            self.head = temp

    def printLinkedList(self):        # function to print the linked list 
        t1 = self.head
        while(t1.next != None):
            print(t1.data)
            t1 = t1.next
        print(t1.data)

obj = SinglyLinkedList()
obj.insertionAtEnd(10)
obj.insertionAtEnd(20)
obj.insertionAtEnd(30)
obj.printLinkedList()




