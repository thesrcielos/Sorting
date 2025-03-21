from sorting import constants
import heapq

def selection_sort(list):
    for i in range(len(list) - 1):
        min_element = i
        for j in range(i + 1, len(list)):
            if list[j] < list[min_element]:
                min_element = j
        list[i], list[min_element] = list[min_element], list[i]
    
    return list
"""
def quick_sort(list):
    if len(list) < 2:
        return list
    size = len(list)
    pivot = list[size //2]
    smaller = []
    greater = []
    for i in range(size//2):
        if pivot >= list[i]:
            smaller.append(list[i])
        else:
            greater.append(list[i])
    
    for i in range(size//2 + 1, size):
        if pivot >= list[i]:
            smaller.append(list[i])
        else:
            greater.append(list[i])

    return quick_sort(smaller) + [pivot] + quick_sort(greater)
"""
def quick_sort(arr):
    sort(arr, 0, len(arr) - 1)
    return arr

def sort(arr, low, high):
    if low < high:
        pivot_index = partition(arr, low, high)
        sort(arr, low, pivot_index-1) 
        sort(arr, pivot_index + 1, high)  

def partition(arr, low, high):
    pivot = arr[high]  
    idx = low

    for i in range(low, high):
        if arr[i] <= pivot:
            arr[idx], arr[i] = arr[i], arr[idx]
            idx+=1
    
    arr[idx], arr[high] = pivot, arr[idx]
    return idx

def heap_sort(list):
    heapq.heapify(list)  
    sorted_list = []
    for _ in range(len(list)):
        sorted_list.append(heapq.heappop(list))
    
    return sorted_list