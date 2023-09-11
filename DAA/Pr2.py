# Python program for implementation of Bubble Sort

import time 

start=time.time()

def bubble_sort(arr):

 n = len(arr)

 for i in range(n):

 # pass i

 for j in range(n - i - 1):

 if arr[j] > arr[j + 1]:

 arr[j], arr[j + 1] = arr[j + 1], arr[j]

 # print the array after each pass

 print("Pass", i + 1, ":", arr)

end=time.time()

#Driver Code for Average Case:-

print(“Average Case”)

arr = [89,42,100,93,11,234,30,82,22,75]

bubble_sort(arr)

print(“Time Taken: ”)

print(end-start*60*60)
#Driver Code for Best Case:-

print(“Best Case”)

arr = [11,22,30,42,75,82,89,93,100,234]

bubble_sort(arr)

print(“Time Taken: ”)

print(end-start*60*60)
#Driver Code for Worst Case:-

print(“Worst Case”)

arr = [234,100,93,89,82,75,42,30,22,11,]

bubble_sort(arr)

print(“Time Taken: ”)

print(end-start*60*60)
