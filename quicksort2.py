#!/usr/bin/python
import random
import sys, getopt

example_array = [3,1,7,5,4,8,2,13,22,7,100,23,0,4,19,121221,123,1,5345,24]

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

def wrap_partition(A,p,r):
    R = random.choice(range(p,r))
    A[r], A[R] = A[R], A[r]
    return partition(A,p,r)

def quicksort(A,low,high, verbose=True):
    if verbose:
        print "IN:",A
    if low == high or len(A) == 1:
        return
    if low < high:
        p = partition(A,low,high)
        quicksort(A,low, p-1,verbose=verbose)
        quicksort(A,p+1,high,verbose=verbose)
    if verbose:
        print "OUT",A

def f_to_array(f):
    return [int(i.rstrip()) for i in open(f,"r").readlines()]

def help():
    print 'quicksort.py \n\n\t-i <inputfie> or --input-file <inputlist> \n\n\t-v <True/False (default is False)> or --verbose <True/False>\n'
    print "Example array:",example_array
    quicksort(example_array,0,len(example_array)-1,verbose=verbose)
    sys.exit(2)

if __name__ == "__main__":
      argv = sys.argv[1:]
      try:
          opts, args = getopt.getopt(argv,"hi:v:",["input-file=","verbose="])
      except getopt.GetoptError:
          help()
      v = False
      for opt, arg in opts:
          if opt == '-h':
              sys.exit(2)
          elif opt in ("-i", "--input-file"):
              input_array = arg
          elif opt in ("-v","--verbose"):
              v = arg
      input_array = f_to_array(input_array)
      quicksort(input_array,0,len(input_array)-1,verbose=v)
      print input_array
