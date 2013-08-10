import random
import re
import string




def generate_sentence():
    return ''.join(random.choice('abcdefghijklmnopqrstuvwxyz ') for i in range(27))

def check_sentence(target, sentence):
    m_count = 0
    for i in range(27):
        m_count = m_count+1 if sentence[i] == target[i] else m_count
    return m_count
    
        
   
    

def check(target):
    best_match = ''
    best_match_count = 0
    for j in range(10000000):
        sentence = generate_sentence()
        match_count = check_sentence(target, sentence)
        if match_count > best_match_count:
            best_match_count = match_count
            best_match = sentence
    return ('True', best_match, best_match_count) if best_match == target else \
           ('False', best_match, best_match_count)

if __name__ == '__main__':
    target = 'methinks it is like a weasel'
    print target
    print '%s, %s, %d' % check(target)
    
