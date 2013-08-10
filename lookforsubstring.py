def grep(lines, searchtext):
    for line in lines:
        if searchtext in line:
            yield line
    
