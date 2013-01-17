def maxseq(str1):
	bmax = 0
	localmax = 0
	for i in range(len(str1)):
		if str1[i-1]==str1[i]:
			localmax += 1
			if localmax > bmax:
				bmax = localmax
		elif str1[i-1]!=str1[i]:
			localmax = 1

	return bmax
