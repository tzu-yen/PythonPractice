import re

def test_patterns(text, patterns=[]):
    """Given source text and a list of patterns, look for matches
       for each pattern within the text and print them to stdout"""
    # Look for each pattern in the text and print the results
    for pattern, desc in patterns:
        print 'Pattern %r (%s)\n' % (pattern, desc)
        print '    %r' % text
        for match in re.finditer(pattern, text):
            s = match.start()
            e = match.end()
            substring = text[s:e]
            n_backslashes = text[:s].count('\w')
            prefix = '.' * (s+n_backslashes)
            print '    %s%r' % (prefix, substring)
        print
    return

if __name__ == '__main__':
    test_patterns('abaaabbababaababaababababaababa',
                  [('ab', "'a' followed by 'b'")])
