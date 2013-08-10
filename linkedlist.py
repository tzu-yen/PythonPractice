class Node(object):
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

slist = Node('1', Node('2', Node('3', Node('4', Node('5')))))
print slist.value
print slist.next.value
print slist.next.next.value
