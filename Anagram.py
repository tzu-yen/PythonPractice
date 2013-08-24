def anagram(s1, s2):
    c1 = [0] * 26
    c2 = [0] * 26

    for i in range(len(s1)):
        pos = ord(s1[i]) - ord('a')
        c1[pos]+=1

    for j in range(len(s2)):
        pos = ord(s2[j]) - ord('a')
        c2[pos] += 1

    for k in range(26):
        if c1[k] !=c2[k]:
            return False
    else: return True
        
print anagram('python', 'pnothy')
