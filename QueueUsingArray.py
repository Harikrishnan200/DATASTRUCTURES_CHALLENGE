queue =[]
capacity = 0
def enqueue(data):
    if len(queue) == capacity:
        print("Queue is Over flow")
        return 

    else:
        queue.append(data)
        print(f"{data} is successfully pushed onto the stack")

def dequeue():
    if len(queue) == 0:
        print("Queue is underflow")
        return 
    else:
        data = queue.pop(0)
        print(f"{data} is successfully dequeued ")

def displayQueue():
    if len(queue) == 0:
        print("Queue is underflow")
        return 
    else:
        print(queue)


capacity = int(input("Enter the maxi. capacity of the Queue:"))

while True:
    print("\n1.Enqueue")
    print("2.Dequeue")
    print("3.Display Queue")

    choice = int(input("\nEnter your choice:"))
    if choice == 1:
        data = int(input("Enter the data to be pushed:"))
        enqueue(data=data)
    elif choice == 2:
        dequeue()

    elif choice == 3:
        displayQueue()

    else:
        print("Invalid Choice")