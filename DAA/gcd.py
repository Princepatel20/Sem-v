import time
# Below isusing the itarative method
t1 = time.time()
def itarative(a, b):
    c = a + b

    while c > 0:
        if a % c == 0 and b % c == 0:
            return c
        c -= 1
    return 1

obj = itarative(30,15) 
t2 = time.time()
# Bellow method is using the recursive method

t3 = time.time()
def recursive(a, b):
	if b == 0:
		return a
	else:
		return recursive(b, a % b)
result = recursive(30, 15)
t4 = time.time()
print("GCD using recursiv method is:", result)
print("Execution Time using recursiv :", t4-t3, "seconds")

print ("GCD using itarative method is:",obj)
print("Execution Time using itarative :", t2-t1, "seconds")



#Method to compute GCD ( iterative )
import time
start=time.time()
def gcd(a,b):
	while b:
		a,b = b,a % b
	return a
	end=time.time()
	print("The gcd of 300 and 280is : ")
	print(gcd(300,280))
	print("The Time for Iterative : ")
	print(end-start*60*60)

#Method to compute GCD ( Recursion )
start1=time.time()
def hcf(a,b):
	if(b==0):
		return a
	else:
		return hcf(b,a % b)
end1=time.time()
print("The gcd of 300 and 280 is : ",end="")
print(hcf(300,280))
print("The Time is : ")
print(end1-start1)
