import stack

def balanceChecker(symbolString):
    s = stack.Stack()
    balanced = True
    index = 0
    while index < len(symbolString) and balanced:
        symbol = symbolString[index]
        if symbol in '([{':
            s.push(symbol)
        else:
            if s.isEmpty():
                balanced = False
            else:
                top = s.pop()
                if not matches(top, symbol):
                    balanced = False
        index += 1

    if balanced and s.isEmpty():return True
    else: return False

def matches(top, symbol):
    if '([{'.index(top) == ')]}'.index(symbol):
        return True
    else: return False
    
        
if __name__ == "__main__":
    symbolString = raw_input('Enter your symbol string: ')
    print balanceChecker(symbolString)
