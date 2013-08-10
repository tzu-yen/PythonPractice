import re

print '='*10, 'search', '='*10
pattern = 'this'
text = 'Does this text match the pattern?'

match = re.search(pattern, text)
s = match.start()
e = match.end()

print 'Found "%s"\nin "%s"\n from %d to %d ("%s")' % \
      (match.re.pattern, match.string, s, e, text[s:e])


print '='*10, 'findall', '='*10

text2 = 'abbaaabbbbaaaaa'
pattern = 'ab'

for match in re.findall(pattern, text2):
    print 'Found "%s"' % match

for match_object in re.finditer(pattern, text2):
    s = match_object.start()
    e = match_object.end()
    print 'Found "%s" at %d: %d' % (match_object.re.pattern, s, e)
