def insertionSort(arr):
    n = len(arr)
    i = 0
    while i < n:
        j = i-1
        temp = arr[i]
        while j >= 0 and temp < arr[j]:
            arr[j+1] = arr[j]
            j-=1
        arr[j+1] = temp
        i+=1

if __name__ == '__main__':
    arr = [4, 5, 7,1, 4, 6, 2, 8]
    insertionSort(arr)
    print(arr)