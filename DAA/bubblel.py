# # Python program for implementation of Bubble Sort
import time
def bubble_sort(dictionary):
    items = list(dictionary.items())
    n = len(items)
    for i in range(n - 1):
        for j in range(n - i - 1):
            if items[j][1] > items[j + 1][1]:
                items[j], items[j + 1] = items[j + 1], items[j]

    sorted = {k: v for k, v in items}
    return sorted

dict = {'1': 89, '2': 42, '3': 100, '4': 93, '5': 11, '6': 234, '7': 30, '8': 82, '9': 22, '10': 75}
start = time.time()
sorted_dict = bubble_sort(dict)
end = time.time()
print("Sorted elements using the bubble sort is: ",sorted_dict)
print("Time taken by avarage case is: ", end-start,"sec")


sorted_items = sorted(dict.items(), key=lambda x: x[1])
dict1 = {k: v for k, v in sorted_items}
start1 = time.time()
sorted_dict1 = bubble_sort(dict1)
end1 = time.time()
print("Sorted elements using the bubble sort is: ",sorted_dict1)
print("Time taken by best case is: ", end1-start1,"sec")

dict2 = {k: v for k, v in sorted(dict.items(), key=lambda x: x[1], reverse=True)}
start2 = time.time()
sorted_dict2 = bubble_sort(dict2)
end2 = time.time()
print("Sorted elements using the bubble sort is: ",sorted_dict2)
print("Time taken by wrost case is: ", end2-start2,"sec")


#Pytho Program for implemention of Bubble Sort
iimport time
start=time.time()
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        #pass i
        for j in range(n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j],arr[j + 1] = arr[j + 1],arr[j]
            #print the array after each pass
            print("Pass",i + 1,":",arr)
        end=time.time()
        #Driver code for Average Case:-
        print("Average Case")
        arr = [89,42,100,93,11,234,30,82,22,75]
        bubble_sort(arr)
        print("Time Taken: ")
        print(end-start*60*60)
        
