# Method to compute FIB ( iterative )

Import time

S=time.time()

def fact(n):

 result = 1

 for i in range(1, n+1):

 result *= i

 print(result)

E=time.time()

a=int(input("Enter a number: "))

print(“Factorial is: ”)

fact(a)

print(“Time for Iterative is: ”)

print(E-S*60*60)

# Method to compute FIB ( Recursive )

s=time.time()

def factorial(n):

 if n == 0:

 return 1

else:
return n * factorial(n-1)

e=time.time()

n = int(input("Enter a number: "))

print("Factorial is: ”)

print(factorial(n))

print(“Time for recursive is: ”)
