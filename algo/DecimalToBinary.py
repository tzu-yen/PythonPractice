import stack


def decTobin(number):
    binaryStack = stack.Stack()
    while(number != 0):
        binaryStack.push(number%2)
        number = number / 2
    binaryString = ''
    while not binaryStack.isEmpty():
        binaryString += str(binaryStack.pop())
    return binaryString
        
if __name__ == "__main__":
    decim = raw_input("Enter a decimal: ")
    print decTobin(int(decim))
