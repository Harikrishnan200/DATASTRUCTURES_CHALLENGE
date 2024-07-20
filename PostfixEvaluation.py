def evaluate_postfix(expression):
    stack = []
    
    for token in expression.split():
        if token.isdigit():  
            stack.append(int(token))
        else: 
            operand2 = stack.pop()
            operand1 = stack.pop()

            if token == '+':
                stack.append(operand1 + operand2)
            elif token == '-':
                stack.append(operand1 - operand2)
            elif token == '*':
                stack.append(operand1 * operand2)
            elif token == '/':
                stack.append(int(operand1 / operand2)) 
            else:
                raise ValueError(f"Unknown operator: {token}")

    return stack.pop()

expression = "3 4 + 2 * 7 /" 
result = evaluate_postfix(expression)
print(f"The result of the postfix expression '{expression}' is {result}")
