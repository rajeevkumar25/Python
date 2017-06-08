class myClass:
	def firstMethod(__self__,a):
		print(type(__self__))
		print(a)
	def secondMethod():
		print('I am in second method!')

	#firstMethod()
	#secondMethod()

myClass.firstMethod(0,7)
myClass.secondMethod()




