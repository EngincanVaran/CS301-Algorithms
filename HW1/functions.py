def binarySearchIterative(alist,item):
    first = 0
    last = len(alist)-1
    found = False
    while(first<=last and not found):
        midpoint = int((first + last)/2)
        if (alist[midpoint] == item):
            found = True
        else:
            if (item < alist[midpoint]):
                last = midpoint-1
            else:
                first = midpoint+1
    return found

def binarySearchRecursive(alist,item):
    if len(alist) == 0:
        return False
    else:
        midpoint = int(len(alist)/2)
        if alist[midpoint] == item:
            return True
        else:
            if item<alist[midpoint]:
                return binarySearchRecursive(alist[:midpoint],item)
            else:
                return binarySearchRecursive(alist[midpoint+1:],item)

def binarySearch (arr, l, r, x):  
    if r >= l:
        mid = int(l + (r - l)/2)
        if arr[mid] == x: 
            return True 
        elif arr[mid] > x: 
            return binarySearch(arr, l, mid-1, x) 
        else: 
            return binarySearch(arr, mid + 1, r, x)
    else:  
        return False