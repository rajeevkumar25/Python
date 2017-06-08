def AlphabetSoup(str):
	str=sorted(str)
	return "".join(str)	

k=AlphabetSoup("hello")
print(k)
