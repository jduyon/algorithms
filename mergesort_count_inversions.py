""" Merge sort involves recursively splitting a list of numbers until 1 number remains. Since when n=1, the list is always sorted,
    and the program moves up the call stack. In this case, the call that just completed, will return a list of (of n=1) and modify
    the 'first' half, then do the same for the 'second' half array variables. Now we have two arrays of n=1 length. Starting from
    the beginning of each array, the program then compares each element from both arrays, (ex: the ith element of 'first' array is
    compared to the jth element of 'second' array. If the first[i] is less than the second[i], then the resulting array 'a' will 
    be append first[i] and only 'i' will be incremented. Only 'i' is incremented because we will also have to compare first[i] to 
    the remainder of second[i] (if there are any elements left). Something to note, if first[i] == second[j] then the element from
    'first' will be appended to 'a', and only 'i' will be incremented. In the case that second[j] is < first[i], we must have an 
    inversion so we increment that count. Since n=1, we skip the while loops below the initial while loop, and return array 'a' 
    back up the call stack. This process is repeated for all merge_sort calls with an array where n=1.
This will only count an inversion if the element in the second half of array is less than (but not equal to) the left half.
"""
import random
def merge_sort(a):
    global inversions
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
                a[k] = second[j]
                trial = second[j]
                j += 1
                inversions += len(first[i:])
#                print ("Inversion:",len(first[i:]),trial)
                  
            k += 1
        while (i < len(first)):
            a[k] = first[i]
            i += 1
            k += 1
        while (j < len(second)):
            a[k] = second[j]
            j += 1
            k += 1
    return a,inversions

a = [int(i.rstrip()) for i in open("IntegerArray.txt","r").readlines()]
#print a
#a=[8,7,6,5,4,3,2,1]
#print merge_sort(a)

inversions = 0
def test_merge_sort():
    global inversions
#    a = [[4,3,2,1],[1,2,3,4,5,6],[1,3,5,2,4,6], [1,5,3,2,4], [5,4,3,2,1], [1,6,3,2,4,5]]
#    for i in xrange(len(a)):
    inversions = 0
    #print "LIST: " + str(a[i])
    print merge_sort(a)

test_merge_sort()
