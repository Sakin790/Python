class Node:
    def __init__(self, item=None, next=None):
        self.item = item
        self.next = next

class SSl:
    def __init__(self, start=None):
        self.start = start

    def isEmpty(self):
        return self.start is None

    def insertAtFirst(self, data):
        newNode = Node(data)
        newNode.next = self.start
        self.start = newNode

    def insertAtLast(self, data):
        newNode = Node(data)
        if self.isEmpty():
            self.start = newNode
        else:
            temp = self.start
            while temp.next is not None:
                temp = temp.next
            temp.next = newNode

    def printList(self):
        if self.isEmpty():
            print("Node is empty")
            return
        temp = self.start
        while temp is not None: 
            print(temp.item, end=" -> ")
            temp = temp.next
        print("None")  


myLinkedList = SSl()
myLinkedList.insertAtFirst(10)
myLinkedList.insertAtLast(20)
myLinkedList.insertAtLast(30)
myLinkedList.printList()
