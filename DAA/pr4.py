import time
import random
s = time.time()
def generate_random_array(n):
return [random.randint(1, 10000) for _ in range(n)]
def quick_sort(arr):
if len(arr) <= 1:
return arr
pivot = arr[len(arr) // 2]
left = [x for x in arr if x < pivot]
middle = [x for x in arr if x == pivot]
right = [x for x in arr if x > pivot]
return quick_sort(left) + middle + quick_sort(right)
arr = generate_random_array(10000)
e = time.time()
sorted_arr = quick_sort(arr)
print("Sorted array (first 10 elements):", sorted_arr[:10])
print("Excution Time for Best Case:"+str((e-s)*60*60))
