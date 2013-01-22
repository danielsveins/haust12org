ciph = '''g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj.
'''

def pycha(str1):
	new = ''
	for i in range(len(str1)):
		num = ord(str1[i])
		num += 2
		if str1[i].isalpha():
	#		new+=(chr(ord(str1[i])+2))
			if str1[i].isupper():
				if num > ord('Z'):
					num -= 26
				elif num < ord('A'):
					num += 26
			elif str1[i].islower():
				if num > ord('z'):
					num -= 26
				elif num < ord('a'):
					num += 26
			new += chr(num)
		else:
			new+=str1[i]
	return new
