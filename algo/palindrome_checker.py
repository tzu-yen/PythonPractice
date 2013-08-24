from deque import Deque

def palindrome_checker(word):
    word_deque = Deque()
    for c in word:
        word_deque.addRear(c)

    stillEqual = True
    while word_deque.size() > 1:
        if word_deque.removeRear() != word_deque.removeFront():
            stillEqual = False
            break
    return stillEqual

print(palindrome_checker("lsdkjfskf"))
print(palindrome_checker("radar"))
        
