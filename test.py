def print_hello_world():
	print('hello world!')

def fib(n):
	fibs = []
	a, b = 0, 1
	for i in range(n):
		a, b = b, a + b
		fibs.append(a)
	return fibs

print(list(fib(10)))

print_hello_world()
>>>>>>> a293542094b97386ad45e526bb35c51029b66063
