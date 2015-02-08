

a = [4,5,1,3,9,10]


def choose_pivot(a,n):
    return 1

def quicksort(a,length):
    if length <= 1:
        return
    else:
        p = choose_pivot(a,length)
        left_a = a[:p]
        right_a = a[p:]
        quicksort(left_a,len(left_a))
        quicksort(right_a,len(right_a))
        new_left = []
        new_right = []
        i=0
        j=0
        while i < len(right_a) and j < len(left_a):
            if right_a[i] > a[p]:
                print right_a[i],a[p]
                new_right.append(right_a[i])
                i += 1
            else:
                print left_a[i],a[p]
                new_left.append(left_a[i])
                j += 1
        return [new_left,new_right]

print quicksort(a,6)
