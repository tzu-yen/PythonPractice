class Node(object):
    def __init__(self, initdata):
        self.data = initdata
        self.next = None

    def getData(self):
        return self.data

    def getNext(self):
        return self.next

    def setData(self, newdata):
        self.data = newdata

    def setNext(self, newnext):
        self.next = newnext


class OrderedList(object):
    def __init__(self):
        self.head = None

    def add(self,item):
        previous = None
        current = self.head
        stop = False
        while current != None and not stop:
            if current.getData() > item:
                stop = True
            else:
                previous = current
                current = current.getNext()
                
        temp = Node(item)
        if previous == None:
            temp.setNext(self.head)
            self.head = temp
        else
            previous.setNext(temp)
            temp.setNext(current)
    
    def remove(self, item):
        current = self.head
        previous = None
        found = False
        while not found:
            if current.getData() == item:
                found = True
            else:
                previous = current
                current = current.getNext()
        if current == self.head:
            self.head = current.getNext()
        else:
            previous.setNext(current.getNext())
            
    def search(self, item):
        current = self.head
        found = False
        stop = False
        while current != None and not found and not stop:
            if current.getData() == item:
                found = True
            elif current.getData() > item:
                stop = True
            else:
                current = current.getNext()
        return found
    
    def isEmpty(self):
        return self.head == None
    
    def length(self):
        count = 0
        current = self.head
        while current != None:
            currect = current.getNext()
            count +=1
        return count
    def index(self, item):
        pass
    def pop(self):
        pass
    def pop(self, pos):
        pass
