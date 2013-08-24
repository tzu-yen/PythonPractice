import stack

def postfixEval(postfixExpr):
    operandStack = stack.Stack()
    tokenList = postfixExpr.split()
    for token in tokenList:
        if token.isdigit():
            operandStack.push(int(token))
        else:
            operand2 = operandStack.pop()
            operand1 = operandStack.pop()
            result = doMath(operand1, operand2, token)
            operandStack.push(result)
    return operandStack.pop()

def doMath(op1, op2, op):
    if op == '+': return op1 + op2
    elif op == '-': return op1 - op2
    elif op == '*': return op1 * op2
    elif op == '/': return op1 / op2
    elif op == '^': return op1 ** op2


if __name__ == "__main__":
    postfixExpr = raw_input("Enter postfix expression: ")
    print postfixEval(postfixExpr)
