#!/usr/bin/python
import random
import sys, getopt
from optparse import OptionParser
from inputs.f_to_array import f_to_array
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

def helper():
    print 'quicksort.py \n\n\t-i <inputfie> or --input-file <inputlist> \n\n\t-v <True/False (default is False)> or --verbose <True/False>\n'
    print "Example array:",example_array
    print "quicksort(example_array,0,len(example_array)-1,verbose=verbose)"
    sys.exit(2)

if __name__ == "__main__":
    parser = OptionParser()
    parser.add_option("-i", "--input-file", dest="input_file",
                      help="Full path to input file.")
    parser.add_option("-v", "--verbose", dest="verbose",
                      help="Verbosity mode!")

    (opts, args) = parser.parse_args()
    if not opts.input_file:
        helper()
        quit()
    if not opts.verbose:
        v = False
    else:
        v = opts.verbose
    input_array = f_to_array(opts.input_file)
    quicksort(input_array,0,len(input_array)-1,verbose=v)
    print input_array
