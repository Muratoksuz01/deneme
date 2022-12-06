from datetime import datetime as dt
#counting_sort
"""import random as rn
arr=list()# 12.31 dk
for i in range(10):# listeyi ayarladık
    arr.append(rn.randint(1,50))
print("ilk dizi ",arr)
def countingSort(inputArray):
    maxElement= max(inputArray)
    boyut = maxElement+1
    countArray = [0] * boyut
    for el in inputArray: 
        countArray[el] += 1
    for i in range(1, boyut):
        countArray[i] += countArray[i-1] 
    outputArray = [0] * len(inputArray)
    i = len(inputArray) - 1
    while i >= 0:
        currentEl = inputArray[i]
        countArray[currentEl] -= 1
        newPosition = countArray[currentEl]
        outputArray[newPosition] = currentEl
        i -= 1
    return outputArray
inputArray=arr
sortedArray = countingSort(inputArray)
print("Counting sort result = ", sortedArray)"""


#insertion_sort
"""import random as rn
arr=list()# 12.31 dk
for i in range(10):# listeyi ayarladık
    arr.append(rn.randint(1,50))
def insertionSort(arr):
    for i in range(1, len(arr)):
        deger = arr[i]
        j = i-1
        while j >=0 and deger< arr[j] :
                arr[j+1] = arr[j]
                j -= 1
        arr[j+1] = deger
    print(arr)
(insertionSort(arr))"""

#quick_sort
"""import random as rn
arr=list()# 12.31 dk
for i in range(10):# listeyi ayarladık
    arr.append(rn.randint(1,50))
print("ilk listemiz:",arr)


def partition(array, low, high):
  pivot = array[high]
  i = low - 1
  for j in range(low, high):
    if array[j] <= pivot:
      i = i + 1
      (array[i], array[j]) = (array[j], array[i])
  (array[i + 1], array[high]) = (array[high], array[i + 1])
  return i + 1


def quickSort(array, low, high):
  if low < high:
    pi = partition(array, low, high)
    quickSort(array, low, pi - 1)
    quickSort(array, pi + 1, high)


list=arr
size = len(list)
quickSort(list, 0, size-1)
print(list)"""
#selection_sort
"""import random as rn
arr=list()# 12.31 dk
for i in range(10):# listeyi ayarladık
    arr.append(rn.randint(1,50))
print("ilk listemiz:",arr)

buyuk=len(arr)

for j in range(buyuk):
    small=arr[j]
    for k in range(j+1,buyuk):
        if small>arr[k]:
            small=arr[k]
            # temp=arr[j]
            # arr[j]=arr[k]
            # arr[k]=temp
            arr[j],arr[k]=arr[k],arr[j]
        else:
            continue
print(arr)"""

# bublee sort
"""import random as rn
arr=list()
for i in range(10):
    arr.append(rn.randint(1,50))
print("ilk listemiz:",arr)


longht=len(arr)
for j in range(longht-2):
    for i in range(longht-1):
        if arr[i]>arr[i+1]:
            temp=arr[i]
            arr[i]=arr[i+1]
            arr[i+1]=temp
            print(arr)
print("son hali ",arr) """


#radix sort
# Radix sort in Python
"""def countingSort(array, place):
    size = len(array)
    output = [0] * size
    count = [0] * 10
    # Calculate count of elements
    for i in range(0, size):
        index = array[i] // place
        count[index % 10] += 1
    # Calculate cumulative count
    for i in range(1, 10):
        count[i] += count[i - 1]
    # Place the elements in sorted order
    i = size - 1
    while i >= 0:
        index = array[i] // place
        output[count[index % 10] - 1] = array[i]
        count[index % 10] -= 1
        i -= 1
    for i in range(0, size):
        array[i] = output[i]
# Main function to implement radix sort
def radixSort(array):
    # Get maximum element
    max_element = max(array)
    # Apply counting sort to sort elements based on place value.
    place = 1
    while max_element // place > 0:
        countingSort(array, place)
        place *= 10
import random as rn
arr=list()# 
for i in range(1000):# listeyi ayarladık
    arr.append(rn.randint(1,50))
print("ilk dizi ",arr)
radixSort(arr)
print(arr)"""

# Shell sort in python
"""
def shellSort(array, n):
    # Rearrange elements at each n/2, n/4, n/8, ... intervals
    interval = n // 2
    while interval > 0:
        for i in range(interval, n):
            temp = array[i]
            j = i
            while j >= interval and array[j - interval] > temp:
                array[j] = array[j - interval]
                j -= interval
            array[j] = temp
        interval //= 2
import random as rn
arr=list()# 12.31 dk
for i in range(1000):# listeyi ayarladık
    arr.append(rn.randint(1,50))
first=dt.now()
print("ilk dizi ",arr)
size = len(arr)
shellSort(arr, size)
print(dt.now()-first)
print(arr)"""





