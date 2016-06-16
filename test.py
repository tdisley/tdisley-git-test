def print_hello_world():
	print('hello world!')

def fib(n):
	a, b = 0, 1
	for i in range(n):
		a, b = b, a + b
		yield a

print(list(fib(10)))

print_hello_world()