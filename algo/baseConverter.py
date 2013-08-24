import stack


def baseConverter(decNumber, base):
    digits = "0123456789ABCDEF"

    remstack = stack.Stack()
    while decNumber > 0:
        remstack.push(digits[decNumber % base])
        decNumber /= base
    convertedResult = ''
    while not remstack.isEmpty():
        convertedResult += str(remstack.pop())
    return convertedResult

if __name__ == "__main__":
    decNumber = int(raw_input("Enter the Number: "))
    base = int(raw_input("Enter the Base: "))

    print baseConverter(decNumber, base)
