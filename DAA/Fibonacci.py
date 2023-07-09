import time
start = time.time()
def fib(n):
	
	if n==0:
		return 0
	elif n == 1:
		return 1
	elif n == 2:
		return 1
	else:
		return fib(n-1)+fib(n-2)
	pass

num = int(input("Enter the number to find fibonacci\n"))
print(fib(num))
end = time.time()
print("Time taken by the recursive method is : ",end-start)
	
start1 = time.time()
def it(num):
	
	a = 0
	b = 1
	if num ==0:
		print(a)
	else:
		print(a)
		print(b)
		for i in range(2,num+1):
			c = a + b
			a = b
			b = c
		print(c)
	end1 = time.time()
	



num1 = int(input("Enter the number to find fibonacci\n"))
it(num1)
end1 = time.time()
print("Time taken by the itrative method is : ",end1-start1)
