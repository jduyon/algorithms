from partition import partition

def deterministic_partition(A,p,r):
    
    A[r], A[R] = A[R], A[r]
    return partition(A,p,r)
