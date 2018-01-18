#!/usr/bin/python
import random
import sys, getopt
from optparse import OptionParser
from inputs.f_to_array import f_to_array
example_array = [3,1,7,5,4,8,2,13,22,7,100,23,0,4,19,121221,123,1,5345,24]

class QuickSort(object):
    def __init__(self,verbose=False):
        self.verbose = verbose

    def choose_pivot(self):
        return 0

    def partition(self, A, p, r):
        """
        This algorithm begins by setting up some variables: the pivot element 'p', a position
        tracker 'i' for the position of the right most element that is the end of the less than
        pivot elements. Next, an iterator variable 'j', is created to scan through the array looking
        for elements that are less than pivot number. In the case where such an element is found,
        that element is swapped to the left of the less than tracker 'i'. Finally at the end, the pivot
        element is placed at position 'i-1', which is between the greater than and less than subarrays of numbers.
        [P | <P | >P | ? ]
        """
        x = A[r]
        i = p-1
        for j in range(p,r):
            if A[j] <= x:
                i += 1
                A[i],A[j] = A[j], A[i]
        A[i+1], A[r] = A[r], A[i+1]
        # i+1 is the 'store index'
        return i+1

    def wrap_partition(self, A,p,r):
        R = random.choice(range(p,r))
        A[r], A[R] = A[R], A[r]
        return self.partition(A,p,r)

    def quicksort(self, A,low,high):
        if self.verbose:
            print "IN:",A
        if low == high or len(A) == 1:
            return
        if low < high:
            p = self.partition(A,low,high)
            self.quicksort(A,low, p-1)
            self.quicksort(A,p+1,high)
        if self.verbose:
            print "OUT",A
        return A

def helper():
    doc = """quicksort.py

        -i <inputfiepath> or --input-file <inputfilepath>
        -v (default is False)> or --verbose

    QuickSort().quicksort(example_array,0,len(example_array)-1,verbose=verbose)
    """
    sys.exit(2)

if __name__ == "__main__":
    parser = OptionParser()
    parser.add_option("-i", "--input-file", dest="input_file",
                      help="Full path to input file.")
    parser.add_option("-v", "--verbose", dest="verbose",
                      action='store_true',help="Verbosity mode!",default=False)

    (opts, args) = parser.parse_args()
    if not opts.input_file:
        helper()
        quit()
    input_array = f_to_array(opts.input_file)
    sort = QuickSort(verbose=opts.verbose)
    print sort.quicksort(input_array,0,len(input_array)-1)
