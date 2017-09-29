def fibonacci(x):
	if x == 0 or x ==1:
		return 1
	else:
		return fibonacci(x-1) + fibonacci(x-2)

print fibonacci(10)

def factorial(x):
	if x == 1: 
		return 1
	else:
		return factorial(x - 1) * x

print factorial(10)