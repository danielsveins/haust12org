Xlist = ['kex', 'xylofonn', 'epli','xenos','asni']

def xsort(str1):
	
	p2 = str1
	p2.sort()
	# str.startswith('x')
	new = []
	delList = []
	for x in range(len(p2)):
		if p2[x].startswith('x') or p2[x].startswith('X'):
			new.append(p2[x])
			delList.append(x)
			
	for i in range(len(delList)):
		del p2[delList[i]]
		p2.reverse()
		p2.append(new[i])
		p2.reverse()
	return new + p2
