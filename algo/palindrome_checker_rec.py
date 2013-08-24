def palindrome_check(string):
    if len(string) == 1: return True
    elif len(string) == 2 and string[0] == string[1]: return True
    else:
        if string[0] == string[-1]:
            return palindrome_check(string[1:len(string)-1])
        else: return False

print palindrome_check('kayak')
print palindrome_check('aibohphobia')
print palindrome_check('live not on evil')
print palindrome_check('able was I ere I saw elba')
print palindrome_check('kanakanak')
print palindrome_check('test')
    
