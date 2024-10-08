class Node:
    def __init__(self,data):
        self.data = data
        self.prev = None
        self.next = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def displayLinKedList(self):
        if self.head is None:
            print("Linked List is empty\n")
        temp = self.head
        while temp is not None:
            print(temp.data, "->", end="")
            temp = temp.next
        print()


    def insertAtBeginning(self,data):
        node = Node(data)
        if self.head is None:
            self.head = node
        else:
            node.next = self.head
            self.head.prev = node
            self.head = node

    def insertAtEnd(self,data):
        node = Node(data=data)
        if self.head is None:
            self.head = node

        else:
            temp = self.head
            while temp.next is not None:
                temp = temp.next

            node.prev = temp
            temp.next = node
    def insertAtSpecificPosition(self,data,pos):
        count = 0
        i = 1
        temp = self.head
        while temp is not None:
            count += 1
            temp = temp.next

        if (pos > count + 1) or (pos < 1):
            print("Invalid Position\n")

        elif pos == 1:
            self.insertAtBeginning(data=data)
        elif pos == count+1:
            self.insertAtEnd(data= data)
        else:
            node = Node(data=data)
            temp = self.head

            while i < pos:
                prev = temp
                temp = temp.next
                i += 1
            node.prev = prev
            prev.next = node
            node.next = temp
            temp.prev = node

    def deleteAtBeginning(self):
        if self.head is None:
            print("List is empty")
        elif self.head.next is None:
            self.head = None
        else:
            self.head = self.head.next
            self.head.prev = None

    def deleteAtEnd(self):
        if self.head is None:
            print("List is empty")
        elif self.head.next is None:
            self.head = None
        else:
            temp = self.head
            # while temp.next is not None:
            #     prev = temp
            #     temp = temp.next
            # prev.next = None

            while temp.next is not None:
                temp = temp.next

            temp.prev.next = None

    def deleteAtSpecificPosition(self,pos):
        count = 0
        i = 1
        temp = self.head
        while temp is not None:
            count += 1
            temp = temp.next

        if pos == 1:
            self.deleteAtBeginning()
        elif pos == count:
            self.deleteAtEnd()
        elif pos > count:
            print("Invalid Position\n")
        elif pos < count:
            temp = self.head
            while i < pos:
                temp = temp.next
                i += 1

            temp.prev.next = temp.next
            temp.next.prev = temp.prev

    def search(self, data):
        temp = self.head
        pos = 1
        while temp is not None:
            if temp.data == data:
                print(f"Data {data} found at position {pos}")
                return
            temp = temp.next
            pos += 1
        print(f"Data {data} not found in the list")
    



l = DoublyLinkedList()

while True:
    print('\n1.Insertion at beginning')  #After end we cannot pass any arguments  and also multiple end is not allowed in a print
    print('2.Insertion at End')
    print('3.Insertion at specific position')
    print('4.Delete at Beginning')
    print('5.Delete at End')
    print('6.Delete at specific position')
    print('7.Display the Linked List')
    print('8.Search')


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
        l.deleteAtBeginning()
    elif choice == 5:
        l.deleteAtEnd()
    elif choice == 6:
        position = int(input('Enter the position:'))
        l.deleteAtSpecificPosition(position)
    elif choice == 7:
        l.displayLinKedList()
    elif choice == 8:
        data = int(input("Enter the data to be search:"))
        l.search(data)
