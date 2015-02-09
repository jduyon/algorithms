def choose_pivot():
    return 0

def partition(A, p, r):
    x = A[r]
    i = p-1
    for j in range(p,r-1):
        if A[j] <= x:
            i += 1
            A[i],A[j] = A[j], A[i]
    A[i+1], A[r] = A[r], A[i+1]
    # i+1 is the 'store index'
    return i+1

x = [3,1,7,5,4,8]
print ("X:",x)
print partition(x,0,5)


def quicksort(A,low,high):
    print "IN:",A
    if low < high:
        p = partition(A,low,high)
        quicksort(A,low, p-1)
        quicksort(A,p+1,high)
    print "OUT",A
quicksort(x,0,len(x)-1)
print x

[3,1,2,5,4,8]
1,5
