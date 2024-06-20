class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        self.head = None

    def displayLinKedList(self):
        temp = self.head
        while temp is not None:
            print(temp.data, "->", end="")
            temp = temp.next

    def insertAtEnd(self,data):
        node = Node(data)
        if self.head is None:
            self.head = node
        else:
            temp = self.head
            while temp.next is not None:
                temp = temp.next
            temp.next = node

    def insertAtBeginning(self,data):
        node = Node(data)
        if self.head is None:
            self.head = node
        else:
            node.next = self.head
            self.head = node

    def insertAtSpecificPosition(self,data,pos):
        count = 0
        i = 1
        node = Node(data)
        temp = self.head
        while temp is not None:
            count += 1
            temp = temp.next
        if (pos > count+1) or (pos < 1):
            print("Invalid Position")
        elif pos == 1:
            self.insertAtBeginning(data)
        elif pos == count+1 :
            self.insertAtEnd(data)
        else:
            temp = self.head
            while i < pos-1:
                temp = temp.next
                i += 1
            node.next = temp.next
            temp.next = node



l = SinglyLinkedList()

while True:
    print('\n1.Insertion at beginning')  #After end we cannot pass any arguments  and also multiple end is not allowed in a print
    print('1.Insertion at End')
    print('1.Insertion at specific position')
    print('4.Display the Linked List')
    choice = int(input("Enter your choice:"))
    if choice == 1:
        data = int(input("Enter the data:"))
        l.insertAtBeginning(data)
    elif choice == 2:
        data = int(input("Enter the data:"))
        l.insertAtEnd(data)
    elif choice == 3:
        data = int(input("Enter the data:"))
        pos = int(input("Enter the position:"))
        l.insertAtSpecificPosition(data,pos)
    elif choice == 4:
        l.displayLinKedList()

