def pump(str1):
	arr = list(str1)
	inc = 0
	for i in arr:
		if i.isdigit():
			n = int(i)
			l = arr[inc+1]
			arr[inc] = arr[inc+1]
			for x in range(n-1):
				arr.insert(inc,l)
		inc += 1

	return ''.join(arr)
