def linecount(cfile):
    # fill in code
    # ...
    infile = file(cfile, 'r')
    content = infile.read()
    n = content.count('\n')
    return n

 
