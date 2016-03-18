""" Merge sort involves recursively splitting a list of numbers until 1 number remains. Since a n=1 list is always sorted,
    it moves up the moves up the call stack and 
"""
import random
def merge_sort(a):
    mid = len(a) / 2
    if len(a) > 1:
        first = a[:mid]
        second = a[mid:]
        merge_sort(first)
        merge_sort(second)
        i = 0
        j = 0
        k = 0
        while (i < len(first) and j < len(second)):
            if first[i] < second[j]:
                a[k] = first[i]
                i += 1
            else:
                #second[j] < first[i]:
                a[k] = second[j]
                j += 1
            k += 1
        while (i < len(first)):
            a[k] = first[i]
            i += 1
            k += 1
        while (j < len(second)):
            a[k] = second[j]
            j += 1
            k += 1
    return a

a = random.sample(range(1,3000000),100000)
print merge_sort(a)
