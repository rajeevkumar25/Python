import plot

def fib(n):
	a,b=0,1
	while b<n:
		print(b,end=' ')
		a,b=b,a+b
	print()
fib(500)

def add(a,b):
	print(a+b)

add(2,5)
x=[1,2,3]
y=[4,5,6]
plot(x,y)

