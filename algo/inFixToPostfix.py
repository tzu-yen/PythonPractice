import stack
import postfixEvaluation

def infixToPostfix(infixexpr):
    prec = {"^":4, "*":3, "/":3, "+":2, "-":2, "(":1}
    opStack = stack.Stack()
    postfixList = []
    tokenList = infixexpr.split()

    for token in tokenList:
        #if token in "ABCDEFGHIJKLMNOPQRSTUVWXYZ" or token in "0123456789":
        if token.isalnum():
            postfixList.append(token)
        elif token == '(':
            opStack.push(token)
        elif token == ')':
            topToken = opStack.pop()
            while topToken != '(':
                postfixList.append(topToken)
                topToken = opStack.pop()
        else:
            while (not opStack.isEmpty()) and prec[token] <= prec[opStack.peek()]:
                  postfixList.append(opStack.pop())
            opStack.push(token)
    while not opStack.isEmpty():
        postfixList.append(opStack.pop())
            
    return " ".join(postfixList)

if __name__ == "__main__":
    print(infixToPostfix("A * B + C * D"))
    print(infixToPostfix("( A + B ) * C - ( D - E ) * ( F + G )"))
    print(infixToPostfix("( A * X + B ) * C / Y - ( D * Z - E ) * ( F + G )"))
    postfix = infixToPostfix("5 * 3 ^ ( 4 - 2 )")
    print postfix
    print postfixEvaluation.postfixEval(postfix)
