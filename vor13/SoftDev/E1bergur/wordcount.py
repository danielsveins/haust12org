def wordcount(file1):
	infile = file(file1, 'r')
	content = infile.read()
	c2 = content.split()
	count = len(c2)
	dic = []
	for i in c2:
		if i not in dic:
			dic.append(i)

	return (count, len(dic))

