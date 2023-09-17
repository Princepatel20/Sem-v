import time
dict = {'1': 'D', '2': 'W', '3': 'A', '4': 'S', '5': 'E', '6': 'U', '7': 'G'}
def ins(dict):
    items = list(dict.items())
    n = len(items)

    for i in range(1, n):
        key = items[i]
        j = i - 1
        while j >= 0 and items[j][1] > key[1]:
            items[j + 1] = items[j]
            j -= 1

        items[j + 1] = key
    sorted = {k: v for k, v in items}
    return sorted

start = time.time()
sorted_dictionary = ins(dict)
end = time.time()
print("sorted element by using insertion sort is:",sorted_dictionary)
print("Time taken by the average case is:",end-start,"sec")


sorted_items = sorted(dict.items(), key=lambda x: x[1])
dict1 = {k: v for k, v in sorted_items}
start1 = time.time()
sorted_dictionary1 = ins(dict1)
end1 = time.time()
print("sorted element by using insertion sort is:",sorted_dictionary1)
print("Time taken by the best case is:",end1-start1,"sec")

dict2 = {k: v for k, v in sorted(dict.items(), key=lambda x: x[1], reverse=True)}
start2 = time.time()
sorted_dictionary2 = ins(dict2)
end2 = time.time()
print("sorted element by using insertion sort is:",sorted_dictionary2)
print("Time taken by the worst case is:",end2-start2,"sec")


#Python program for implementation of Insertion Sort
Import time
Start time
Start=time.time()
def insertion_sort(arr):
    n = len(arr)
    for i in range(1,n):
        #pass i
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
            arr[j + 1] = key
            #print the array after each pass
            print("After pass",i,":",arr)
        end=time.time()

#Driven Code for Average Case:-
print("Average Case: ")
arr = ['D','W','A','S','E','U','G']
insertion_sort(arr)
print("Time Taken: ")
print(end-Start*60*60)

#Driven Code for Best Case:-
print("Best Case: ")
arr = ['A','D','E','G','S','U','W']
insertion_sort(arr)
print("Time Taken: ")
print(end-Start*60*60)

#Driven Code for Worst Case:-
print("Worst Case: ")
arr = ['W','U','S','G','E','D','A']
insertion_sort(arr)
print("Time Taken: ")
print(end-Start*60*60)
