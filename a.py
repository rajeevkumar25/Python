def outer():
	x=1
	def inner():
		nolocal x
		x=5
		y=2
		print('inner x and y is:',x,y)
	inner()
	print('outer x is:',x)
outer()
