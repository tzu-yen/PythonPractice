line = "Google, 100, 490.10"
field_type = [str, int, float]
raw_fields = line.split(',')
fields = [t(f) for t,f in zip(field_type, raw_fields)]
print fields
