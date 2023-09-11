# Method to compute FIB ( iterative )

import time 

start=time.time()

def fibonacci(n): 

 a = 0

 b = 1

 for i in range(n+1): 

 print(a, end = " ") 

 a, b = b, a + b

end= time.time()

n = int(input("Enter the number of terms: ")) 

fibonacci(n)

print("Time For Iterative: ")

print(end-start*60*60)

#Method to compute FIB ( Recursion )

start1=time.time()

def fibonacci(n):

 if n <= 1:

 return n

 return fibonacci(n - 1) + fibonacci(n - 2)

end1=time.time()

n = int(input("Enter a number: "))

print(fibonacci(n))

print("Time for Recursion: ")

print(end1-start1*60*60)
