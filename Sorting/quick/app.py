# start element as pivot

from asyncio.windows_events import INFINITE


def quickSort(arr, low, high):
    if low < high:
        pi = partition(arr, low, high)
        quickSort(arr, low, pi-1)
        quickSort(arr, pi+1, high)

def partition(arr, low, high):
    pi = arr[low]
    p = low
    q = high

    while p < q:
        while arr[p] <= pi:
            p+=1
        while arr[q] > pi:
            q-=1
        if p < q:
            swap(arr, p, q)
    swap(arr, low, q)
    return q

def swap(arr, i, j):
    arr[i], arr[j]=arr[j], arr[i]

if __name__ == "__main__":
    # arr = [45, 25, 31, 66, 54, 87]
    arr = [5, 4, 3,3, 2, 1]
    arr.append(INFINITE)
    quickSort(arr, 0, len(arr)-1)
    print(arr[:-1])

