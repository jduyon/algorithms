import random
from partitions.partition import partition
from partitions.randomized_partition import randomized_partition
from inputs.f_to_array import f_to_array

# Partition is a very important algorithm!

def randomselect(A,p,r,selection):
    if p == r or len(A) ==1:
        return A[p]
    q = randomized_partition(A,p,r)
#    print A,"P:",p,"R:",r,"Q:",q,"i:",selection
    k = q - p + 1
    if selection == k:
        return A[q]
    elif selection < k:
        return randomselect(A,p,q-1,selection)
    else:
        return randomselect(A,q+1,r,selection-k)

x=f_to_array('inputs/IntegerArray.txt')

print randomselect(x,0,len(x)-1,5)
