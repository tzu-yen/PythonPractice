import stack2

s2 = stack2.Stack2()
s2.push('a')
s2.push(1)
s2.push([2,3,4])

print len(s2)
print s2.pop()
print s2.pop()
print len(s2)
