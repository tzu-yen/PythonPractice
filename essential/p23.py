raise RuntimeError("Computer says no")
try:
    f = open('file.txt', 'r')
except IOError as e:
    print e
