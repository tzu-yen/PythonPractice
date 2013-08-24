class Stack(object):
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[-1]

    def size(self):
        return len(self.items)


def reverseString(string):
    s = Stack()
    for w in string:
        s.push(w)
    r_string =''
    while not s.isEmpty():
        r_string += s.pop()
    return r_string

if __name__ == "__main__":
    string = raw_input("Enter a string: ")
    print "the reverse of what you enter is: %s" % reverseString(string)
        

    
