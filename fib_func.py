#function declaration 

def fib(n):
	a, b=0,1
	while(a < n): 
		print(a)
		a, b =b, a+b
#fib(200)

def fib2(n):
	a, b =0, 1
	result = []
	while(a<n):
	     result.append(a)
	     a,b = b, a+b
	return result

fib100 = fib2(10)
print(fib100)

#classes in python 
##class myEmptyClass:
#	pass
	

