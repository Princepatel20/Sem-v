import time

start = time.time()
def fib(n):
	
	if n<=1:
		return n
	else:
		return fib(n-1)+fib(n-2)
	
end = time.time()

	
start1 = time.time()
def it(num):
	
	a = 0
	b = 1
	if num ==0:
		print(a)
	else:
		# print(a)
		# print(b)
		for i in range(2,num+1):
			c = a + b
			a = b
			b = c
		print("Fibonacii using  itrative",c)
end1 = time.time()



num = int(input("Enter the number to find fibonacci\n"))
it(num)
print("Fibonacii using  recursive",fib(num))
print("Time taken by the itrative method is : ",end1-start1)
print("Time taken by the recursive method is : ",end-start)
