import random
from partitions.partition import partition
from partitions.randomized_partition import randomized_partition
from files.f_to_array import f_to_array

# Partition is a very important algorithm!

def deterministicselect(A,p,r,selection):
    if p == r or len(A) ==1:
        return A[p]
    
    q = partition(A,p,r)
#    print A,"P:",p,"R:",r,"Q:",q,"i:",selection
    k = q - p + 1
    if selection == k:
        return A[q]
    elif selection < k:
        return randomselect(A,p,q-1,selection)
    else:
        return randomselect(A,q+1,r,selection-k)

x=f_to_array('inputs/small_integers.txt')

#print randomselect(x,0,len(x)-1,5)

def split_array(A,n):
    print len(A)
    for i in range(0,n):
        y = 0 + (len(A) / n)*i
        x = 0 + (len(A) / n)*(i+1)
        if i < 1:
            print i,y,x
            print A[:len(A)/n]
        elif i == n-1:
            print i,y,x
            print A[x:]
        else:
            print i,y,x
            print A[y:x]
split_array(x,3)
