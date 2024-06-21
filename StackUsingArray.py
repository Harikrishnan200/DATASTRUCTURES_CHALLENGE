stack =[]

def pushData(data):
    stack.append(data)
    print(f"{data} is successfully pushed onto the stack")

def popData():
    if len(stack) == 0:
        print("Stack is empty")
        return
    else:
        data = stack.pop()
        print(f"{data} is successfully poped off from the stack")

def displayStack():
    if len(stack) == 0:
        print("Stack is empty")
        return
    else:
        print("Stack elements are:")
        for i in range(len(stack)-1,-1,-1):
            print(stack[i])


while True:
    print("\n1.Push the data")
    print("2.Pop the data")
    print("3.Display stack")

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