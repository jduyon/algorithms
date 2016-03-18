

ar = [4,5,1,3,9,10]
print ar
def choose_pivot():
    return 0


def partition(list,left_index,right_index):
    """ 
    [P|<P|>P|?]
    
    This algorithm begins by setting up some variables: the pivot element 'p', a position
    tracker 'i' for the position of the right most element that is the end of the less than
    pivot elements. Next, an iterator variable 'j', is created to scan through the array looking
    for elements that are less than pivot number. In the case where such an element is found,
    that element is swapped to the left of the less than tracker 'i'. Finally at the end, the pivot
    element is placed at position 'i-1', which is between the greater than and less than subarrays of numbers.
    """
    pivot = choose_pivot()
    p = list[left_index]
    i = left_index + 1
    # Start J to the right of p
    for j in xrange(i,right_index):
        if list[j] < p:
            list[j],list[i] = list[i], list[j]
            i = i+1
    list[left_index],list[i-1] = list[i-1], list[left_index]
    return i

def quicksort(a,low,high):
    print "recursed"
    if low < high:
        p = partition(a,low,high)
        quicksort(a, low, p-1)
        quicksort(a,p+1,high)
    print a

quicksort(ar,0,len(ar))

#print ar,len(ar)

def qsort2(list):
    print list
    if list == []:
        return []
    else:
        pivot = list[0]
        lesser = qsort2([x for x in list[1:] if x < pivot])
        greater = qsort2([x for x in list[1:] if x >= pivot])
        return lesser + [pivot] + greater
#print qsort2(ar)
