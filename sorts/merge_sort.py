from inputs.f_to_array import f_to_array
from optparse import OptionParser
import sys

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
class MergeSort(object):
    def __init__(self, count_inversions=False):
        self.inversions = 0
        self.count_inversions = count_inversions

    def merge_sort(self,a):
        mid = len(a) / 2
        if len(a) > 1:
            first = a[:mid]
            second = a[mid:]
            self.merge_sort(first)
            self.merge_sort(second)
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
                    self.inversions += len(first[i:])
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
        if self.count_inversions:
            return a,self.inversions
        else:
            return a

def helper():
    doc = """ mergesort_with_inversions.py

        -i <inputfilepath> or --input-file <inputfilepath>

        -v (default is False)> or --verbose

        -c or --count-inversions

    merge_sort_wrapper(example_array,0,len(example_array)-1,verbose=verbose)
    """
    sys.exit(2)

if __name__ == "__main__":
    parser = OptionParser()
    parser.add_option("-i", "--input-file", dest="input_file",
                      help="Full path to input file.")
    parser.add_option("-v", "--verbose", dest="verbose",
                      action='store_true',help="Verbosity mode!")
    parser.add_option("-c", "--count-inversions", dest="inversion_count",
                      action='store_true',help="Count number of times" \
                         "there was an inversion.")

    (opts, args) = parser.parse_args()
    if not opts.input_file:
        helper()
        quit()
    if not opts.verbose:
        v = False
    else:
        v = opts.verbose
    input_array = f_to_array(opts.input_file)
    sort = MergeSort(opts.inversion_count)
    output = sort.merge_sort(input_array)
    print output

