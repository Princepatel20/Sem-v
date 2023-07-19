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
