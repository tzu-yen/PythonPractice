import string

values = {'var':'foo'}

t = string.Template("""
Variable : $var
Escape  :$$
VAriable in text: ${var}iable
""")

print 'Template:', t.substitute(values)
