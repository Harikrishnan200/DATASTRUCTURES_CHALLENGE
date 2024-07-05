class InfixToPostfixConverter:
    def __init__(self):
        self.precedence = {'+': 1, '-': 1, '*': 2, '/': 2, '^': 3}
        self.stack = []
        self.output = []

    def is_operator(self, char):
        return char in self.precedence

    def get_precedence(self, op):
        return self.precedence[op] if op in self.precedence else 0

    def infix_to_postfix(self, expression):
        for char in expression:
            if char.isalnum():  # Operand
                self.output.append(char)
            elif char == '(':  
                self.stack.append(char)
            elif char == ')':  
                while self.stack and self.stack[-1] != '(':
                    self.output.append(self.stack.pop())
                self.stack.pop()  
            else:  # Operator
                while (self.stack and self.stack[-1] != '(' and
                       self.get_precedence(char) <= self.get_precedence(self.stack[-1])):
                    self.output.append(self.stack.pop())
                self.stack.append(char)

        while self.stack:
            self.output.append(self.stack.pop())

        return ''.join(self.output)

expression = "3+(2*4)-5"
converter = InfixToPostfixConverter()
postfix_expression = converter.infix_to_postfix(expression)
print("Infix: ", expression)
print("Postfix: ", postfix_expression)
