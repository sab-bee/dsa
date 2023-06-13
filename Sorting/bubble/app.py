def bubbleSort(arr):
    n = len(arr)
    flag = False
    for i in range(n-1):
        for j in range(n-i-1):
            if arr[j] > arr[j+1]:
                flag = True
                swap(arr, j, j+1)
        if not flag:
            return

def swap(arr, i, j):
    arr[i], arr[j] = arr[j], arr[i]



if __name__ == '__main__':
    arr = [5, 2, 8, 1, 8, 9, 4]
    bubbleSort(arr)
    print(arr)