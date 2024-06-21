stack =[]

def pushData(data):
    stack.append(data)
    print(f"{data} is successfully pushed onto the stack")

def popData():
    data = stack.pop()
    print(f"{data} is successfully poped off from the stack")

def displayStack():
    print(stack)


while True:
    print("\n1.Push the data")
    print("1.Pop the data")
    print("1.Display stack")

    choice = int(input("\nEnter your choice:"))
    if choice == 1:
        data = int(input("Enter the data to be pushed:"))
        pushData(data=data)
    elif choice == 2:
        popData()

    elif choice == 3:
        displayStack()

    else:
        print("Invalid Choice")