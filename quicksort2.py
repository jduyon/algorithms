import random
def choose_pivot():
    return 0

def partition(A, p, r):
    x = A[r]
    i = p-1
    for j in range(p,r):
        if A[j] <= x:
            i += 1
            A[i],A[j] = A[j], A[i]
    A[i+1], A[r] = A[r], A[i+1]
    # i+1 is the 'store index'
    return i+1

x = [3,1,7,5,4,8,2,13,22,7,100,23,0,4,19,121221,123,1,5345,24]
print ("X:",x)
print partition(x,0,5)

def wrap_partition(A,p,r):
    R = random.choice(range(p,r))
    A[r], A[R] = A[R], A[r]
    return partition(A,p,r)

def quicksort(A,low,high):
    print "IN:",A
    if low == high or len(A) == 1:
        return
    if low < high:
        p = partition(A,low,high)
        quicksort(A,low, p-1)
        quicksort(A,p+1,high)
    print "OUT",A

quicksort(x,0,len(x)-1)
print x

