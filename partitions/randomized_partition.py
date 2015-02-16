from partition import partition
import random

def randomized_partition(A,p,r):
    R = random.choice(range(p,r))
    A[r], A[R] = A[R], A[r]
    return partition(A,p,r)

