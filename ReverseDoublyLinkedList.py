class Node:
    def __init__(self,data):
        self.data = data
        self.prev = None
        self.next = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def display(self):
        if self.head is None:
            print("List is empty")
        else:
            temp = self.head
            while temp is not None:
                print(temp.data, "->", end="")
                temp = temp.next
            print()

    def insert_node(self,data):
        node = Node(data)
        if self.head is None:
            self.head = node
        else:
            temp = self.head
            while temp.next is not None:
                temp = temp.next

            node.prev = temp
            temp.next = node

    def reverse(self):
        if self.head is None:
            print("List is empty")
        else:
            temp = None
            current_node = self.head
            # Swap the prev and next of each node
            while current_node is not None:
                temp = current_node.prev
                current_node.prev = current_node.next
                current_node.next = temp
                current_node = current_node.prev

            # Update the head
            if temp is not None:
                self.head = temp.prev

dl = DoublyLinkedList()
while True:
    print("1. Insertion")
    print("2. Traverse")
    print("3. Reverse the list")
    choice = int(input("\nEnter your choice:"))

    if choice == 1:
        data = int(input("\nEnter the data"))
        dl.insert_node(data)
    elif choice == 2:
        dl.display()
    elif choice == 3:
        dl.reverse()

