# Method to compute GCD ( iterative )

import time

start=time.time()

def gcd(a, b): 

 while b: 

 a, b = b, a % b 

 return a

end=time.time()

print("The gcd of 300 and 280 is : ")

print(gcd(300, 280))

print("The Time For Iterative : ")

print(end-start*60*60)

# Method to compute GCD ( Recursion )

start1=time.time()

def hcf(a, b):

if(b == 0):

return a
else:

return hcf(b, a % b)

end1=time.time()

print("The gcd of 300 and 280 is : ", end="")

print(hcf(300, 280))

print("The Time is : ")

print(end1-start1)
