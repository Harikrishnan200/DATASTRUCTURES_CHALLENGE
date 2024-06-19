class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        self.head = None

    def display(self):
        if self.head is None:
            print('Linked List is empty')
        else:
            temp = self.head
            while temp is not None:
                print(temp.data,'->',end='')
                temp = temp.next

l = SinglyLinkedList()
n = int(input("Enter the no. of nodes:"))

for i in range(n):
    num = int(input("Enter the data:"))
    node = Node(data=num)
    if l.head is None:
        l.head = node
    else:
        temp = l.head
        while temp.next is not None:
            temp = temp.next
        temp.next = node
l.display()


