import math
def TimeConvert(num):
	hr=int(num/60)
	minu=num%60
	return str(hr) + ":" + str(minu)
k=TimeConvert(1)
print(k)