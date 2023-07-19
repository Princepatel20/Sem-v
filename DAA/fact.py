import time
# Below method is iterative method
start2 = time.time()
def iterative_factorial(n):
    fact = 1
    for i in range(n):
        fact = fact * (i+1)
    return fact
    pass
end2 = time.time()
# Below example is recursive method
start3 = time.time()
def recursive_factorial(n):
    if n == 1:
        return 1
    else:
        return n * recursive_factorial(n-1)
end3 = time.time()
t2 = end2-start2
t3 = end3-start3
num = int(input("Enter the number\n"))
print("Factorial using iterative method",iterative_factorial(num))
print("Time taken by the iterative function is: ",t2)
print("Factorial using recursive method is : ", recursive_factorial(num))
print("Time taken by the recursiv function is: ",t3)
