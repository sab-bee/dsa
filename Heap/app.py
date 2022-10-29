def insertHeap(arr, n, data):
    arr.append(data)

    while n+1 > 1:
        if data > arr[n//2]:
            swap(arr, n, n//2)
            n = n//2
        else:return

def deleteHeap(arr, n):
    i = 0 # is root at first
    parentOfLast = (n-1)//2 # store parent of the last element
    swap(arr, i, n-1) # swap the last element with the root element

    while i < parentOfLast:

        leftChild = i*2+1 # of current
        rightChild = i*2+2 # of current

        if arr[leftChild] > arr[rightChild]:
            swap(arr, i, leftChild)
            i=leftChild
        else:
            swap(arr, i, rightChild)
            i=rightChild
    arr.pop()

def swap(arr, i, j):
    arr[i],arr[j]=arr[j],arr[i]

if __name__ == '__main__':
    arr = [14, 12, 8, 6, 7, 5, 4]
    insertHeap(arr, len(arr), 20)
    print(arr)
    deleteHeap(arr, len(arr))
    print(arr)
    deleteHeap(arr, len(arr))
    print(arr)