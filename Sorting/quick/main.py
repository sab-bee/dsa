# middle element as pivot

def quickSort(arr, low, high):

    if low >= high:
        return None
    
    pi = partition(arr, low, high)
    quickSort(arr, low, pi-1)
    quickSort(arr, pi+1, high)

def partition(arr, low, high):     

    m = (low+high)//2
    pi = arr[m]
    p = low
    q = high

    while p < q:
        while arr[p] <= pi:
            p+=1
        
        while arr[q] > pi:
            q-=1
        
        if p < q:
            swap(arr, p, q)

    swap(arr, m, q)
    return q

def swap(arr, i, j):
    arr[i], arr[j] = arr[j], arr[i]
    
if __name__ == '__main__':
    arr = [5, 4, 3, 3, 2, 1]
    quickSort(arr, 0, len(arr)-1)
    print(arr)