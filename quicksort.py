

ar = [4,5,1,3,9,10]

def choose_pivot(a,n):
    return 1


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
    p = list[left_index]
    i = left_index + 1
    # Start J to the right of p
    for j in xrange(1,right_index):
        if j > right_index -1:
            break
        if list[j] < p:
            list[j],list[i] = list[i], list[j]
            i = i+1
    list[left_index],list[i-1] = list[i-1], list[left_index]
    return list

def quicksort(a,length):
    print "recursed"
    if length <= 1:
        print a
        return [a]
    else:
        p = choose_pivot(a,length)
        left_a = a[:p]
        right_a = a[p:]
        left_a = partition(left_a,p,len(left_a))
        right_a = partition(right_a,p,len(right_a))
        print left_a,right_a

        return quicksort(left_a,len(left_a)) + [] + quicksort(right_a,len(right_a))

print quicksort(ar,len(ar)-1)

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
