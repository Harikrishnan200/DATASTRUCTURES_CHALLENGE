class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class SinglyLinkedList:
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
            print("Invalid Position\n")
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

    def deleteAtBeginning(self):
        if self.head is None:
            print("Linked List is empty\n")
            return
        else:
            print(str(self.head.data)+ " deleted successfully\n")
            self.head = self.head.next

    def deleteAtEnd(self):
        if self.head is None:
            print("Linked list is empty\n")
            return
        elif self.head.next is None:
            print(str(self.head.data) + " deleted successfully\n")
            self.head  = None
            return
        else:
            temp = self.head
            while temp.next is not None:
                prev = temp
                temp = temp.next
            prev.next = None

    def deleteAtSpecificPosition(self,pos):
        count = 0
        i = 1
        temp = self.head
        while temp is not  None:
            count +=1
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
                prev = temp
                temp = temp.next
                i += 1
            print(str(temp.data) + " deleted successfully\n")
            prev.next = temp.next
    def search(self,data):
        flag = False
        count = 0
        temp = self.head
        while temp is not None:
            count +=1
            if temp.data == data:
                flag = True
                print(str(data)+" is found at position"+str(count))
                print("\n")
                return
            else:
                temp = temp.next
        else:
            print(str(data)+" is not found\n")



l = SinglyLinkedList()

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