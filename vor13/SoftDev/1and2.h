
def maxdiff(list)
	md = 0
	last = list.pop(0)
	for i in list:
		if (abs(i - last) > md):
			md = abs(i - last)
	return md


