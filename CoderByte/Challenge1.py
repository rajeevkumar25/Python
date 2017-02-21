def letstry(str):
	newstr=""	
	for ltr in str:
		if (ord(ltr) >= 97 and ord(ltr) <=122):
			newchar=chr(ord(ltr)+1)
			#print(newchar)
			newstr=newstr+newchar
			#print(newstr)
			if newchar in ("aeiou"):
				newstr=""
				newchar=newchar.upper()
			#	print(newchar)
				newstr=newstr+newchar
	return newstr						

k=letstry("dog")
print(k)
