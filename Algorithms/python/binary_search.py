def binary_search(alist, item):
    """
    returns the index where the item is in alist. O(logn) time
    alist must be in ascending order
    # returns the index of element closest to the item that is still <= item in alist
    """
    first = 0
    last = len(alist)-1
    found = False
    while first <= last and not found:
        midpoint = (first + last)//2
        if alist[midpoint] == item:
            found = alist[midpoint]
        # elif alist[midpoint-1] <= item < alist[midpoint]:
        #     found = alist[midpoint-1]
        else:
            if item < alist[midpoint]:
                last = midpoint-1
            else:
                first = midpoint+1
    return found
