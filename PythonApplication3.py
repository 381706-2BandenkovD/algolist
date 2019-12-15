# -*- coding: utf-8 -*-
import time
import numpy as np
import matplotlib.pyplot as plt

'''  D HEAP SORT '''
def dheaping(arr, ind, size, d):
    first_child = ind * d + 1                                         
    if first_child < size:
        last_child = first_child                                                
        i = 1                                       
        while (i <= d-1):                                              
            if first_child+i < size and arr[first_child+i] > arr[last_child]:  
                last_child = first_child + i                                    
                i += 1
            else:
                i += 1
        if arr[ind] < arr[last_child]:                                     
           arr[ind], arr[last_child] = arr[last_child], arr[ind]                                      
           dheaping(arr, last_child, size, d) 

def heapsort(arr, d):
    n = len(arr)
    for i in range(n // 2 - 1, -1, -1):      
        dheaping(arr, i, n, d)    
    for i in range(n-1, 0, -1):       
        arr[i], arr[0] = arr[0], arr[i]            
        dheaping(arr, 0, i, d) 


'''  QUICK HOARE SORT '''
def partition(arr, low, high):  
    pivot = arr[(low + high) // 2]
    i = low - 1
    j = high + 1
    while True:
        i += 1
        while arr[i] < pivot:
            i += 1
        j -= 1
        while arr[j] > pivot:
            j -= 1

        if i >= j:
            return j

        arr[i], arr[j] = arr[j], arr[i]

def quick_sort(arr):  
    def _quick_sort(items, low, high):
        if low < high:
            split_index = partition(items, low, high)
            _quick_sort(items, low, split_index)
            _quick_sort(items, split_index + 1, high)

    _quick_sort(arr, 0, len(arr) - 1)

#######################################################################
qTime = list()
dHeapTime = list()
arr2k = list()
arr2k = np.random.randint(0, 10000, 2000)
arr4k = list()
arr4k = np.random.randint(0, 10000, 4000)
arr6k = list()
arr6k = np.random.randint(0, 12000, 6000)
arr8k = list()
arr8k = np.random.randint(0, 16000, 8000)
arr10k = list()
arr10k = np.random.randint(0, 20000, 10000)
arr15k = list()
arr15k = np.random.randint(0, 30000, 15000)
#######################################################################
print("____________________D_Heap_Sort________________________")
d = 7
arr = [32, 24, 2, 6, 23, 4, 151, 2, 843, 9]
arr2 = [ 32, 24, 2, 6, 23, 4, 151, 2, 24, 6, 2, 91, 64, 47, 80, 68, 66, 93, 91, 31, 16, 3, 62, 32, 9, 23, 49, 76, 69, 49, 25, 14, 90 ]
heapsort(arr,d)
heapsort(arr2,d)
print("Heapsort 10 elem ", arr)
print("Heapsort 33 elem ", arr2)
dHS2k = arr2k
t1 = time.process_time()
heapsort(dHS2k, d)
print("Heapsort 2000 elem took %f seconds" % ((time.process_time()-t1)))
dHeapTime.append(time.process_time()-t1)

dHS4k = arr4k
t1 = time.process_time()
heapsort(dHS4k, d)
print("Heapsort 4000 elem took %f seconds" % ((time.process_time()-t1)))
dHeapTime.append(time.process_time()-t1)

dHS6k = arr6k
t1 = time.process_time()
heapsort(dHS6k, d)
print("Heapsort 6000 elem took %f seconds" % ((time.process_time()-t1)))
dHeapTime.append(time.process_time()-t1)

dHS8k = arr8k
t1 = time.process_time()
heapsort(dHS8k, d)
print("Heapsort 8000 elem took %f seconds" % ((time.process_time()-t1)))
dHeapTime.append(time.process_time()-t1)

dHS10k = arr10k
t1 = time.process_time()
heapsort(dHS10k, d)
print("Heapsort 10000 elem took %f seconds" % ((time.process_time()-t1)))
dHeapTime.append(time.process_time()-t1)

dHS15k = arr15k
t1 = time.process_time()
heapsort(dHS15k, d)
print("Heapsort 15000 elem took %f seconds" % ((time.process_time()-t1)))
dHeapTime.append(time.process_time()-t1)

print("____________________Quick_Sort__________________________")
ar = [32, 24, 2, 6, 23, 4, 151, 2, 843, 9]
ar1 = [ 32, 24, 2, 6, 23, 4, 151, 2, 24, 6, 2, 91, 64, 47, 80, 68, 66, 93, 91, 31, 16, 3, 62, 32, 9, 23, 49, 76, 69, 49, 25, 14, 90 ]
quick_sort(ar)
quick_sort(ar1)
print("Quick Sort 8 elem ", ar)
print("Quick Sort 33 elem ", ar1)

qS2k = arr2k
t = time.process_time()
quick_sort(qS2k)
print("Quick Sort 2000 elem took %f seconds" % ((time.process_time()-t)))
qTime.append(time.process_time()-t)

qS4k = arr4k
t = time.process_time()
quick_sort(qS4k)
print("Quick Sort 4000 elem took %f seconds" % ((time.process_time()-t)))
qTime.append(time.process_time()-t)

qS6k = arr6k
t = time.process_time()
quick_sort(qS6k)
print("Quick Sort 6000 elem took %f seconds" % ((time.process_time()-t)))
qTime.append(time.process_time()-t)

qS8k = arr8k
t = time.process_time()
quick_sort(qS8k)
print("Quick Sort 8000 elem took %f seconds" % ((time.process_time()-t)))
qTime.append(time.process_time()-t)

qS10k = arr10k
t = time.process_time()
quick_sort(qS10k)
print("Quick Sort 10000 elem took %f seconds" % ((time.process_time()-t)))
qTime.append(time.process_time()-t)

qS15k = arr15k
t = time.process_time()
quick_sort(qS15k)
print("Quick Sort 15000 elem took %f seconds" % ((time.process_time()-t)))
qTime.append(time.process_time()-t)

print("____________________Graphic________________________")
sh = [len(arr2k), len(arr4k), len(arr6k), len(arr8k), len(arr10k), len(arr15k)]
plt.title('Sort Comparison') 
plt.ylabel('execution time')
plt.xlabel('amount of elements')
p1, = plt.plot(sh, qTime)
p2, = plt.plot(sh, dHeapTime)
plt.legend([p1,p2], ["Quick Sort","D Heap Sort"], loc=2) 
plt.grid(True)
plt.show()