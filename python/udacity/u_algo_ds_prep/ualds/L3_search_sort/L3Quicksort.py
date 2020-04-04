from L2_list_collectons.LinkedQueue import LinkedQueue

def quicksort(array):
    inplace_quick_sort(array, 0, len(array)-1)
    return array


def inplace_quick_sort(S, a, b):
    """sort the list from S[a] to S[b] inclusive using quick sort algo"""
    if a >= b:  #border case for recursion
        return
    pivot = S[b]    #last el of S selectd as pivot
    left = a
    right = b-1
    while left <= right:
        #scan until value equal or larger than pivot
        while left <= right and S[left] < pivot:
            left +=1
        #scan until value equal or smaller than pivot
        while left <= right and pivot < S[right]:
            right -= 1
        if left <= right:
            S[left], S[right] = S[right], S[left] #swap values in place
            left, right = left + 1, right -1

    #put pivot into its final place (currently at left index
    S[left], S[b] = S[b], S[left]

    print("before recursion: pivot: {0} left: {1}  right: {2}"
          .format(S[left], left, right) )
    #make recursive calls
    inplace_quick_sort(S, a, left - 1)
    inplace_quick_sort(S, left+1, b)


def quick_sort(S):
    """sort elements of queue with quick-sort LinkedQueue class is used
        GTGb
    """
    n = len(S)
    if n < 2:
        return
    #divide
    p = S.first()  #take head el as a pivot
    L = LinkedQueue() # queue to left
    E = LinkedQueue()  # queue for pivot
    G = LinkedQueue()  # queue to right
    while not S.is_empty():
        if S.first() < p:
            L.enqueue(S.dequeue())
        elif p < S.first():
            G.enqueue(S.dequeue())
        else:
            E.enqueue(S.dequeue())
    #conquer with recursion
    quick_sort(L)
    quick_sort(G)
    #concatenate results
    while not L.is_empty():
        S.enqueue(L.dequeue())
    while not E.is_empty():
        S.enqueue(E.dequeue())
    while not G.is_empty():
        S.enqueue(G.dequeue())

def test_inplace_qsort():
    tst_arr = [21, 4, 1, 3, 9, 20, 25, 6, 21, 14]
    print("ini input:", tst_arr)
    res = quicksort(tst_arr)
    print(res)

def test_queue_quick_sort():
    l = LinkedQueue()
    l.enqueue(21)
    l.enqueue(4)
    l.enqueue(1)
    l.enqueue(3)
    l.enqueue(9)
    l.enqueue(20)
    l.enqueue(25)
    l.enqueue(6)
    l.enqueue(21)
    l.enqueue(14)
    print("before sorting")
    l.printQ()
    quick_sort(l)
    print("after sorting")
    l.printQ()


def main():
    #test_inplace_qsort()
    test_queue_quick_sort()

if __name__ == '__main__':
        main()